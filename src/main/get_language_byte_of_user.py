
import json

import os
import sys
sys.path.append(os.getcwd())
from src.utils.git_api import GitApi
language_statistics= {}


def update_language_statistic(language_repo_statistics):
    for language in language_repo_statistics:
        if language not in language_statistics.keys():
            language_statistics[language]=language_repo_statistics[language]
        else:
            language_statistics[language] += language_repo_statistics[language]


if __name__ == '__main__':
    git_api = GitApi()
    username=input("Enter username: ")
    repo_info = json.loads(git_api.get_repo_info_of_user(username).content)
    for repo in repo_info:
        language_url=repo["languages_url"]
        language_repo_statistics=json.loads(git_api.get_response(language_url).content)
        update_language_statistic(language_repo_statistics)
    print(language_statistics)
