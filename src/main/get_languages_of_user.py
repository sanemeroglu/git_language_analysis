
import json
import os
import sys
sys.path.append(os.getcwd())
from src.utils.git_api import GitApi
language_statistics= {}


def update_language_statistic(language):
    if language not in language_statistics.keys():
        language_statistics[language]=1
    else:
        language_statistics[language] += 1

if __name__ == '__main__':
    git_api = GitApi()
    username=input("Enter username: ")
    repo_info = json.loads(git_api.get_repo_info_of_user(username).content)
    for repo in repo_info:
        language=repo["language"]
        update_language_statistic(language)
    print(language_statistics)
