# TelloPy
Python API for interacting with DJI Tello Drones using the official SDK. Developed by __Niaz M. Sameer__ for the __CCC Kei Long College Computer Society.__

## Usage
### How to send instructions to the drone
1. Download or clone this git repository onto your computer.
2. Open the `main.py` file
3. Under the `# Write your instructions here:` comment, write all the instructions you'd like to send to the drone.
### How to use the API
#### Initalizing the drone object
Before anything, you must first initialize the drone object. A drone object will have already been created in `main.py` like this `Tello = Drone("192.168.10.1", 8889, "192.168.10.2", 8889)`.

In your instructions, write `Tello.initialize()` to initialize the drone object.

Once you have initialized the drone object, you can now start sending commands.

#### Taking off
`Tello.takeoff()`

#### Landing
`Tello.land()`

#### Moving forward
`Tello.go_forward(distance)`

#### Moving left
`Tello.go_left(distance)`

#### Moving right
`Tello.go_right(distance)`

#### Moving back
`Tello.go_back(distance)`

#### Going upwards
`Tello.go_up(height)`

#### Going downwards
`Tello.go_down(height)`

#### Rotating clockwise
`Tello.rotate_cw(angle)`

#### Rotating counter-clockwise
`Tello.rotate_ccw(angle)`

## In an emergency...
If, for any reason, you need your drone to stop immediately and fall to the ground, don't worry, I developed a solution! In `main.py`, a signal handler has been implemented to detect a KeyboardInterupt (Ctrl+C). By pressing Ctrl+C, the API will signal the drone to stop its motors immediately and your computer will cut the connection. __Use this with care as the falling drone may injure someone.__
