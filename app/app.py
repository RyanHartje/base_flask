from flask import Flask
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

@app.route('/')
def index():
  return "Hello World"

if __name__ == "__main__":
  app.run(debug=True,port=5000,host="0.0.0.0")
