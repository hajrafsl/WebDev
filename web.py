from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
   return "<!doctype html><head><meta charset=utf-8><title>Hello World</title></head><body><p>Hello World</p></body>"



if __name__ == '__main__':
    app.run(debug=True)