import requests
from datetime import date, timedelta


def get_time_delta(days=7):
    date_days_ago = date.today() - timedelta(days)
    return date.isoformat(date_days_ago)


def get_trending_repositories(from_date):
    params = dict(
        sort="stars", order="desc", q="created:>{date}".format(date=from_date)
    )
    trending_repositories = requests.get(
        "https://api.github.com/search/repositories", params=params
    )
    return trending_repositories.json()


def get_open_issues_amount(repo_owner, repo_name):
    url = "https://api.github.com/repos/{owner}/{repo}/issues".format(
        owner=repo_owner, repo=repo_name
    )
    list_of_issues = requests.get(url)
    return len(list_of_issues.json())


if __name__ == "__main__":
    count_repositories = 20
    trending_repo = get_trending_repositories(get_time_delta(days=7))["items"]
    for repo in trending_repo[:count_repositories]:
        stargazers_count = repo["stargazers_count"]
        repo_owner = repo["owner"]["login"]
        repo_name = repo["name"]
        repo_url = repo["html_url"]
        open_issues_count = get_open_issues_amount(repo_owner, repo_name)
        print(
            "Stars:", stargazers_count,
            "Open issues:", open_issues_count,
            "URL:", repo_url,
        )

