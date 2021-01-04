To setup the db and pgadmin on it's own you can just run

```bash
docker-compose up -d
```

Run the `refresh_db.sh` script to tear down running container instances, delete the volumes, rebuild the psql container and re-deploy.

Pgadmin is reachable at localhost:8080.
Login to pgadmin is

    username: dev@pomeron.com
    password: secret

Login to database is:

    username: admin 
    password: secret
