# cmd_vel_mux/mux_node.py

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class CmdVelMux(Node):
    def __init__(self):
        super().__init__('cmd_vel_mux')
        self.cmd_source = 'lane'  # default
        self.sub_lane = self.create_subscription(Twist, '/lane/cmd_vel', self.cb_lane, 10)
        self.sub_parking = self.create_subscription(Twist, '/parking/cmd_vel', self.cb_parking, 10)
        self.sub_traffic = self.create_subscription(Twist, '/traffic_light/cmd_vel', self.cb_traffic, 10)
        self.sub_tunnel = self.create_subscription(Twist, '/tunnel/cmd_vel', self.cb_tunnel, 10)
        self.sub_source = self.create_subscription(String, '/mode/cmd_source', self.cb_source, 10)
        self.pub_cmd = self.create_publisher(Twist, '/cmd_vel', 10)

    def cb_lane(self, msg):
        if self.cmd_source == 'lane':
            self.pub_cmd.publish(msg)

    def cb_parking(self, msg):
        if self.cmd_source == 'parking':
            self.pub_cmd.publish(msg)

    def cb_traffic(self, msg):
        if self.cmd_source == 'traffic_light':
            self.pub_cmd.publish(msg)

    def cb_tunnel(self, msg):  
        if self.cmd_source == 'tunnel':
            self.pub_cmd.publish(msg)

    def cb_source(self, msg):
        self.cmd_source = msg.data
        self.get_logger().info(f'CMD source set to: {self.cmd_source}')


def main(args=None):
    rclpy.init(args=args)
    node = CmdVelMux()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

