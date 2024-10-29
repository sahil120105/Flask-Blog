class Config:
    SECRET_KEY = "238ejwfjr394w0raf80q409rjirwf03"  # protect against cross-site request forgery (CSRF) attacks
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    SQLALCHEMY_DATABASE_URI = "sqlite:///user.sqlite3"   #Sets the SQLALCHEMY_DATABASE_URI configuration variable to a SQLite database file named site.db
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True 
    MAIL_USERNAME = "your_email"
    MAIL_PASSWORD = "your_app_password"