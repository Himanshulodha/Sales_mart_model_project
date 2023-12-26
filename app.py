from flask import Flask,render_template,redirect, url_for, request
from model import  Predict_Sales

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello_world():
    if request.method=='GET':
        return render_template('index.html',data='hi')
    else:
        Item_Weight=request.form["Item_Weight"]
        Item_Fat_Content=request.form["Item_Fat_Content"]
        Item_Visibility=request.form["Item_Visibility"]
        Item_Type=request.form["Item_Type"]
        Item_MRP=request.form["Item_MRP"]
        Outlet_Size=request.form["Outlet_Size"]
        Outlet_Location_Type=request.form["Outlet_Location_Type"]
        Outlet_Type=request.form["Outlet_Type"]
        New_Item_Type=request.form["New_Item_Type"]
        Outlet_Years=request.form["Outlet_Years"]
        Outlet=request.form["Outlet"]   
        # Outlet_Location_Type=request.form["Outlet_Location_Type"]
        val=Predict_Sales([Item_Weight, Item_Fat_Content, Item_Visibility, Item_Type,  Item_MRP, Outlet_Size, Outlet_Location_Type, Outlet_Type, New_Item_Type, Outlet_Years, Outlet])
        return render_template('result.html',data=val)

if __name__=="__main__":
    app.run(host="0.0.0.0")
    