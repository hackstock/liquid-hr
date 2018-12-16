from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app import login_manager

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=True)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(BaseModel):
    __tablename__ = "users"
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    is_enabled = db.Column(db.Boolean, nullable=True, default=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    last_login_at = db.Column(db.DateTime, nullable=True)
    profile = db.relationship('Profile', backref='user', uselist=False)

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

class Profile(BaseModel):
    __tablename__ = "profiles"
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(255), nullable = False)
    gender = db.Column(db.String(255), nullable = False)
    date_of_birth = db.Column(db.String(255), nullable = True)
    phone_number = db.Column(db.String(255), nullable = False)
    private_email = db.Column(db.String(255), nullable = False)
    house_address = db.Column(db.String(255), nullable = True)
    postal_code = db.Column(db.String(255), nullable = True)
    town = db.Column(db.String(255), nullable = True)
    nationality = db.Column(db.String(255), nullable = False)

class Employee(BaseModel):
    __tablename__ = "employees"
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))
    supervisor_id = db.Column(db.Integer, nullable=True)
    bank_account_number = db.Column(db.String(255), nullable=False, unique=True)
    bank_account_name = db.Column(db.String(255), nullable=False)
    bank_account_branch = db.Column(db.String(255), nullable=False)
    social_insurance_number = db.Column(db.String(255), nullable = False)
    annual_leave_days = db.Column(db.Integer, nullable=True)
    religion = db.Column(db.String(255), nullable = False)
    date_of_employment= db.Column(db.String(255), nullable = False)
    emergency_contact_name = db.Column(db.String(255), nullable = False)
    emergency_contact_relationship = db.Column(db.String(255), nullable = False)
    emergency_contact_email = db.Column(db.String(255), nullable = False)
    emergency_contact_phone = db.Column(db.String(255), nullable = False)
    profile = db.relationship('Profile', backref='employee', uselist=False)


    