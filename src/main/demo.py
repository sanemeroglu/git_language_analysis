string='<https://api.github.com/users?page=1&per_page=100&since=135>; rel="next", <https://api.github.com/users{?since}>; rel="first"'
print(string.replace("<",">").split(">")[1])