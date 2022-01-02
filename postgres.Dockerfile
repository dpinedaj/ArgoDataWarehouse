FROM postgres:latest
COPY ./config/init_db/create_tables.sql /docker-entrypoint-initdb.d/create_tables.sql
