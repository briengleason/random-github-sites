from flask import Flask, request, make_response
from flask_cors import CORS, cross_origin
from query_github_sites import find_random_page
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import os
import logging


application = Flask(__name__)

cors = CORS(application)

auth = HTTPBasicAuth()
users = {
    os.environ.get('API_USERNAME'): generate_password_hash(os.environ.get('API_PASSWORD'))
}

logging.basicConfig(level=logging.INFO)


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@application.route('/')
@cross_origin()
def index():
    return 'Index Page'


@application.route('/api/random_site', methods=['GET', 'OPTIONS'])
# @auth.login_required
@cross_origin()
def get_random_site():
    logging.info("inside of get_random_site")
    page = find_random_page()
    logging.info(page)
    return page, 200

if __name__ == '__main__':
    application.run(host="0.0.0.0")
