from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlebot3_autorace_detect',
            executable='detect_signcombine',
            name='detect_signcombine',
            output='screen',
            remappings=[
                ('/detect/image_input', '/camera/image_compensated'),
                ('/detect/image_input/compressed', '/camera/image_compensated/compressed'),
                ('/detect/image_output', '/detect/image_traffic_sign'),
                ('/detect/image_output/compressed', '/detect/image_traffic_sign/compressed'),
            ]
        )
    ])
