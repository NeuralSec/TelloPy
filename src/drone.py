import socket
import threading

class Drone:
  def __init__(self, drone_ip, drone_port, local_ip, local_port):
    # Drone Object Constructor
    # Runs when you create a new Drone object

    # Networking Destination
    self.ip = drone_ip
    self.port = drone_port
    self.address = (self.ip, self.port)

    # UDP Socket for communication (Computer -> Drone)
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind socket to local IP and port
    self.socket.bind((local_ip, local_port))

    # Two counters to track how many times data was sent or received
    self.send_id = 0
    self.receive_id = 0

    # Since receiving data has to be done alongside sending...
    # ..., a thread will be assigned to handle receiving data
    self.receiver_thread = threading.Thread(target=self.receive)
    self.receiver_thread.daemon = True

  def send(self, content):
    # Send data through the UDP socket to the drone
    # Encode data with utf-8 standard

    # Run loop until send_id matches receive_id
    while True:
      if (self.send_id == self.receive_id):
        break
    
    self.send_id += 1
    self.socket.sendto(content.encode('utf-8'), self.address)

    print("SEND #%s: %s" % (self.send_id, content))

  def receive(self): 
    # This function is not mainly to receive data from drone...
    # ...but to delay next command until previous command is acknowleged
    while True:
      response, receiver_ip = self.socket.recvfrom(2048)
      self.receive_id += 1

      print("RECV #%s: %s" % (self.receive_id, response))

  # Emergency Stop Function
  # Cuts the motors, stops the receiver thread, closes the connection
  # Use with care
  def emergency_stop(self):
    self.socket.sendto("emergency".encode('utf-8'), self.address)
    self.receiver_thread.stop()
    self.socket.close()

  # Below are functions for moving the drone
  def takeoff(self):
    self.send("takeoff")

  def land(self):
    self.send("land")
  
  def go_forward(self, distance):
    self.send("forward %s" % (str(distance)))

  def go_back(self, distance):
    self.send("back %s" % (str(distance)))

  def go_left(self, distance):
    self.send("left %s" % (str(distance)))

  def go_right(self, distance):
    self.send("right %s" % (str(distance)))

  def rotate_cw(self, degrees):
    self.send("cw %s" % (str(degrees)))

  def rotate_ccw(self, degrees):
    self.send("ccw %s" % (str(degrees)))

  def go_up(self, height):
    self.send("up %s" % (str(height)))

  def go_down(self, height):
    self.send("down %s" % (str(height)))

  def hover(self):
    # Stops the drone mid-air
    self.send("stop")

  def initialize(self):
    # Start receiver thread
    self.receiver_thread.start()

    # Establish connection and initialize SDK mode on drone
    self.send('command')

  # FOR TESTING ONLY
  # def test(self):
  #   self.send('takeoff')
  #   self.send('land')