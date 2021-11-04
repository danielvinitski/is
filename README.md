# IS Buy tool

[Cellwize Chime](https://www.cellwize.com/) has multiple components, but as a whole, it provides you a wide range of capabilities to improve and optimize existing Cellular infrastructure. 

## TL;DR

```console
$ docker-compose up
```

## Introduction

This Docker compose orchestrate the deployment of customer-api-server, customer-management, mongoDB, Kafka and Zookeeper.  

## Prerequisites

- Docker
- Docker-compose


## Installing the stack

To install the Stack run the command:

```console
$ docker-compose up -d
```

## Parameters

The following table lists the configurable parameters of each service.

### customer-api-server

| Parameter             | Description                            | Default                 |
|-----------------------|----------------------------------------|-------------------------|
| `KAFKA_ENDPOINT`      | `Kafka bus endpoint`                   | `localhost:9093`        |
| `KAFKA_TOPIC`         | `kafka topic to produce`               | `buy`                   |
| `MANAGEMENT_ENDPOINT` | `customer-management service endpoint` | `http://127.0.0.1:5005` |
| `SERVER_PORT`         | `Server port to run the service`       | `5000`                  |

### customer-management

| Parameter             | Description                                | Default                 |
|-----------------------|--------------------------------------------|-------------------------|
| `KAFKA_ENDPOINT`      | `Kafka bus endpoint`                       | `localhost:9093`        |
| `KAFKA_TOPIC`         | `kafka topic to consume`                   | `buy`                   |
| `KAFKA_GROUP_ID`      | `Kafka group id`                           | `my-group`              |
| `SERVER_PORT`         | `Server port to run the service`           | `5005`                  |
| `MONGODB_ENDPOINT`    | `Mongodb endpoint`                         | `localhost:27017`       |
| `MONGODB_DB`          | `Server port to run the service`           | `shop`                  |

## API Calls

``


## Instruction

Run the docker Compose on your VM/laptop

To purchase:
`curl -X POST http://localhost:5000/api/v1/buy   -H 'Content-Type: application/json'   -d '{"username":"foo","userId":"1","price":"999"}'`

To get all the purchases:
`curl http://127.0.0.1:5000/api/v1/getBuyList`

https://github.com/bitnami/bitnami-docker-kafka

## More information about Mongodb docker

https://github.com/bitnami/bitnami-docker-mongodb