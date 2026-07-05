# News App Using API

This is a simple Python project that allows users to search for news articles based on a topic they are interested in.

The program asks the user to enter a news topic, sends a request to the NewsAPI website, receives news data in JSON format, and displays article titles with their URLs.

## Features

- Takes user input for a news topic
- Fetches news articles using NewsAPI
- Displays article titles
- Displays article URLs
- Uses JSON data from an API response
- Beginner-friendly Python API project

## Technologies Used

- Python
- Requests library
- NewsAPI

## How the Code Works

1. The user enters a news topic.
2. The program creates a URL using the topic and API key.
3. The `requests.get()` function sends a request to NewsAPI.
4. The response is converted into JSON format using `.json()`.
5. The program gets the list of articles from the JSON data.
6. Each article title and URL is printed in the terminal.

## Requirements

Before running this project, install the `requests` library:

```bash
pip install requests