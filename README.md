# ArgoDataWarehouse

## Description
- Data migration solution using Argo as orchestator to run multiple Cron Workflows simultaneously using different kubernetes pods.

- The solution architecture is based on hexagonal architecture or ports and adapters design pattern.

- The data warehouse (in this case a relational database) is on postgres which is very limited in performance, handling partitions, indenxes and so on.

- The database is designed in two schemas `raw` and `processed` to handle the data as is and processed with a fixment in the data schema, the tables are also partitioned by date.

## Usage:
- Prepare kubernetes environment
- Install argo: look at https://github.com/argoproj/argo-workflows/releases/tag/v3.2.6
- Setup argo deployment using: make init-argo
- Setup workflows using: make setup-workflows

## Monitoring:
- To monitor the workflows argo have a full managed UI, you can visualize it using: make argo-ui and going to http://localhost:2746
- To monitor the database behaviour, you can also connect to the db using: make db-ui and connecting with your preferred IDE with the credentials for the dummy case are:
    - postgres_user: postgres
    - postgres_password: password
    - postgres_db: postgres
