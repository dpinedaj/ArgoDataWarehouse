FROM postgres:latest

# TODO: Temporal ENV
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=admin
ENV POSTGRES_DB=pruebas

COPY ./config/init_db/create_tables.sql /docker-entrypoint-initdb.d/create_tables.sql
