from flask import Flask, flash, request, redirect,url_for, render_template, Blueprint
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('index.html')

@main.route('/services')
def services():
    return render_template('services.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/about')
def about():
    return render_template('about.html')

app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)