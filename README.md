# BigMart Sales Prediction

## Problem Statement :
Nowadays, shopping malls and Big Marts keep track of individual item sales data in order to forecast future client demand and adjust inventory management. In a data warehouse, these data stores hold a significant amount of consumer information and particular item details. By mining the data store from the data warehouse, more anomalies and common patterns can be discovered.


## Approach :
The main goal is to build a model to predict the BigMart outlet sales based on different factors available in the dataset.

- **Data Collection :** The dataset was downloaded from the Kaggle.
- **Exploratory Data Analysis :** Plotted different graphs to get more insights about dependent and independent variables/features(Univariate Analysis, Bi-variate Analysis and Multi-variate Analysis).
![alt text](https://github.com/nikhilpatil44/bigmart-sales-prediction/blob/main/images/sales%20by%20item%20type.png)

![alt text](https://github.com/nikhilpatil44/bigmart-sales-prediction/blob/main/images/sales%20by%20location%20%26%20item%20type.png)

![alt text](https://github.com/nikhilpatil44/bigmart-sales-prediction/blob/main/images/sales%20by%20outlet%20type.png)

- **Feature Engineering :** Handled missing values, created new variables/features as per insights. Also numerical features scaled down and Categorical features encoded.
- **Model Building :** In this step, first dataset Splitting is done. After that model is trained on different Machine Learning Algorithms such as:
    1) Linear Regression
    2) Decision Tree Regressor
    3) Random Forest Regressor
    4) Gradient Boosting Regressor
    5) Adaboost Regressor
    6) XGBoost Regressor
    7) Support Vector Machine
    Evaluation is done on basis of RMSE score and R-squared.

- **Model Selection :** After performing some tunning the best model is selected.
- **Pickle File :** The best accuaracy model was then saved using Pickle.
- **Webpage :** Using Frontend tools created a webform that takes all the necessary inputs from the uset to predict the output.
- **Deployment :** I have deployed project on the Heroku Platform.


## Deployment Link :
https://bigmart-sale-prediction.herokuapp.com/   deployed to Heroku


## Web Inerface :
![alt text](https://github.com/nikhilpatil44/bigmart-sales-prediction/blob/main/images/web%20interface-1.png)


![alt text](https://github.com/nikhilpatil44/bigmart-sales-prediction/blob/main/images/web%20interface-2.png)


## Libraries used :
    1) Pandas
    2) Numpy
    3) Matplotlib, Seaborn, Plotly
    4) Scikit-Learn
    5) Flask
    6) HTML
    7) CSS

## Technical Aspects :
    1) Python 
    2) Front-end : HTML, CSS
    3) Back-end : Flask
    4) Deployment : Heruko

