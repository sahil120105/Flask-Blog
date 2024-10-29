from flaskblog import create_app, db
from flaskblog.models import User

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        users = User.query.all()

        for user in users:
            print(user)

        """ to delete entire database
        
        for user in users:
            db.session.delete(user)
            db.session.commit()
        """

        if not users:
            print("database empty")    
            
    app.run(debug=True)
