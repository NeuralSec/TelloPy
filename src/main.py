import signal
import sys
from drone import Drone

Tello = Drone("192.168.10.1", 8889, "192.168.10.2", 8889)

# Emergency Handler
# Press Ctrl-C in an emergency to stop the drone immediately
def signal_handler(sig, frame):
  print("\nEMERGENCY STOP! WATCH OUT FOR FALLING DRONE!")
  Tello.emergency_stop()
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Write your instructions here:

# Example:
# Tello.initialize()
# Tello.takeoff()
# Tello.go_up(20)
# Tello.go_down(20)
# Tello.land()