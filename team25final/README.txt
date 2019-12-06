README CSE6242 Team25

## DESCRIPTION

To predict and analyze the taxi price of NYC and compare it with Lyft, a prediction model was built and an interactive web application is constructed. The code is consist of the following part:

1. Data processing based on Spark/Scala on Databricks. The dataset can be download from https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page. The data is refined to train the prediction model. The processed data can be found at https://drive.google.com/drive/folders/1uR4-vIgYwsRGPDta_PPfpgzBxAZiAbP2

2. Time parameter generating. After using Scala, we need to generate month, weekday and time zone. If the time format is not right, modify it because if this file was opened in Excel before, its time format may change.

3. Model based on lightGBM. 
data_process.py: deleting not used columns and merge each month data into one csv.
train.py: call this for model training.
predict.py: call this for model prediction test.
utils.py: utility methods
experiment.py: parameter exploration

4. Interactive web application. Based on FLASK framework. The lightGBM regression model is ingrained in the web back end. In the front end, Google map API is called to generate map, marker and get location. Distance matrix API is called to get estimated duration and distance. D3.js is used to transfer the longitude and latitude into NYC taxi zone. jQuery .Ajax is used to send data between two ends. SQLite database is embedded to store search history.

5. Preparing data for experiment. Generate the csv files used to compare, analyze and visualize based on several Python scripts. Then, Tableau is used to create the charts based on the csv files.


## INSTALLATION

$ pip install flask

$ pip install lightgbm

$ pip install pandas
$ pip install numpy
$ pip install sklearn

## EXECUTION

1）To run the regression model

1. for trianing:

$ python3 train.py

2. for experiment:
$ python3 experiment.py

3. for prediction:
$ python3 predict.py

1) To run the web application:

* Change the API_KEY in web_application/map/template/index.html
$ pip install pipenv
$ pipenv install --dev
$ pipenv shell
$ set FLASK_ENV=development (use export instead of set on MacOS)
$ set FLASK_APP=map (use export instead of set on MacOS)
$ flask initdb (optional)
$ flask run

$ Running on(local) http://127.0.0.1:5000/
$ Press CTRL+C to quit


2) To run the data cleaning and processing:

1. Create a Community Edition account on Databricks. https://community.cloud.databricks.com/
2. Create a cluster.
3. Download the Yellow Taxi Trip Records data (.csv) of the year 2018 from: https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
4. Import data files into the Databricks as 'Data' and copy the path of the file.
   Path example: ‘/FileStore/tables/XXX.csv’
5. Import the Scala notebook file 'NYC_taxi(1).scala' into the workspace.
6. Attach the cluster to the imported scala notebook.
7. Line 25 in the Scala notebook: paste the path of the file you uploaded as data in step 4.
8. Line 89 in the Scala notebook: specify the path you want to save the result csv. For example, 'dbfs:/FileStore/df/refined_012018'
9. run the Scala
10. Download the result .csv file:
   reference: https://towardsdatascience.com/databricks-how-to-save-files-in-csv-on-your-local-computer-3d0c70e6a9ab
   a. copy the url of the page you just run the Scala at and paste it into a new tab
   b. insert the file path you want to download between the '.com' and '?o=XXXXX' into the url
   c. press 'enter' to download the file
   To get the file path:
   a. go to the folder you saved the result data, for example: Data --> DBFS --> df -->refined_012018 --> part_00000XXXXXX
   b. copy the file path of the 'part_00000xxxxx' file starting from 'df'. For example:
       'df/refined_012018.csv/part_00000XXXXXX.csv'
   c. add '/files/' before the file path.
      For example:'/files/df/refined_012018.csv/part_00000XXXXXX.csv'

3) To run the data preparing related python code:

1. Get a .csv file which contains Lyft price, whose structure is like the data_demo.csv, 
2. Run get_point.py to generate the longitude and latitude in the .csv, 
3. Run get_tirp_dis&dur.py to get trip_distance and trip_duration from google distance matrix api, 
4. Run rearrange.py to rearrange the data order to fit the format of model.
5. After getting the price from model, run add_price.py to add price to csv file.
6. Projection.csv is need when getting lontitude and latitude point from location id and this csv file is included. 
7. Run rush_hour.py, generating the csv files to compare rush hour and non-rush hour. 
8. Run weekday.py to generate two csv files in weekday experiment. 
9. When generating experiment data, the frequent request may be blocked. In this case, the parameter i in the for loop can be reduced.



