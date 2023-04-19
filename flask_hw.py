from flask import Flask,jsonify, request

app = Flask(__name__)

data = [
    {
        'Contact':'9987644456',
        'Name':'Raju',
        'done':'false',
        'id':1
    },
    {
        'Contact':'9876543222',
        'Name':'Rahul',
        'done':'false',
        'id':2
    }
]

@app.route("/")
def hello():
    return "Hello!"

@app.route("/add-data", methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': data[-1]['id'] + 1,
        'title': request.json['Name'],
        'description': request.json.get('Contact', ""),
        'done': False
    }
    data.append(contact)
    return jsonify({
        "status":"success",
        "message": "contact added succesfully!"
    })
    

@app.route("/get-data")
def get_contact():
    return jsonify({
        "data" : data
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)