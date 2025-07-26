#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
import math
import time

class NavigationCommander(Node):
    def __init__(self):
        super().__init__('navigation_commander')

        self.goal_pub = self.create_publisher(PoseStamped, '/goal_pose', 10)
        self.init_pub = self.create_publisher(PoseWithCovarianceStamped, '/initialpose', 10)

        self.timer = self.create_timer(2.0, self.send_commands)
        self.sent = False

    def send_commands(self):
        if self.sent:
            return

        # ✅ 초기 위치 설정
        init_msg = PoseWithCovarianceStamped()
        init_msg.header.frame_id = 'map'
        init_msg.pose.pose.position.x = 0.0
        init_msg.pose.pose.position.y = 0.0
        init_msg.pose.pose.orientation.w = 1.0  # 0도 회전

        self.init_pub.publish(init_msg)
        self.get_logger().info("✅ Published initial pose")

        time.sleep(1.0)  # 약간의 시간 기다려주기

        # ✅ 목표 위치 설정
        goal_msg = PoseStamped()
        goal_msg.header.frame_id = 'map'
        goal_msg.pose.position.x = 2.0
        goal_msg.pose.position.y = 1.5
        yaw_rad = math.radians(90)
        goal_msg.pose.orientation.z = math.sin(yaw_rad / 2)
        goal_msg.pose.orientation.w = math.cos(yaw_rad / 2)

        self.goal_pub.publish(goal_msg)
        self.get_logger().info("🎯 Published goal pose")

        self.sent = True

def main(args=None):
    rclpy.init(args=args)
    node = NavigationCommander()
    rclpy.spin_once(node, timeout_sec=5.0)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
