xhost +local:root

docker start vo_system 2> /dev/null

docker exec -it vo_system bash