from flask import Flask, render_template
import sys, os 

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(host='127.0.0.1' , port=8001)
