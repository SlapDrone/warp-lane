FROM postgres:13.1
COPY ["./db_scripts/0100_tables", "./db_scripts/1000_data", "./db_scripts/2000_views", "/docker-entrypoint-initdb.d/"]