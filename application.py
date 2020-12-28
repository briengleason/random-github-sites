from flask import Flask
from flask_cors import CORS
from query_github_sites import find_random_page
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import os


application = Flask(__name__)

cors = CORS(application, resources={r"/api/*": {"origins": "*"}})
application.config['CORS_HEADERS'] = 'Content-Type'

auth = HTTPBasicAuth()
users = {
    os.environ.get('API_USERNAME'): generate_password_hash(os.environ.get('API_PASSWORD'))
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@application.route('/')
def index():
    return 'Index Page'

@application.route('/api/random_site', methods=['POST'])
@auth.login_required
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def get_random_site():
    return find_random_page()


if __name__ == '__main__':
    application.run(host="0.0.0.0")
