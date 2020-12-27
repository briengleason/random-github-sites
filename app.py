from flask import Flask
from query_github_sites import find_random_page

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/api/random_site', methods=['POST'])
def get_random_site():
    return find_random_page()


if __name__ == '__main__':
    app.run()
