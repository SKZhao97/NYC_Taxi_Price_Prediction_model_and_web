// Databricks notebook source
// Q2 [25 pts]: Analyzing a Large Graph with Spark/Scala on Databricks

// STARTER CODE - DO NOT EDIT THIS CELL
import org.apache.spark.sql.functions.desc
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import spark.implicits._

// COMMAND ----------

// STARTER CODE - DO NOT EDIT THIS CELL
// Definfing the data schema
val customSchema = StructType(Array(StructField("VendorID", IntegerType, true), StructField("tpep_pickup_datetime", TimestampType, true), StructField("tpep_pickup_datetime", TimestampType, true),StructField("passenger_count", IntegerType, true),StructField("trip_distance", FloatType, true),StructField("RatecodeID", IntegerType, true),StructField("store_and_fwd_flag", StringType, true),StructField("PULocationID", IntegerType, true),StructField("DoLocationID", IntegerType, true),StructField("payment_type", IntegerType, true),StructField("fare_amount", FloatType, true),StructField("extra", FloatType, true),StructField("mta_tax", FloatType, true),StructField("tip_amount", FloatType, true),StructField("tolls_amount", FloatType, true),StructField("improvement_surcharge", FloatType, true),StructField("total_amount", FloatType, true)))

// COMMAND ----------

// STARTER CODE - YOU CAN LOAD ANY FILE WITH A SIMILAR SYNTAX.
// MAKE SURE THAT YOU REPLACE THE examplegraph.csv WITH THE mathoverflow.csv FILE BEFORE SUBMISSION.
val df = spark.read
   .format("com.databricks.spark.csv")
   .option("header", "true") // Use first line of all files as header
   .option("nullValue", "null")
   //.schema(customSchema)
   .load("/FileStore/tables/yellow_tripdata_2018_01-0b2e8.csv")
   //.withColumn("date", from_unixtime($"timestamp"))
   //.drop($"timestamp")

// COMMAND ----------

//display(df)
df.show()

// COMMAND ----------

// drop unnecessary columns
val dfDropped = df.drop("VendorID").drop("passenger_count").drop("store_and_fwd_flag").drop("payment_type").drop("tip_amount")
dfDropped.show()

// COMMAND ----------

// Delete the lines with RatecodeID = 5;

var df_deleteRatecodeID=dfDropped.filter("RatecodeID!=5")
df_deleteRatecodeID.show()

// COMMAND ----------

// Delete lines with fare_amount or total_amount <= 0;

var df_deleteBadFareTotal=df_deleteRatecodeID
    .filter("fare_amount > 0")
    .filter("total_amount > 0")
df_deleteBadFareTotal.show()

// COMMAND ----------

// Delete mta_tax != 0.5 and improvement_surcharge != 0.3;

var df_deleteBadMtaImprove=df_deleteBadFareTotal
    .filter("mta_tax = 0.5")
    .filter("improvement_surcharge = 0.3")
df_deleteBadMtaImprove.show()


// COMMAND ----------

// drop mta_tax and improvement_surcharge
val df_dropMtaImprove = df_deleteBadMtaImprove.drop("mta_tax").drop("improvement_surcharge")
df_dropMtaImprove.show()

// COMMAND ----------

// get trip duration as 'seconds'
//ref: https://jaceklaskowski.gitbooks.io/mastering-spark-sql/spark-sql-functions-datetime.html#unix_timestamp
// val df_addDuration = df_dropMtaImprove.selectExpr("(unix_timestamp(tpep_dropoff_datetime) - unix_timestamp(tpep_pickup_datetime))");
// df_addDuration.show()
val df_addDuration = df_dropMtaImprove.withColumn("trip_duration", unix_timestamp(col("tpep_dropoff_datetime")) - unix_timestamp(col("tpep_pickup_datetime")))
df_addDuration.show()

// COMMAND ----------

//Store
//download: https://towardsdatascience.com/databricks-how-to-save-files-in-csv-on-your-local-computer-3d0c70e6a9ab

var df_refined = df_addDuration.select("tpep_pickup_datetime", "tpep_dropoff_datetime", "trip_duration", "trip_distance", "RatecodeID", "PULocationID", "DOLocationID", "fare_amount", "extra", "tolls_amount", "total_amount");
df_refined.show();
//df_refined.write.saveAsTable("refined");
df_refined.coalesce(1).write.format("com.databricks.spark.csv").option("header", "true").save("dbfs:/FileStore/df/refined_012018");
