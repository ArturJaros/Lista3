from flask import Flask, make_response
import requests

BASE_URL = "https://swapi.dev/api/"
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "hello world"

@app.route("/test/<string:ppl_id>")
def test(ppl_id):
    resp = requests.get(f"{BASE_URL}people/{ppl_id}/")
    if resp.status_code == 200:
        return resp.json()
    else:
        return "failed", 500

if __name__ == "__main__":
    app.run()
