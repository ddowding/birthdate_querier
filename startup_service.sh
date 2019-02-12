#/bin/bash

docker-compose up -d
docker exec -it birthdate_querier python main.py --help

echo "To run a command use: docker exec -it birthdate_querier python main.py <args>"
