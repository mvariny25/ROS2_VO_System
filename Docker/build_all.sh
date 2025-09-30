DOCKERFILE=$1

docker stop vo_system
docker rm -f vo_system

docker build -t vo_system -f "$DOCKERFILE" .