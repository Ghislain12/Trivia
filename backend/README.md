# Backend - Trivia API

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createbd trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

### Documentation

## Introduction

This documentation is about all routes and endpoints availables for the trivia api.

`GET '/api/v1.0/categories'`

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, `categories`, that contains an object of `id: category_string` key: value pairs.

```json
{
  "1": "Science",
  "2": "Art",
  "3": "Geography",
  "4": "History",
  "5": "Entertainment",
  "6": "Sports"
}
```

`GET '/api/v1.0/questions'`

- Fetches a dictionary of question in which the keys are the ids and the value is the corresponding string of the question
- Request Arguments: None
- Returns: An object with a single key `questions`, `number of total questions`, `current category`, `categories`.

```json
{
    "question": "2+2",
    "answer": "4",
    "category": "5",
    "difficulty": "4"
}'
```

`DELETE '/api/v1.0/questions/<int:id>'`

- Delete question using a question ID
- Request Arguments: ID
- Returns: An object with a single key `deleted`, `number of total questions`, `questions`.

```json
{
    "success": True,
    "deleted": "1",
      "questions": [{
          "question": "2+2",
          "answer": "4",
          "category": "5",
          "difficulty": "4"
      }],
    "totals_questionss": "10"
}
```

`POST '/api/v1.0/questions'`

- POST a new question, which will require the question and answer text, category, and difficulty score
- Request Arguments: {
                          "question": "2+2",
                          "answer": "4",
                          "category": "5",
                          "difficulty": "4"
                      }
- Returns: An object with a single key `created`, `number of total questions`, `questions`,.

```json
{
    "question": "2",
    "questions": [{
          "question": "2+2",
          "answer": "4",
          "category": "5",
          "difficulty": "4"
      }],
    "totals_questionss": "10"
}'
```

`POST '/api/v1.0/questions/search'`

- get questions based on a search term. It should return any questions for whom the search term is a substring of the question
- Request Arguments: search_term
- Returns: An object with a single key `questions`, `number of total questions`, `current category`,.

```json
{
    "question": [{
          "question": "2+2",
          "answer": "4",
          "category": "5",
          "difficulty": "4"
      }],
    "current_category": None,
    "totals_questions": "10"
}'
```

`GET '/api/v1.0/categories/<int:category_id>/questions'`

- GET questions based on category
- Request Arguments: Category ID
- Returns: An object with a single key `questions`, `number of total questions`, `current category`,.

```json
{
    "question": [{
          "question": "2+2",
          "answer": "4",
          "category": "5",
          "difficulty": "4"
      }],
    "current_category": "2",
    "totals_questions": "10"
}'
```

`GET '/api/v1.0/categories/<int:category_id>/questions'`

- get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
- Request Arguments: ```json
                      {
                          'previous_questions': [1, 4, 20, 15]
                          quiz_category': 'current category'
                      }
                      ```
- Returns: An object with a single key `questions`, `number of total questions`, `current category`,.

```json
{
  "question": {
    "id": 1,
    "question": "This is a question",
    "answer": "This is an answer",
    "difficulty": 5,
    "category": 4
  }
}
```
## The Documentation of the api can be found following this link : 'https://documenter.getpostman.com/view/18525553/VUxRP6La'



## Testing

Write at least one test for the success and at least one error behavior of each endpoint using the unittest library.

To deploy the tests, run

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```


