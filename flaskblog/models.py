from flaskblog import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask import current_app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#create a User model (represents a user entity) which maps to a database table
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # primary key: it is a unique id for a user
    username = db.Column(db.String(20), unique=True, nullable=False)    #nullable: can't be null
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default= "default.jpeg")
    password = db.Column(db.String(60), nullable=False)

    #generates a reset token
    def get_reset_token(self, expires_sec=1800):
        s= Serializer(current_app.config["SECRET_KEY"])    #takes the secret key and expiration time
        return s.dumps({"user_id": self.id}).encode("utf-8")    #uses the secret key to encode the payload given in the dictionary

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            user_id = s.loads(token, max_age=1800)["user_id"]     #returns payload information
        except:
            return None
        return User.query.get(user_id)

    #creates a relationship with Post 
    post = db.relationship('Post', backref="author", lazy=True)     #backref: similar to adding another column to the Post model (referencing Post class)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"


#create a Post model which maps to a database table
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    content = db.Column(db.Text, nullable= False)   #Foreignkey: it has a relationship to the user model (we are referencing the table name so user is lowercase)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"