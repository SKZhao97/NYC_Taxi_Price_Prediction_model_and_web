To run the data cleaning and processing:
1. Create a Community Edition account on Databricks. https://community.cloud.databricks.com/
2. Create a cluster.
3. Download the Yello Txi Trip Records data (csv) of the year 2018 from: https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
4. Import data files into the databricks as 'Data' and copy the path of the file.
   Path example: ‘/FileStore/tables/XXX.csv’
5. Import the Scala notebook file 'NYC_taxi(1).scala' into the workspace.
6. Attach the cluster to the imported scala notebook.
7. Line 25 in the scala notebook: paste the path of the file you uploaded as data in step 4.
8. Line 89 in the scala notebook: specify the path you want to save the result csv. For example, 'dbfs:/FileStore/df/refined_012018'
9. run the Scala
10. Download the result csv file:
   reference: https://towardsdatascience.com/databricks-how-to-save-files-in-csv-on-your-local-computer-3d0c70e6a9ab
   a. copy the url of the page you just run the scala at and paste it into a new tab
   b. insert the file path you want to download between the '.com' and '?o=XXXXX' into the url
   c. press 'enter' to download the file
   To get the file path:
   a. go to the folder you saved the result data, for example: Data --> DBFS --> df -->refined_012018 --> part_00000XXXXXX
   b. copy the file path of the 'part_00000xxxxx' file starting from 'df'. For example:
       'df/refined_012018.csv/part_00000XXXXXX.csv'
   c. add '/files/' before the file path.
      For example:'/files/df/refined_012018.csv/part_00000XXXXXX.csv'
