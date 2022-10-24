import os
from logging import getLogger
from logging import basicConfig

from dotenv import load_dotenv
from github import Github
from github import GithubException

GITHUB_ACCESS_TOKEN_KEY: str = "GITHUB_ACCESS_TOKEN"
logger = getLogger("main")


def main() -> None:
    load_dotenv()
    configure_logging()
    github = load_github()


def configure_logging() -> None:
    basicConfig(level=os.environ.get("LOG_LEVEL", "INFO"))


def load_github() -> Github | None:
    access_token = os.environ.get(GITHUB_ACCESS_TOKEN_KEY)
    if access_token is None:
        logger.warning("GITHUB_ACCESS_TOKEN_KEY is not set")

    github = Github(access_token)

    try:
        user = github.get_user().login
    except GithubException as err:
        logger.error(f"Getting user failed: {err}")
        return None

    logger.info(f"Logged in as {user}")
    return github


if __name__ == '__main__':
    main()
