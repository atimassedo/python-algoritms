from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world"

@app.route("/data/<username>/<int:years>")
def data(username,years):
    return {"name": username , "years":years}
    




if __name__ == '__main__':
    app.run(debug=True)










