from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)

file = open("./random_forest_regression_model.pkl", 'rb')
model = pickle.load(file)

data = pd.read_csv('./cleaned_data.csv')

@app.route('/')
def home():
    Item_Fat_Content = sorted(data['Item_Fat_Content'].unique())
    Item_Type = sorted(data['Item_Type'].unique())
    Outlet_Size = sorted(data['Outlet_Size'].unique())
    Outlet_Location_Type = data['Outlet_Location_Type'].unique()
    Outlet_Type = sorted(data['Outlet_Type'].unique())
    #Outlet_Year = sorted(data['Outlet_Year'].unique())
    return render_template("index.html", Item_Fat_Content= Item_Fat_Content, Item_Type= Item_Type, Outlet_Size=Outlet_Size,
    Outlet_Location_Type= Outlet_Location_Type, Outlet_Type=Outlet_Type)

@app.route('/predict', methods=['POST'])
def predict():
    Item_Weight = float(request.form.get('Item_Weight')) 
    Item_Fat_Content = request.form.get('Item_Fat_Content')
    Item_Visibility = request.form.get('Item_Visibility')
    Item_Type = request.form.get('Item_Type')
    Item_MRP = request.form.get('Item_MRP')
    Outlet_Size = request.form.get('Outlet_Size')
    Outlet_Location_Type = request.form.get('Outlet_Location_Type')
    Outlet_Type = request.form.get('Outlet_Type')
    Outlet_Establishment_Year = request.form.get('Outlet_Establishment_Year') 
  
    prediction = model.predict(pd.DataFrame([[Item_Weight, Item_Fat_Content, Item_Visibility, Item_Type,
    Item_MRP, Outlet_Size, Outlet_Location_Type, Outlet_Type, Outlet_Establishment_Year]], columns=['Item_Weight', 
    'Item_Fat_Content', 'Item_Visibility', 'Item_Type',
    'Item_MRP', 'Outlet_Size', 'Outlet_Location_Type', 'Outlet_Type', 'Outlet_Establishment_Year']))

    return str(prediction[0])


if __name__ == '__main__':
    app.run(debug=True)    