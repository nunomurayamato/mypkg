#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Yamato Nunomura
# SPDX-License-Identifier: BSD-3-Clausei

import os
import psutil
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64


class MemoryUsagePublisher(Node):
    def __init__(self):
        super().__init__('memory_usage_publisher')
        self.publisher_ = self.create_publisher(Float64, 'memory_usage', 10)
        self.timer = self.create_timer(1.0, self.publish_memory_usage)
        self.process = psutil.Process(os.getpid())  
        self.get_logger().info('Memory Usage Publisher Node has been started.')

    def publish_memory_usage(self):
        memory_usage = self.process.memory_info().rss / (1024 * 1024)  
        self.publisher_.publish(Float64(data=memory_usage))
        self.get_logger().info(f'Publishing memory usage: {memory_usage:.2f} MB')


def main(args=None):
    rclpy.init(args=args)
    node = MemoryUsagePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Node stopped cleanly.')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

