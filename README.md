
# Al Mayadeen Articles API

This project is a Flask-based REST API that interacts with a MongoDB database to retrieve and analyze articles. The API provides various endpoints to query articles based on keywords, authors, publication dates, word counts, and other parameters. The data is stored in a MongoDB collection called `articles` within the `Al_Mayadeen` database.

## Features

- **Top Keywords**: Retrieve the top 10 most frequent keywords.
- **Top Authors**: Get the top 10 authors with the most articles.
- **Articles by Date**: Get the count of articles grouped by their publication date.
- **Articles by Word Count**: Retrieve the distribution of articles based on word count.
- **Articles by Language**: Get the count of articles grouped by their language.
- **Articles by Classes**: Retrieve the count of articles grouped by their classes.
- **Articles by Keyword**: Search articles based on a specific keyword.
- **Articles by Author**: Search articles written by a specific author.
- **Top Classes**: Retrieve the top 10 most frequent classes.
- **Article Details**: Get detailed information about a specific article by `postid`.
- **Articles with Video**: Get articles that include video content.
- **Articles by Year**: Retrieve the count of articles published in a specific year.
- **Longest and Shortest Articles**: Get the top 10 longest and shortest articles by word count.
- **Articles by Keyword Count**: Retrieve articles grouped by the number of keywords.
- **Articles with Thumbnail**: Get articles that include a thumbnail image.
- **Articles Updated After Publication**: Get articles that were updated after their initial publication.
- **Articles by Coverage**: Retrieve articles grouped by a specific coverage class.
- **Popular Keywords in Last X Days**: Get the top keywords used in the last X days.
- **Articles by Month**: Get the count of articles published in a specific month and year.
- **Articles by Word Count Range**: Retrieve articles that fall within a specific word count range.
- **Articles with Specific Keyword Count**: Get articles that have an exact number of keywords.
- **Articles by Specific Date**: Retrieve articles published on a specific date.
- **Articles Containing Specific Text**: Search for articles that contain a specific text string.
- **Articles with More than X Words**: Get articles that have more than a specified number of words.
- **Articles Grouped by Coverage**: Retrieve the count of articles grouped by coverage class.
- **Articles from the Last X Hours**: Get articles published within the last X hours.
- **Articles by Title Length**: Retrieve articles grouped by the length of their titles.
- **Most Updated Articles**: Get the top 10 articles that have been updated the most times.

## Prerequisites

- Python 3.x
- Flask
- PyMongo
- MongoDB running on `localhost` with the default port `27017`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/al-mayadeen-api.git
   cd al-mayadeen-api
   ```

2. Install the required Python packages:

   ```bash
   pip install Flask pymongo
   ```

3. Ensure MongoDB is running and accessible at `mongodb://localhost:27017/`.

4. Start the Flask application:

   ```bash
   python app.py
   ```

5. The API will be available at `http://127.0.0.1:5000/`.

## Usage

You can interact with the API using tools like `curl`, Postman, or directly from your web browser.

### Example Endpoints

- **Get the top 10 keywords**: 
  - `GET /top_keywords`

- **Get articles by a specific author**: 
  - `GET /articles_by_author/<author_name>`

- **Get articles published in 2024**:
  - `GET /articles_by_year/2024`

- **Search articles containing the word "Flask"**:
  - `GET /articles_containing_text/Flask`

Refer to the [Features](#features) section for a full list of available endpoints.

## License

This project is licensed under the MIT License - By Hanin Kassir
