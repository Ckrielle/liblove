from alive_progress import alive_bar
from bs4 import BeautifulSoup
import pkg_resources
import requests


RED = '\033[31m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
END = '\033[0m'


token = "ADD TOKEN HERE"
installed_packages = pkg_resources.working_set
installed_packages_list = sorted([f"{i.key}" for i in installed_packages])
length = len(installed_packages_list)

with alive_bar(length, enrich_print=False) as bar:
    for package in installed_packages_list:
        url = "https://pypi.org/project/" + package
        r = requests.get(url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html.parser')
            divs = soup.find_all("div", {"class": "github-repo-info"})
            repos = [repo['data-url'] for repo in divs]
            if repos != []:
                repo = repos[0][29:]
                headers = {
                    'Authorization': f'token {token}',
                    'Accept': 'application/vnd.github.v3+json'
                }
                star = "https://api.github.com/user/starred/" + repo
                put_r = requests.put(star, headers=headers)
                status = put_r.status_code
                if status == 204:
                    print("{1}Gave a {4}{2}★ STAR {4}{1}to {4}{2}{0}{4}{3} <3{4}".format(package, BLUE, YELLOW, RED, END))
                elif status == 401:
                    print(f"{RED}UNAUTHORIZED ACCESS CHECK YOUR TOKEN{END}")
            else:
                print("{2}{0}{4}{1} doesn't have a repo {4}{3}:({4}".format(package, BLUE, YELLOW, RED, END))
        else:
            print("{1}Couldn't find {4}{2}{0}{4} {3}:({4}".format(package, BLUE, YELLOW, RED, END))
        bar()
