from pyspark.sql import SparkSession\nfrom pyspark.sql.functions import *\n\n# Create SparkSession\nspark = SparkSession.builder \
    .appName("KafkaStreamReader") \
    .getOrCreate()\n\n# Read from Kafka\nkafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "your_kafka_topic") \
    .load()\n\n# Process the data\nkafka_df = kafka_df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")\n\n# Define query to write the output to console\nquery = kafka_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()\n\n# Await termination of the streaming query\nquery.awaitTermination()