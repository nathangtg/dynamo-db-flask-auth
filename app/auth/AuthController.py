from ..database.Database import Database
from ..models.user import User 
from .auth_util import AuthUtil

class AuthController: 
    def __init__(self):
        self.db = Database()
        self.table = self.db.connect().Table("practice")
        
    def register_user(self, data):
        
        # Check the user already exists
        user = self.get_user(data["email"])
        if user:
            return {"message": "User already exists."}
        
        user = User(
            pk=f"USER#{data['email']}",
            sk="PROFILE",
            username=data["username"],
            email=data["email"],
            password=data["password"]
        )
        
        self.table.put_item(Item=user.to_dict())
        return user.to_dict()
    
    def login_user(self, data):
        
        required_fields = ["email", "password"]
        missing_fields = [field for field in required_fields if field not in data]
        
        if missing_fields:
            raise ValueError(f"Missing fields: {', '.join(missing_fields)}")
        
        user_data = self.get_user(data["email"])

        if not user_data:
            raise ValueError("User not found")

        user = User.from_dict(user_data)

        if not user.verify_password(data["password"]):
            raise ValueError("Incorrect password")

        return {
            **{key: value for key, value in user.to_dict().items() if key != "password"},
            "token": AuthUtil.generate_token(user)
        }

    def get_user(self, user_email):
        response = self.table.get_item(Key={"pk": f"USER#{user_email}", "sk": "PROFILE"})
        
        if "Item" not in response: 
            return None
        
        return response["Item"] if "Item" in response else None