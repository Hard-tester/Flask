from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    
            {
        "id": 1,
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com",
        "address": "123 Main St, Cityville"
        },
        {
        "id": 2,
        "name": "Jane Smith",
        "age": 25,
        "email": "jane.smith@example.com",
        "address": "456 Elm St, Townsville"
        },
        {
        "id": 3,
        "name": "Michael Johnson",
        "age": 35,
        "email": "michael.johnson@example.com",
        "address": "789 Oak St, Villageton"
        },
        {
        "id": 4,
        "name": "Emily Brown",
        "age": 28,
        "email": "emily.brown@example.com",
        "address": "101 Pine St, Hamletville"
        },
        {
        "id": 5,
        "name": "Christopher Lee",
        "age": 40,
        "email": "christopher.lee@example.com",
        "address": "202 Maple St, Riverside"
        }
    
]
@app.route("/")
def hello_world():
    return render_template('Index.html', jobs=JOBS , Other_data="Dummy data ")

if __name__ == "__main__":
    app.run(host= '0.0.0.0', debug=True )