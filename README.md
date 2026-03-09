# Real-Time ML Streaming Service

A real-time machine learning microservice built with Kafka and Python.
This project demonstrates processing streaming data and performing instant ML inference.

## Features
- Event streaming using Apache Kafka
- Real-time ML inference with Scikit-learn
- Dockerized microservices for deployment
- Logging predictions to database
- Example: fraud detection or anomaly detection

## Architecture
Producer → Kafka → ML Consumer → Prediction Service → Database

## Run
1. Start Kafka broker (docker-compose)
2. Start producer script to send data
3. Start consumer API to serve predictions
4. Monitor logs or DB for results