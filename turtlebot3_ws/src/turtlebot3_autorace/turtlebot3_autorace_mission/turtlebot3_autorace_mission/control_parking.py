#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import UInt8

class ControlParking(Node):
    def __init__(self):
        super().__init__('control_parking')

        # Subscriber to receive parking state
        self.create_subscription(UInt8, '/detect/parking_stamped', self.cb_parking_state, 10)

        # Publisher to send parking order
        self.pub_parking_order = self.create_publisher(UInt8, '/detect/parking_order', 10)

        # Publisher to stop the robot if needed
        self.pub_cmd_vel = self.create_publisher(Twist, '/cmd_vel', 10)

        # Start by sending parking command
        self.get_logger().info('[Control] Sending parking order')
        self.send_parking_command(1)  # 1: parking

    def send_parking_command(self, command_value):
        msg = UInt8()
        msg.data = command_value
        self.pub_parking_order.publish(msg)

    def cb_parking_state(self, msg):
        if msg.data == 2:  # exit
            self.get_logger().info('[Control] Parking completed. Stopping robot.')
            self.stop_robot()

    def stop_robot(self):
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.pub_cmd_vel.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    node = ControlParking()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
