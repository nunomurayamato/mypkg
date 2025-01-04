#!/bin/bash
# SPDX-FileCopyrightText: 2025 Yamato Nunomura  
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

timeout 10 ros2 launch mypkg Memorypublisher.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'Publishing memory usage: {memory_usage:.2f} MB'
