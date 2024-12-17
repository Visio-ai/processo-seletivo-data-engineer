from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum

# Configuração do Spark
    # .config("spark.executor.extraClassPath", "/opt/spark/jars/postgresql.jar")\
spark = SparkSession.builder \
    .appName("Example Pipeline") \
    .config("spark.jars", "/my-jars/postgresql.jar") \
    .master("spark://spark:7077") \
    .getOrCreate()
spark.sparkContext.setLogLevel('WARN')

postgres_url = "jdbc:postgresql://postgres:5432/medallion_pipeline"
user = "your_username"
password = "your_password"

data = [
    (1, "Alice", 30),
    (2, "Bob", 25),
    (3, "Cathy", 27)
]
columns = ["id", "name", "age"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

df.write.format("jdbc")\
.option("url", postgres_url) \
.option("dbtable", "my_table") \
.option("user", user) \
.option("password", password) \
.option("driver", "org.postgresql.Driver") \
.mode("overwrite") \
.save()

df = spark.read \
.format("jdbc") \
.option("url", postgres_url) \
.option("driver", "org.postgresql.Driver").option("dbtable", "my_table") \
.option("user", user) \
.option("password", password) \
.load()

df.show()
