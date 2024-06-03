# Smart city project

## Objective
This project will be building a Smart City End to End Realtime data streaming pipeline covering each phase from data ingestion to processing and finally storage. We'll utilize tools like IOT devices, Apache Zookeeper, Apache Kafka, Apache Spark, Docker, Python, AWS Cloud, AWS Glue, AWS Athena, AWS IAM, AWS Redshift and further we can use PowerBI to visualize data on Redshift.


## Problem
![Problem](/map.png)

Suppose we go from London to Birmingham by car and it takes more than 2 hours to travel. We will design a pipeline that is responsible for collecting information from IOT devices such as vehicles, GPS, cameras, weather, and incident information. This pipeline will retrieve information from many sources and process and store data in the cloud in real-time. From that data, it can be fed into systems to visualize or suggest more optimal routes.


## System Architecture

![System Architecture](/arrchitecture.png)

## Flow

1. Data come from many sources:
    - Vihicle information
    - GPS information
    - Cameras information
    - Weather information
    - Emergency information
2. Kafka control information comes from sources.
3. Consumer with Apache Spark that listening to events that are coming into Kafka.
4. Spark streaming written data into S3 bucket.
5. Then AWS Glue extract information from raw storage using data catalog.
6. Finally, we can access data with Amazon Athena or Redshift.

## File Description
- **Docker-compose.yml** implement Kafka service include Zookeeper and Kafa, and Spark include 1 master node and 2 worker.
- **main.py** 
    - Implement function generate data for vihicle, gps, camera, weather, emergency, function push data to topic of kafka. This also have function for simulate data generation for journey. 
    - Simulated data is generated continuously along the way and is continuously pushed to the kafka topic.

- **spark-city.py** create spark session with configuration to access data stored in Amazon S3. Then Spark will read data stream from Kafka topic. Finally, Spark write data to S3 bucket

## Config AWS describe
### 1. S3 Storage
![S3 Storage](/s3.png)
- Storage data in specific folder, the data save with format parquet file.

### 2. Glue
### Glue Crawler
Glue crawler will crawl data from S3 to save it in table format
![Glue Crawler](/crawler.png)

### Glue Catalogs
![Glue Catalogs](/glue_table.png)

### 3. Athena
Query data from AWS Data Catalog
![Athena](/athena.png)

### 4. Redshift
Connect to Redshift using account config in Redshift. And ingest data from Catalog to database in redshift. Then we can query data in redshift.
![Redshift](/redshift.png)

### 5. IAM
Create IAM role for permissions access service S3 and Glue
![IAM](/iam_role.png)


