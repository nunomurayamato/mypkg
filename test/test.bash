#!/bin/bash
# SPDX-FileCopyrightText: 2025 Yamato Nunomura  
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

timeout 10 ros2 launch mypkg memorypublisher.launch.py > /tmp/mypkg.log

if [ -s $temp_file ]; then
    echo "Test passed: Memory usage values are:"
    cat $temp_file
else
    echo "Test failed: No memory usage values recorded."
fi

rm -f $temp_file
