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
    control_traffic_node = Node(
        package='turtlebot3_autorace_mission',  # ← 사용 중인 패키지명으로 바꿔주세요
        executable='control_traffic_light',
        name='control_traffic_light',
        output='screen',
        remappings=[
            ('/traffic_light_color', '/traffic_light_color'),
            ('/traffic_light/cmd_vel', '/traffic_light/cmd_vel'),
            ('/mode/cmd_source', '/mode/cmd_source')
        ]
    )

    return LaunchDescription([
        control_traffic_node
    ])
