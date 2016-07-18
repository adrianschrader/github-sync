import requests as reqs
import git as git

GITHUB_API = "https://api.github.com"
GITHUB_USERNAME = "adrianschrader"
GITHUB_REPOSITORY = "pontoon"
DIR_REPO = "."


def get_url_repo():
    return "/".join([
        GITHUB_API,
        "repos",
        GITHUB_USERNAME,
        GITHUB_REPOSITORY])

repo = git.cmd.Git(DIR_REPO)
repo.pull()

request = reqs.get(get_url_repo() + "/events")
print(request.json())
