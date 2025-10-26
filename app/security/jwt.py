from datetime import datetime, timedelta
from jose import jwt

def create_access_token(data: dict, secret: str, minutes: int, algorithm: str="HS256"):
    to_encode = data.copy()
    to_encode["exp"] = datetime.utcnow() + timedelta(minutes=minutes)
    return jwt.encode(to_encode, secret, algorithm=algorithm)
