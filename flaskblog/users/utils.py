import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)   #create a random 8 byte hex value
    f_name, f_ext = os.path.splitext(form_picture.filename)     #split the filename recieved from the user into the filename and its extension
    picture_fn = random_hex + f_ext     #set the filename of the pictrure uploaded by the user to a custom value so it doesn't match any other currently in the directory
    picture_path = os.path.join(current_app.root_path, "static/profile_pics", picture_fn)

    output_size = (125,125)

    form_picture.save(picture_path)
    i = Image.open(form_picture)
    i.thumbnail(output_size)    #resize image
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message("Passoword Reset Request", sender="noreply@app.com", recipients = [user.email])
    msg.body = f"""To reset you passoword, visit the following link:

{url_for("reset_token", token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will occur.

        """
    try:
        mail.send(msg)
        print("Email is sent")
    except Exception as e:
        print(e)
        print("Email was not sent")