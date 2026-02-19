#!/usr/bin/python3
"""
Module to interact with JSONPlaceholder API using requests.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch posts from JSONPlaceholder and print their titles.
    Also print the status code of the response.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """
    Fetch posts from JSONPlaceholder and save them to posts.csv.
    Each row contains id, title, and body.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Structure data into list of dictionaries
        data = [{"id": post["id"], "title": post["title"], "body": post["body"]}
                for post in posts]

        # Write to CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(data)
