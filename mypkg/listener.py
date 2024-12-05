import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.sub = self.create_subscription(Int16, "countup", self.cb, 10)

#rclpy.init()
#node = Node("listener")


    def cb(self, msg):
        self.get_logger().info(f"I heard: {msg.data}")
    #global node
    #node.get_logger().info("Listen: %d" % msg.data)


def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

    #pub = node.create_subscription(Int16, "countup", cd, 10)
    #rclpy.spin(node)
