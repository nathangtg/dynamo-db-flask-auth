from flask import request, jsonify
from ..models.user import User 
from ..database.Database import Database

class UserController:
    def __init__(self):
        self.db = Database()
        self.table = self.db.connect().Table("practice")

    def create_user(self, data):
        user = User(
            pk=f"USER#{data['email']}",
            sk="PROFILE",
            username=data["username"],
            email=data["email"],
            password=data["password"]
        )
        self.table.put_item(Item=user.to_dict())
        return user.to_dict()

    def get_user(self, user_email):
        response = self.table.get_item(Key={"pk": f"USER#{user_email}", "sk": "PROFILE"})
        return response["Item"] if "Item" in response else None
