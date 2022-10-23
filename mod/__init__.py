from flask import Flask, request, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api()

users = [[1, "User"]]
categories = [[1, "Витрати"]]
records = [[1, 1, 1, "20.10.2022", 100],
           [2, 1, 1, "20.10.2022", 100],
           [1, 2, 1, "20.10.2022", 100],
           [1, 7, 1, "20.10.2022", 100]]

@app.route("/user", methods=["POST","GET"])
def create_user_post():
    if request.method == "POST":
      id = request.form['id']
      user_name = request.form['user_name']
      users.append([id, user_name])
      return (render_template('user.html'))

@app.route('/category')
def create_category():
    if request.method == "POST":
        id = request.form['id']
        category_name = request.form['category_name']
        categories.append([id, category_name])
        return (render_template('record.html'))

@app.post('/record')
def create_record():
    if request.method == "POST":
        id = request.form['id']
        user_id = request.form['User_id']
        category_id = request.form['category_id']
        record_data = request.form['record_data']
        record_sum = request.form['record_sum']
        return (render_template('record.html'))

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
