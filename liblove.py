from bs4 import BeautifulSoup
import pkg_resources
import requests

token = 'ADD YOURS HERE'
installed_packages = pkg_resources.working_set
installed_packages_list = sorted([f"{i.key}" for i in installed_packages])


for package in installed_packages_list:
    url = "https://pypi.org/project/" + package
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        mydivs = soup.find_all("div", {"class": "github-repo-info"})
        repos = [repo['data-url'] for repo in mydivs]
        if len(repos):
            repo = repos[0][29:]
            headers = {
                'Authorization': f'token {token}',
                'Accept': 'application/vnd.github.v3+json'
            }
            star = "https://api.github.com/user/starred/" + repo
            put_r = requests.put(star, headers=headers)
