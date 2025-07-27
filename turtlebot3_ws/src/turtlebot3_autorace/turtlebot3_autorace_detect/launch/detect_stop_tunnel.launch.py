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
# Author: Jihoon Choi (or your name)

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Node for stopping when tunnel is detected
    stop_on_tunnel_node = Node(
        package='turtlebot3_autorace_detect',  # ❗여기에는 실제 패키지 이름을 넣어야 함
        executable='detect_stop_tunnel',          # ❗빌드된 실행 파일 이름
        name='detect_stop_tunnel',
        output='screen',
        remappings=[
            ('/cmd_vel', '/cmd_vel'),  # mux가 처리하므로 일반적인 토픽은 그대로 유지
            ('/tunnel/cmd_vel', '/tunnel/cmd_vel'),  # 정지용 cmd_vel
            ('/detect/traffic_sign', '/detect/traffic_sign'),  # 표지판 인식 결과
            ('/mode/cmd_source', '/mode/cmd_source')  # mux 전환용
        ]
    )

    return LaunchDescription([
        stop_on_tunnel_node
    ])
