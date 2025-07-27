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

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    detect_parking_node = Node(
        package='turtlebot3_autorace_detect',  # 🚨 여기 패키지 이름이 맞는지 꼭 확인!
        executable='detect_parking',           # 실행 파일 이름
        name='detect_parking',
        output='screen'
    )

    return LaunchDescription([
        detect_parking_node
    ])
