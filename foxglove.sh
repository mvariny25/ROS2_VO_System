#!/bin/bash
export COLCON_WS=~/colcon_ws
# export ROS_WS=~/ros_ws 


source /opt/ros/humble/setup.bash
source ${COLCON_WS}/install/setup.bash
# echo "source ${ROS_WS}/install/setup.bash" >> ~/.bashrc || true


ros2 launch foxglove_bridge foxglove_bridge_launch.xml port:=8765