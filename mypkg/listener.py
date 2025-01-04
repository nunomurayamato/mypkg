#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Yamato Nunomura
# SPDX-License-Identifier: BSD-3-Clausei

import rclpy
from rclpy.node import Node
<<<<<<< HEAD
from person_msgs.srv import Query
=======
from std_msgs.msg import Float64  # メモリ使用量を受け取るのでFloat64型を使用

class MemoryListener(Node):
    def __init__(self):
        super().__init__('memory_listener')
        self.subscription = self.create_subscription(
            Float64,
            'memory_usage',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.get_logger().info('Memory Listener Node has been started.')

    def listener_callback(self, msg):
        self.get_logger().info(f'Received memory usage: {msg.data:.2f} MB')
>>>>>>> lesson10.1


def main(args=None):
    rclpy.init(args=args)
    node = MemoryListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Memory Listener stopped cleanly.')
    finally:
        node.destroy_node()
        rclpy.shutdown()

<<<<<<< HEAD
def main():
    client = node.create_client(Query, 'query')
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('待機中')

    req = Query.Request()
    req.name = "布村大和"
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('呼び出し失敗')
            else:
                node.get_logger().info("age:{}".format(response.age))

            break

    node.destroy_node()
    rclpy.shutdown()
=======

if __name__ == '__main__':
    main()
>>>>>>> lesson10.1

