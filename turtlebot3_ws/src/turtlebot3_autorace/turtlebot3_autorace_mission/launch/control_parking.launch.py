#!/usr/bin/env python3
#
# Copyright 2025 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Hyungyu Kim

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    control_parking_node = Node(
        package='turtlebot3_autorace_mission',
        executable='control_parking',
        name='control_parking',
        output='screen',
        remappings=[
            ('/cmd_vel', '/cmd_vel'),
            ('/detect/parking_order', '/detect/parking_order'),
            ('/detect/parking_stamped', '/detect/parking_stamped')
        ]
    )

    return LaunchDescription([
        control_parking_node
    ])
