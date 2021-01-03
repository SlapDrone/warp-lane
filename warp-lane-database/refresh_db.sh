docker-compose down
docker volume rm warp-lane-database_app-db-data
docker-compose up -d --build application-db
docker-compose up -d
