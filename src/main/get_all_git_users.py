import json
import os
import sys
from http import HTTPStatus
from pprint import pprint

sys.path.append(os.getcwd())
from src.utils.git_api import GitApi


def read_from_json(path):
    with open(path, "r") as file:
        return json.load(file)


def write_to_json_file(path, data):
    with open(path, "w+") as file:
        return file.write(json.dumps(data, indent=4))


if __name__ == '__main__':
    keys = ["id", "name", "full_name", "private", "languages_url"]
    git_api = GitApi()
    # Relative Path ve Absolute Path - Sezer
    json_path = "src/Data/user_list.json"
    while True:
        my_json_data = read_from_json(json_path)
        last_link = my_json_data["LAST_LINK"]
        user_response = git_api.get_all_users(last_link)
        # 2XX 3XX 4XX 5XX
        if user_response.status_code != HTTPStatus.OK:
            print("Error. Check the response", user_response.status_code, user_response.content.decode())
            break
        body = json.loads(user_response.content.decode())
        for item in body:
            new_dict = {key: val for key, val in item.items() if key in keys}
            my_json_data.get("USER LIST").append(new_dict)
        my_json_data["LAST_LINK"] = user_response.headers["link"].replace("<", ">").split(">")[1]
        write_to_json_file(json_path, my_json_data)

        print("Current repo size is ", len(my_json_data.get("USER LIST")))
