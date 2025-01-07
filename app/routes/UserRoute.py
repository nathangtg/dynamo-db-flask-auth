from flask import request, jsonify, Blueprint
from ..controllers.UserController import UserController
from ..auth.auth_util import require_auth

UserRoute = Blueprint("UserRoute", __name__)

@UserRoute.route("/users", methods=["POST"])
def create_user():
    data = request.json
    if not data:
        return jsonify({"error": "Request body is missing"}), 400
    
    try:
        user = UserController().create_user(data)
        return jsonify(user), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@UserRoute.route("/users/<user_email>", methods=["GET"])
def get_user(user_email):
    user = UserController().get_user(user_email)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify(user), 200

@UserRoute.route("/users/profile", methods=["POST"])
@require_auth
def get_user_profile():
    user = request.user
    return jsonify(user.to_dict()), 200

