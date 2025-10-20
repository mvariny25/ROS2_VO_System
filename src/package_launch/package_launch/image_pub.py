# #!/usr/bin/env python3
# import rclpy
# from rclpy.node import Node
# from sensor_msgs.msg import Image
# from cv_bridge import CvBridge
# import cv2

# class WebcamPublisher(Node):
#     def __init__(self):
#         super().__init__('webcam_publisher')
#         self.publisher_ = self.create_publisher(Image, '/camera', 10)
#         self.timer = self.create_timer(0.01, self.timer_callback)  # 10 Hz
#         self.cap = cv2.VideoCapture(0)  # 0 is default webcam
#         self.bridge = CvBridge()
#         if not self.cap.isOpened():
#             self.get_logger().error("Could not open webcam!")

#     def timer_callback(self):
#         ret, frame = self.cap.read()
#         if not ret:
#             self.get_logger().error("Failed to capture image")
#             return
        
#         gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         msg = self.bridge.cv2_to_imgmsg(gray_frame, encoding="mono8")
#         self.publisher_.publish(msg)
#         self.get_logger().info("Published webcam image")

# def main(args=None):
#     rclpy.init(args=args)
#     node = WebcamPublisher()
#     try:
#         rclpy.spin(node)
#     except KeyboardInterrupt:
#         pass
#     node.cap.release()
#     node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()
# #!/usr/bin/env python3
# import rclpy
# from rclpy.node import Node
# from sensor_msgs.msg import Image
# from cv_bridge import CvBridge
# import cv2

# class WebcamPublisher(Node):
#     def __init__(self):
#         super().__init__('webcam_publisher')
#         self.publisher_ = self.create_publisher(Image, '/camera', 10)
#         self.timer = self.create_timer(0.01, self.timer_callback)  # 10 Hz
#         self.cap = cv2.VideoCapture(0)  # 0 is default webcam
#         self.bridge = CvBridge()
#         if not self.cap.isOpened():
#             self.get_logger().error("Could not open webcam!")

#     def timer_callback(self):
#         ret, frame = self.cap.read()
#         if not ret:
#             self.get_logger().error("Failed to capture image")
#             return
        
#         gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         msg = self.bridge.cv2_to_imgmsg(gray_frame, encoding="mono8")
#         self.publisher_.publish(msg)
#         # self.get_logger().info("Published webcam image")


# # class ImageListener(Node):
# #     def __init__(self):
# #         super().__init__('image_listener')
# #         self.publisher_ = self.create_publisher(Image, '/camera', 10)
# #         # self.timer = self.create_timer(0.01, self.listener_callback)  # 10 Hz
# #         self.bridge = CvBridge()

# #         # Subscribe to *any* image topic (use remapping at launch if needed)
# #         self.subscription = self.create_subscription(
# #             Image,
# #             '/image',  # default topic, can be remapped at runtime
# #             self.listener_callback,
# #             10)
# #         self.subscription  # prevent unused variable warning

# #     def listener_callback(self, msg: Image):
# #         # Convert ROS Image to OpenCV image
# #         try:
# #             cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            
# #             ret, frame = cv_image.read()
# #             gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# #             msg = self.bridge.cv2_to_imgmsg(gray_frame, encoding="mono8")
# #             self.publisher_.publish(msg)
# #             # For testing, show the frame
# #             # cv2.imshow("Incoming Image", cv_image)
# #             # cv2.waitKey(1)
# #             # self.get_logger().info("Published webcam image")

# #         except Exception as e:
# #             self.get_logger().error(f"Failed to convert image: {e}")


# # class ImageProcessor(Node):
# #     def __init__(self):
# #         super().__init__('image_processor')
# #         self.bridge = CvBridge()

# #         # Subscribe to any input image topic
# #         self.subscription = self.create_subscription(
# #             Image,
# #             '/image',   # remap this if needed
# #             self.listener_callback,
# #             10)

# #         # Publisher for processed (grayscale) images
# #         self.publisher_ = self.create_publisher(Image, '/camera', 10)
# #         self.timer = self.create_timer(0.01, self.timer_callback) 

# #     def listener_callback(self, msg: Image):
# #         try:
# #             # Convert ROS Image → OpenCV frame
# #             cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

# #             # Convert to grayscale
# #             gray_frame = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
# #             self.gf = gray_frame
# #             # Convert OpenCV → ROS Image
# #             out_msg = self.bridge.cv2_to_imgmsg(gray_frame, encoding="mono8")

# #             # Publish processed image
# #             # self.publisher_.publish(out_msg)
# #             # self.get_logger().info("Published grayscale image")

# #         except Exception as e:
# #             self.get_logger().error(f"Image processing failed: {e}")
# #     def timer_callback():
# #         msg = self.bridge

#         #         gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# #         msg = self.bridge.cv2_to_imgmsg(gray_frame, encoding="mono8")
# #         self.publisher_.publish(msg)
# #         # self.get_logger().info("Published webcam image")


# def main(args=None):
#     rclpy.init(args=args)
#     node = WebcamPublisher()
#     # node = ImageListener()
#     # node = ImageProcessor()
#     try:
#         rclpy.spin(node)
#     except KeyboardInterrupt:
#         pass
#     # node.cap.release()
#     node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()

#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import urllib.request
from std_msgs.msg import String
import os
import datetime as dt
from datetime import datetime as dtt
import numpy as np
import time

def download_image_in_memory(url):
    resp = urllib.request.urlopen(url)
    image_data = resp.read()
    arr = np.asarray(bytearray(image_data), dtype=np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    return img

class WebcamPublisher(Node):
    def __init__(self):
        super().__init__('webcam_publisher')
        self.publisher_ = self.create_publisher(Image, '/camera', 10)
        self.timer = self.create_timer(0.01, self.timer_callback)  # 10 Hz
        self.cap = cv2.VideoCapture(0)  # 0 is default webcam
        self.bridge = CvBridge()
        if not self.cap.isOpened():
            self.get_logger().error("Could not open webcam!")

    def timer_callback(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().error("Failed to capture image")
            return
        
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        msg = self.bridge.cv2_to_imgmsg(gray_frame, encoding="mono8")
        self.publisher_.publish(msg)
        self.get_logger().info("Published webcam image")

class FlightGearPublisher(Node):
    def __init__(self):
        super().__init__('flightgear_publisher')
        self.publisher_ = self.create_publisher(Image, '/camera', 10)
        self.bridge = CvBridge()
        self.image_url = 'http://localhost:7000/screenshot?window=sview&type=png'
        # timestamp_str = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        # self.folder_name = f"images_{timestamp_str}"
        # os.makedirs("images", exist_ok=True)
        # os.makedirs(f"images/{self.folder_name}", exist_ok = True)
        # self.image_counter = 0
        self.timer = self.create_timer(0.01, self.timer_callback)

    def timer_callback(self):
        try:
            image = download_image_in_memory(self.image_url)
            # ret, frame = image.read()
            gray_frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            msg = self.bridge.cv2_to_imgmsg(gray_frame, encoding="mono8")
            self.publisher_.publish(msg)
            self.get_logger().info("Published flightgear image")


        except:
            print('Could not grab image from URL')
def main(args=None):
    rclpy.init(args=args)
    # node = WebcamPublisher()
    node = FlightGearPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.cap.release()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
