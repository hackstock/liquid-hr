from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app import login_manager

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=True)


class User(BaseModel):
    __tablename__ = "users"
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    is_enabled = db.Column(db.Boolean, nullable=True, default=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    last_login_at = db.Column(db.DateTime, nullable=True)

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.id

    def is_active(self):
        return self.is_enabled

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    