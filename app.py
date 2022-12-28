from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/services')
def services_page():
    return render_template('services.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()
