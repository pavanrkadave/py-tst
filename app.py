from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    @app.route("/")
    def hello_world():
        return "Hello, World!"

    app.run(host="0.0.0.0", threaded=True)
