from flask import jsonify,request
from models.Users import User
from application import loggerInstance

_logger = loggerInstance("users")

def check_if_exist(email,name):
    u1 = User.query.filter_by(name = name).first()
    if u1:
        return True
    u2 = User.query.filter_by(email = email).first()
    if u2:
        return True
    return False

def home():
    _logger.info("HOME")
    return jsonify({"message":"test","data":[12,32,4]})

def get(user_id:int):
    user = User.query.filter_by(id=user_id).first()
    _logger.info(f"User found : {user.serialize()}")
    if user:
        return jsonify({"user_data":user.serialize()})
    return jsonify({"user_data":"Not found!"})

def get_all():
    all_users = User.query.all()
    list_users = [user.serialize() for user in all_users]
    return jsonify({"users":list_users})

def add_user():
    print(x)
    name = request.args.get('name')
    email = request.args.get('email')
    password = request.args.get('password')
    if not check_if_exist(email,name):
        user = User()
        user.name = name
        user.email = email
        user.password = password
        user.save()
        return jsonify({"user":user.serialize(),"status":"ok"})
    return jsonify({"data_req":f"Email : {request.args.get('email')} / Name : {request.args.get('name')} / Password : {request.args.get('password')}"})

