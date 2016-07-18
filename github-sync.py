import git as git

GITHUB_API = "https://api.github.com"
GITHUB_USERNAME = "adrianschrader"
GITHUB_REPOSITORY = "github-sync"
DIR_REPO = "."


def get_url_repo():
    return "/".join([
        GITHUB_API,
        "repos",
        GITHUB_USERNAME,
        GITHUB_REPOSITORY])

repo = git.cmd.Git(DIR_REPO)
repo.pull()
