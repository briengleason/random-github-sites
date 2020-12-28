from flask import Flask
from query_github_sites import find_random_page

application = Flask(__name__)

@application.route('/')
def index():
    return 'Index Page'

@application.route('/api/random_site', methods=['POST'])
def get_random_site():
    return find_random_page()


if __name__ == '__main__':
    application.run(host="0.0.0.0")
