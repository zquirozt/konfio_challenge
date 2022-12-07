
# Coding Challenge - Bitcoin Price (KONFIO)

The objective is develop an automated and scalable process to obtain the average of each 5 days (moving average) of the price of bitcoin in the first quarter of 2022.
This challenge install and configure Grafana using PostgreSQL as datasource.

## Requeriments

[docker](https://docs.docker.com/engine/install/ubuntu/)

[docker-compose](https://docs.docker.com/compose/) 

## How to run?

To run: 

```
docker compose up
```


> **Note:** If you have **problems** reloading code changes **run**: docker system prune -a


To bulk data to postgres database:

```
curl --location --request POST 'localhost:8000/bulk'
```
## How to visualize the results?

Open [Grafana](http://localhost:3000) on explorer with the follow credentials:

```
user = admin
password = admin
```
> **Note:** You need **change** and **confirm** the new password

In the **Dashboards panel** you can find the **Bitcoin prices** graph.

## Motivations

### Why a rest-API to bulk data?

- Easy access to trigger the bulk process
- Get the access to the local docker network (Static IPs)

### Why docker?
- Consistent & Isolated Environment
- Rapid Application Deployment
- Better Portability


## Nice to have (with more time of develop)

- **unit test** to the bulk process.
- **automate** the bulk process.