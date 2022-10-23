from flask import Flask
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api()

users = [[1, "User"]]
categories = [[1, "Витрати"]]
records = [[1, 1, 1, "20.10.2022", 100],
           [2, 1, 1, "20.10.2022", 100],
           [1, 2, 1, "20.10.2022", 100],
           [1, 7, 1, "20.10.2022", 100]]

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
