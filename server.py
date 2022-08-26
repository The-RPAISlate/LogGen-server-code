from turtle import width
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, supports_credentials=True)

def displayData(data):
    with open("logData.csv", "a") as file:
        logRow = "\n"+str(data["id"])
        file.write(logRow)

@app.route("/")
def home():
    return "Home route"

@app.route("/log", methods=["POST"])
@cross_origin(supports_credentials=True)
def generateLog():
    if request.method == "POST":
        data = request.get_json()
        if data["id"] == "000000":
            return jsonify({"status": 404})
        
        displayData(data)
        
        return jsonify({
            "status": 200
        })

if __name__ == "__main__":
    app.run()