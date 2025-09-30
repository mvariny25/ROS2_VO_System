# ARG ROS_DISTRO
# ARG ROS_ARCH


FROM osrf/ros:humble-desktop-full
# FROM osrf/ros:rolling-desktop-full
# ARG ROS_DISTRO
# ARG ROS=ros-${ROS_DISTRO}
# ARG USR=root

# ARG HOST_USERNAME
# ARG HOST_UID
# ARG HOST_GROUPNAME
# ARG HOST_GID

RUN mkdir -p /root/colcon_ws/src
WORKDIR /root/colcon_ws

# RUN groupadd -g ${HOST_GID} ${HOST_USERNAME} && \
#     useradd -u ${HOST_UID} -g ${HOST_GID} -m ${HOST_USERNAME}


SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y sudo vim nano curl socat terminator python3-pip


RUN apt clean && apt-get update && apt-get install -y \
    build-essential \
    libeigen3-dev \
    libjsoncpp-dev \
    libspdlog-dev \
    libwebsocketpp-dev \
    libcurl4-openssl-dev \
    cmake \
    python3-pip \
    python3-colcon-common-extensions \
    python3-rosdep \
    python3-rosinstall \
    python3-vcstool \
    git \
    curl \
    dh-make \
    fakeroot \
    terminator \
    net-tools \
    && apt-get clean

# RUN git clone https://github.com/stevenlovegrove/Pangolin && cd Pangolin

# RUN ./scripts/install_prerequisites.sh --dry-run recommended && \
#     ./scripts/install_prerequisites.sh recommended && \
#     cmake -B build && \
#     cmake --build build -j4 && \
#     sudo cmake --install build

# RUN export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/local && \
#     sudo ldconfig && \
#     source ~/.bashrc

# RUN cd ~ && \
#     mkdir -p ~/ros2_test/src && \
#     cd ~/ros2_test/src && \
#     git clone https://github.com/Mechazo11/ros2_orb_slam3.git && \
#     cd .. # make sure you are in ~/ros2_ws root directory && \
#     rosdep install -r --from-paths src --ignore-src -y --rosdistro humble && \
#     source /opt/ros/humble/setup.bash && \
#     colcon build --symlink-install
# Uncomment this to support building .debs for new ROS distros, where we are not in the index yet; add distro to yaml.
#RUN echo "yaml file:///home/build/docker/rosdep.yaml" > /etc/ros/rosdep/sources.list.d/50-local-packages.list

# RUN apt-get update && apt install ros-humble-novatel-oem7-driver -y
RUN apt-get update && apt-get install -y \
    ros-humble-foxglove-bridge \
    ros-humble-usb-cam 

ENV COLCON_WS=/root/colcon_ws

# Create expected directories (will be overwritten by mounts at runtime)
RUN mkdir -p ${ROS_WS}/src ${COLCON_WS}/src

# rosdep init & update (safe to do here)
RUN rosdep update && sudo rosdep fix-permissions && rosdep update

WORKDIR ${COLCON_WS}


CMD ["bash", "-l"]
