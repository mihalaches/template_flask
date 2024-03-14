from flask import jsonify
from models.Users import User

import logging

_logger = logging.getLogger(__name__)

def home():
    _logger.info("HOME")
    return jsonify({"message":"test","data":[12,32,4]})

def get(user_id:int):
    user = User.query.filter_by(id=user_id).first()
    if user:
        return jsonify({"user_data":user.serialize()})
    return jsonify({"user_data":"Not found!"})

def get_all():
    all_users = User.query.all()
    list_users = [user.serialize() for user in all_users]
    return jsonify({"users":list_users})