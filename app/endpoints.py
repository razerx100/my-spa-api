from app import api
from flask import make_response, jsonify

@api.route("/")
def home():
    return {"Api": "Works"}