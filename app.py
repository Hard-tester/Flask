from flask import Flask, render_template,url_for,redirect,request
from pymongo import MongoClient
from bson.objectid import ObjectId


app= Flask(__name__)

database_connection = MongoClient("mongodb+srv://Amar:75drBjindQ6Qp3kh@amarbiradar.r4vczg4.mongodb.net/")
database = database_connection.Flask_database # mongo database

Flask_table= database.Flask_table # Flask  database table or collection 

@app.route("/",methods = ['GET','POST'])

def index():
    
    if request.method=="POST":
        content = request.form['content']
        degree = request.form['degree']
        
        Flask_table.insert_one({'content':content,"degree":degree})
        
        return redirect(url_for('index'))
    
    all_todos=Flask_table.find()
    return render_template('index.html',Flask_table=all_todos)

@app.post("/<id>/delete")
def delete(id):
    Flask_table.delete_one({"_id" : ObjectId(id)})
    return redirect(url_for('index'))
        









if(__name__=='__main__'):
    app.run(debug=True,host='0.0.0.0')



