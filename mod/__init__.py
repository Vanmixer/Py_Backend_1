from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import requests

app = Flask(__name__)
api = Api()

users = [[1, "User"]]
categories = [[1, "Витрати"]]
records = [[1, 1, 1, "20.10.2022", 100],
           [2, 1, 1, "20.10.2022", 100],
           [1, 2, 1, "20.10.2022", 100],
           [1, 7, 1, "20.10.2022", 100]]
@app.post('/user')
def create_user():
    new_one = request.json
    users.append(new_one)
    return users

@app.post('/category')
def create_category():
    new_one = request.json
    categories.append(new_one)
    return categories

@app.post('/record')
def create_record():
    new_one = request.json
    records.append(new_one)
    return records

class Main(Resource):
    def get(self, user_id):
        result = list()
        counter = 0
        for x in range(len(records)):
            if(records[x][0] == user_id):
              counter = + 1
              result.insert(counter, records[x])
        return result


api.add_resource(Main, "/api/record/<int:user_id>")
api.init_app(app)







if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")
