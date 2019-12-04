# New York City taxi price prediction 
## Data_Analysis_and_Visualization_Final_Project

### TITLE: Is Uber really cheaper than Taxi?
    Teammates: S Zhao, H Wang, X Zhang, Y Xiao and Y ke
### Process:

1. **Data**: Download from NYC Taxi & Limousine Commission https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
2. **Data Processing and Refining**: Use Spark on Databricks (coding in Scala) https://community.cloud.databricks.com/login.html
3. **Data Cluster**: k-means(coding in Python), do cluster to time, distance, start position and desination
4. **Model**: Regression machine learning(coding in Python)
5. **Model training**: Microsoft lightGBM framework, regression module
6. **Model test and evaluation**: Cross validation, Morte Carlo Simulation, TP/TN/FP/FN (expected)
7. **Visulization**: Draw bar chart, line chart and heatmap to show the comparation between Uberv and Taxi in NYC based on D3.js and Tableau
8. **Web**: Based on Flask structure, use Google Map APIs to get position information such as latitude, longtitude, trip distance, trip duration; use jQuery to implement the data transfer between frontend and backend; use D3.js to load NYC open data taxi zone json file to transfer coordinate to location id.
9. **Document**: Poster design $ report compile

### Demo(Interactive web)
![image](https://github.com/SKZhao97/NYC_Taxi_Price_Prediction/blob/master/Demo.gif)

### Structure
![Demo](https://github.com/SKZhao97/NYC_Taxi_Price_Prediction/blob/master/Map_web_with_model/web_structure.jpg)
![Prediction](https://github.com/SKZhao97/NYC_Taxi_Price_Prediction/blob/master/Prediction_Workflow.png)

### License
This project is licensed under the MIT License (see the LICENSE file for details).
