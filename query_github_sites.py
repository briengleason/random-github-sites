import requests
import random
import os

def find_random_page():

    token = os.environ.get('API_GITHUB_TOKEN')
    
    
    ownerList = ['apache', 'microsoft', 'google', 'facebook', 'alibaba', 'vuejs', 'tensorflow', 'freecodecamp', 'tencent', 'github']
    owner = random.choice(ownerList)

    query_url = f"https://api.github.com/orgs/{owner}/repos"

    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    repo = random.choice(requests.get(query_url, headers=headers, verify=False).json()).get('name')

    contributors_url = f"https://api.github.com/repos/{owner}/{repo}/contributors"

    contributor = random.choice(requests.get(contributors_url, headers=headers, verify=False).json()).get('login')

    pages_url = f"https://api.github.com/repos/{contributor}/{contributor}.github.io"

    pages = requests.get(pages_url, headers=headers, verify=False).json()

    if pages.get('message') == 'Not Found':
        return find_random_page()
    else:
        return f"https://{pages.get('name')}"
