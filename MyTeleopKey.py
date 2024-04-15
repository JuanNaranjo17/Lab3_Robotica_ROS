import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import TeleportAbsolute, TeleportRelative
import termios, sys, os
from numpy import pi

TERMIOS = termios

def callback(msg):
    rospy.loginfo(msg.x)

def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c.decode('utf-8')

def move():
    #help(rospy.ServiceProxy)

    rospy.init_node('robot_cleaner', anonymous = True)
    rate = rospy.Rate(10)

    cmd_vel_topic = '/turtle1/cmd_vel' 
    pose_topic = '/turtle1/pose'
    tel_rel_topic = '/turtle1/teleport_relative'
    tel_abs_topic = '/turtle1/teleport_absolute' 

    velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size = 10)
    #pbscrose_sucriber = rospy.Subscriber(pose_topic, Pose, callback)
    #rospy.spin()
    relative_service = rospy.ServiceProxy(tel_rel_topic, TeleportRelative)
    absolute_service = rospy.ServiceProxy(tel_abs_topic, TeleportAbsolute)

    velocity_message = Twist()

    while not rospy.is_shutdown():

        velocity_message.linear.x = 0
        velocity_message.linear.y = 0
        velocity_message.linear.z = 0
        velocity_message.angular.x = 0
        velocity_message.angular.y = 0
        velocity_message.angular.z = 0

        tecla = getkey().lower()

        if tecla == 'w':
            velocity_message.linear.x = 1
        elif tecla == 's':
            velocity_message.linear.x = -1
        elif tecla == 'a':
            velocity_message.angular.z = pi*5/180  
        elif tecla == 'd':
            velocity_message.angular.z = -pi*5/180
        elif tecla == ' ':
            relative_service(0, pi)
        elif tecla == 'r':
            absolute_service(5.544445, 5.544445, 0)
        else:
            velocity_message.angular.z = 0

        velocity_publisher.publish(velocity_message)
        rate.sleep()
        print(tecla)

def main():
    if __name__ == '__main__':
        try:
            move()
        except rospy.ROSInterruptException: pass

main()