# Lab3_Robotica_ROS
The next laboratory develops some topics about ROS and the tustlesim tool for teach Ros concepts.

The laboratory was carried out by Juan Carlos Naranjo Jaramillo in colaboration with David Santiago Rodriguez Almanza.

The matlab file turtlesim_1.m connects with master node of ROS for create a turtlesim_node that use a publish topic 'turtle1/cmd_vel' to change the properties of velocity of turtle 1, it will do a movement for a second defined by velocity parameters.

The matlab file turtle_lab.m allows the turtle1 to subscribe to the topic 'turtle1/pose' for receive the pose parameters (x, y, theta, angular velocity, linear velocity) to show them, also it can connect to the service 'turtle1/teleport_absolute' for change the position of turtle1 giving the position parameters.

https://github.com/JuanNaranjo17/Lab3_Robotica_ROS/assets/96454607/bd378a98-faf0-44b6-b862-7034ef3ffafc

The python file MyTeleopKey.py it's an aplication for control the position of the turtle1 with the keyboard, for do that, the turtle1 use the publish topic for change the velocity parameters following the keyboard input, also, it uses the service 'turtle1/teleport_absolute' for return the turtle1 to starting position, also uses the service 'turtle1/teleport_relative' for rotate the turtle1 pi radians.

https://github.com/JuanNaranjo17/Lab3_Robotica_ROS/assets/96454607/2091955f-22d4-4e95-9a1a-de39226e9da7
