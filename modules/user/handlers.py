from flask import jsonify
import logging


def home():
    return jsonify({"message":"test","data":[12,32,4]})

def get(user_id:int):
    return jsonify({"user_data":f"User with id : {user_id}"})