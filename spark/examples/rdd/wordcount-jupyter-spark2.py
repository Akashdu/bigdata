from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("PythonWordCount").getOrCreate()
lines = spark.sparkContext.textFile("/data/mr/wordcount/input/")
words = lines.flatMap(lambda x: x.split(' '))
tuples = words.map(lambda x: (x.lower(), 1))
result = tuples.reduceByKey(lambda x, y: x + y)
ordered = result.sortBy(lambda x: -x[1])
ordered.take(10)
