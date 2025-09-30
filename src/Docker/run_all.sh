xhost +local:root

docker run -it \
    --name=vo_system \
    --volume="$(pwd):/root/colcon_ws" \
    --env="DISPLAY=$DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --volume="/dev:/dev" \
    --device-cgroup-rule='c 81:* rmw' \
    --net=host \
    --privileged \
    --volume="/etc/timezone:/etc/timezone:ro" \
    --volume="/etc/localtime:/etc/localtime:ro" \
    vo_system \
    bash

echo "Done."