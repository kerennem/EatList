from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def index():
    return "Hellow Flask "

@app.route("/")
def home:
    return render_;
if __name__ == '__main__':
    app.run(debug=True)