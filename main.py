#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   Arthals
# @File    :   main.py
# @Time    :   2024/08/10 03:06:58
# @Contact :   zhuozhiyongde@126.com
# @Software:   Visual Studio Code

import os
from datetime import datetime

from session import GitHubIssueNotifier, BarkNotifier, Session


def start():
    print(f"{'[Start]':<15}: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    username = os.getenv("username", "")
    password = os.getenv("password", "")
    api_token = os.getenv("api-token", "")
    bark = os.getenv("bark", "")

    owner = os.getenv("owner", "")
    repo = os.getenv("repo", "")

    if not username or not password:
        raise ValueError("username, password are required")

    if not bark:
        if not owner or not repo:
            notifier = None
        else:
            notifier = GitHubIssueNotifier(owner, repo, api_token)
    else:
        notifier = BarkNotifier(bark)

    
    quit()
    data = {
        "username": username,
        "password": password,
    }

    s = Session(config=data, notifier=notifier)
    s.login()
    s.get_grade()
    s.check_update()

    print(f"{'[End]':<15}: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    start()
