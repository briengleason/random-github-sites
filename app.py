from flask import Flask
from query_github_sites import find_random_page

app = Flask(__name__)


@app.route('/api/random_site')
def get_random_site():
    return find_random_page()


if __name__ == '__main__':
    app.run()
