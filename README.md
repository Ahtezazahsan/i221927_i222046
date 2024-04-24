# Real-time Data Processing with MongoDB Integration

# Introduction:

In this project, I focused on real-time data processing using Apache Kafka and integration with MongoDB. My goal was to demonstrate the streaming and processing of a sampled version of the Amazon Metadata dataset, applying frequent itemset mining algorithms, and storing the results in MongoDB.

# Dataset Description:

I utilized the Amazon Metadata dataset, which comprises JSON objects containing attributes such as asin, title, feature, description, price, imageURL, categories, etc. To ensure manageability for processing, I sampled the dataset.

# Pre-Processing:

Loading Data: I loaded the sampled Amazon dataset into memory.
Data Cleaning: I performed preprocessing to remove inconsistencies, handle missing values, and format the data for analysis.
JSON File Generation: I created a new JSON file containing the preprocessed data.
Real-time Pre-processing: I implemented batch processing to execute pre-processing in real-time.
Streaming Pipeline Setup:

Producer Application: I developed a producer application to stream preprocessed data in real-time.
Consumer Applications: I created three consumer applications to subscribe to the producer's data stream.
# Frequent Itemset Mining:

Apriori Algorithm: I implemented the Apriori algorithm in one consumer to provide real-time insights and associations.
PCY Algorithm: I implemented the PCY algorithm in another consumer to offer real-time insights and associations.
Custom Algorithm: In the third consumer, I implemented a custom algorithm focusing on innovation and creativity, adapting it to the streaming environment.
# Database Integration:

I chose MongoDB for database integration due to its suitability for real-time streaming applications. I modified each consumer to connect to MongoDB and store the processed data.

# Running the Project:

Ensure Apache Kafka and MongoDB are installed and running.
Execute the producer application to initiate streaming of preprocessed data.
Run the consumer applications to process and store data in MongoDB.
Bonus: Enhancing Project Execution with a Bash Script:

I provided a bash script to streamline project execution by running the producer and consumers and initializing all Kafka components.

Conclusion:

This project exemplifies my implementation of real-time data processing with Apache Kafka and MongoDB integration. I showcased innovative approaches to adapt algorithms to the streaming environment, offering a comprehensive solution for real-time analytics and data processing.
