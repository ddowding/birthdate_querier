# A service for querying birth dates

* This requires docker compose to run, it can be installed with:
```
pip3 install docker-compose
```

## Run
* `./startup_service.sh`
* Execute a query on the container: `docker exec -it birthdate_querier python main.py --query birthday`
* Stop the service `docker-compose down`

## Example scripts
* Some example scripts exist that have example queries inside: e.g:
    * ./example_query_scripts/query_age_over_n.sh`
    * This will execute `python main.py --age_over_n 22` on the running container.

## Command usage:
* Running `docker exec -it birthdate_querier python main.py --help` will show the usage of the container

```
usage: main.py [-h] [--query QUERY] [--age_over_n N] [--delete DELETE]

User query engine

optional arguments:
  -h, --help            show this help message and exit
  --query QUERY, -q QUERY
                        --query birthdays # number of birthdays today. --query
                        uuid # list of uuid's of user's birthdays
  --age_over_n N, -a N  --age_over_n <query age> # query ages over n
  --delete DELETE, -d DELETE
                        --delete <uuid> # Deletes user based on UUID.

```

## Mounting csv's

* The container mounts the csv under the ``./Data/users.csv` path
