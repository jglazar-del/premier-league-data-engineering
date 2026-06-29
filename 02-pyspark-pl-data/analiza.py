from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("analysis") \
    .getOrCreate()

data = spark.read.csv("../E0.csv", header=True, inferSchema=True)

#data.show(5)

data.write.mode("overwrite").parquet("output")

df_home = data.select("HomeTeam", "FTHG", "FTR")
df_away = data.select("AwayTeam", "FTAG", "FTR")

df_all = df_home.join(df_away, on="FTR", how="inner")

df_all.show(25)