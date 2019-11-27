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
val customSchema = StructType(Array(StructField("VendorID", IntegerType, true), StructField("tpep_pickup_datetime", StringType, true), StructField("tpep_pickup_datetime", StringType, true),StructField("passenger_count", IntegerType, true),StructField("trip_distance", FloatType, true),StructField("RatecodeID", IntegerType, true),StructField("store_and_fwd_flag", StringType, true),StructField("PULocationID", IntegerType, true),StructField("DoLocationID", IntegerType, true),StructField("payment_type", IntegerType, true),StructField("fare_amount", FloatType, true),StructField("extra", FloatType, true),StructField("mta_tax", FloatType, true),StructField("tip_amount", FloatType, true),StructField("tolls_amount", FloatType, true),StructField("improvement_surcharge", FloatType, true),StructField("total_amount", FloatType, true)))

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

// Delete the lines with RatecodeID = 5;

var df_deleteRatecodeID=df.filter("RatecodeID!=5")
df_deleteRatecodeID.show()

// COMMAND ----------

// Delete lines with fare_amount or total_amount larger than 0;

var df_deleteBadFareTotal=df_deleteRatecodeID
    .filter("fare_amount>=0")
    .filter("total_amount>=0")
df_deleteBadFareTotal.show()

// COMMAND ----------

// Delete mta_tax != 0.5 and improvement_surcharge != 0.3;

var df_deleteBadMtaImprove=df_deleteBadFareTotal
    .filter("mta_tax = 0.5")
    .filter("improvement_surcharge = 0.3")
df_deleteBadMtaImprove.show()


// COMMAND ----------

//Store

var df_refined = df_deleteBadMtaImprove;
df_refined.show();
df_refined.write.saveAsTable("refined");
