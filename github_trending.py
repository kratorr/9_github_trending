import requests
from datetime import date, timedelta


def time_delta(days=7):
    date_days_ago = date.today() - timedelta(days)
    return date.isoformat(date_days_ago)


def get_trending_repositories(date):
    response = requests.get(
        r"https://api.github.com/search/"
        r"repositories?q=created:>{date}&sort=stars&order=desc".format(
            date=date
        )
    )
    return response.json()


if __name__ == "__main__":
    count_repositories = 20
    trending_repositories_dict = get_trending_repositories(time_delta(days=7))
    trending_repositories_list = trending_repositories_dict["items"]
    for number, repo  in enumerate(trending_repositories_list):
        if number == count_repositories:
            break
        stargazers_count = repo["stargazers_count"]
        open_issues_count = repo["open_issues_count"]
        repo_url = repo["html_url"]
        print(
            "Stars:", stargazers_count,
            "Open issues:", open_issues_count,
            "URL:", repo_url
        )