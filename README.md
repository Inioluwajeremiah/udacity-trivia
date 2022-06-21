# Trivia API

## Setting up the Backend

### Install Dependencies

* Python 3.7 or Python 3.7+ - You can read the official documentation of the latest version [here](https://docs.python.org/3/)
* Virtual Environment - (NB This operation should be doone in your backend folder). When using Python for projects, we recommend working in a virtual environment. This keeps your project dependencies distinct and structured. The python documentation include instructions for creating a virtual environment for your platform. You can visit this [resource](https://phoenixnap.com/kb/install-flask) for additional information on how to setup virtual environment for various OS. The core dependencies are Flask, Flask-CORS and SQLAlchemy.
* PIP Dependencies - Once your virtual environment is up and running, navigate to the /backend directory and run the appropriate dependencies.
<pre>
    # installs all the dependencies needed for this project
    pip install -r requirements.txt

    # alternatively, for key dependencies run
    pip install Flask
    pip install Flask-CORS
    pip install SQLAlchemy
</pre>

### Setting up the Database

This project uses the Postgres database. Install 
* Ensure you have PostgreSQL server installed on your local machine. You can downlod it [here](https://www.postgresql.org/download/)
* Login to your Postgres account via your terminal or user friendly pgAdmin
* After logging in to your terminal run 
<pre> 
    # to create a new database in windows OS
    CREATE DATABASE trivia
    # to create a new database in MAC or Linux OS
    createdb trivia
    # using pgAdmin
    expand servers at the left pane of pgAdmin software, right click on database and select create to create a new postgres database
</pre>
* To connect to your newly created database in your terminal run: <pre> \c trivia </pre>
* To populate the database you just created with the trivia.psql file provided. From the backend folder in terminal run: <pre>  psql trivia < trivia.psql </pre>
* Alrernatively you can populate your newly created database with the trivia postgres script (trivia.psql) using pgAdmin. Expand your database name, right clik on 'Schema' and select 'PSQL Tools'. In 'PSQL Tools' run: <pre> [database_name]-#  \i   /path/to/trivia.psql </pre>

Run the Server

From within the ./src directory first ensure you are working using your created virtual environment.

To run the server, execute:

flask run --reload

The --reload flag will detect file changes and restart the server automatically.
To Do Tasks

These are the files you'd want to edit in the backend:

    backend/flaskr/__init__.py
    backend/test_flaskr.py

One note before you delve into your tasks: for each endpoint, you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

    Use Flask-CORS to enable cross-domain requests and set response headers.
    Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
    Create an endpoint to handle GET requests for all available categories.
    Create an endpoint to DELETE a question using a question ID.
    Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score.
    Create a POST endpoint to get questions based on category.
    Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
    Create a POST endpoint to get questions to play the quiz. This endpoint should take a category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
    Create error handlers for all expected errors including 400, 404, 422, and 500.

Documenting your Endpoints

You will need to provide detailed documentation of your API endpoints including the URL, request parameters, and the response body. Use the example below as a reference.
Documentation Example

GET '/api/v1.0/categories'

    Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
    Request Arguments: None
    Returns: An object with a single key, categories, that contains an object of id: category_string key: value pairs.

{
  "1": "Science",
  "2": "Art",
  "3": "Geography",
  "4": "History",
  "5": "Entertainment",
  "6": "Sports"
}

Testing

Write at least one test for the success and at least one error behavior of each endpoint using the unittest library.

To deploy the tests, run

dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py

API Reference
Getting Started
Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration.
Authentication: This version of the application does not require authentication or API keys.
Error Handling
Errors are returned as JSON objects in the following format:

{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
The API will return three error types when requests fail:

400: Bad Request
404: Resource Not Found
422: Not Processable
Endpoints
GET /books
General:
Returns a list of book objects, success value, and total number of books
Results are paginated in groups of 8. Include a request argument to choose page number, starting from 1.
Sample: curl http://127.0.0.1:5000/books
  "books": [
    {
      "author": "Stephen King",
      "id": 1,
      "rating": 5,
      "title": "The Outsider: A Novel"
    },
    {
      "author": "Lisa Halliday",
      "id": 2,
      "rating": 5,
      "title": "Asymmetry: A Novel"
    },
    {
      "author": "Kristin Hannah",
      "id": 3,
      "rating": 5,
      "title": "The Great Alone"
    },
    {
      "author": "Tara Westover",
      "id": 4,
      "rating": 5,
      "title": "Educated: A Memoir"
    },
    {
      "author": "Jojo Moyes",
      "id": 5,
      "rating": 5,
      "title": "Still Me: A Novel"
    },
    {
      "author": "Leila Slimani",
      "id": 6,
      "rating": 5,
      "title": "Lullaby"
    },
    {
      "author": "Amitava Kumar",
      "id": 7,
      "rating": 5,
      "title": "Immigrant, Montana"
    },
    {
      "author": "Madeline Miller",
      "id": 8,
      "rating": 5,
      "title": "CIRCE"
    }
  ],
"success": true,
"total_books": 18
}
POST /books
General:
Creates a new book using the submitted title, author and rating. Returns the id of the created book, success value, total books, and book list based on current page number to update the frontend.
curl http://127.0.0.1:5000/books?page=3 -X POST -H "Content-Type: application/json" -d '{"title":"Neverwhere", "author":"Neil Gaiman", "rating":"5"}'
{
  "books": [
    {
      "author": "Neil Gaiman",
      "id": 24,
      "rating": 5,
      "title": "Neverwhere"
    }
  ],
  "created": 24,
  "success": true,
  "total_books": 17
}
DELETE /books/{book_id}
General:
Deletes the book of the given ID if it exists. Returns the id of the deleted book, success value, total books, and book list based on current page number to update the frontend.
curl -X DELETE http://127.0.0.1:5000/books/16?page=2
{
  "books": [
    {
      "author": "Gina Apostol",
      "id": 9,
      "rating": 5,
      "title": "Insurrecto: A Novel"
    },
    {
      "author": "Tayari Jones",
      "id": 10,
      "rating": 5,
      "title": "An American Marriage"
    },
    {
      "author": "Jordan B. Peterson",
      "id": 11,
      "rating": 5,
      "title": "12 Rules for Life: An Antidote to Chaos"
    },
    {
      "author": "Kiese Laymon",
      "id": 12,
      "rating": 1,
      "title": "Heavy: An American Memoir"
    },
    {
      "author": "Emily Giffin",
      "id": 13,
      "rating": 4,
      "title": "All We Ever Wanted"
    },
    {
      "author": "Jose Andres",
      "id": 14,
      "rating": 4,
      "title": "We Fed an Island"
    },
    {
      "author": "Rachel Kushner",
      "id": 15,
      "rating": 1,
      "title": "The Mars Room"
    }
  ],
  "deleted": 16,
  "success": true,
  "total_books": 15
}
PATCH /books/{book_id}
General:
If provided, updates the rating of the specified book. Returns the success value and id of the modified book.
curl http://127.0.0.1:5000/books/15 -X PATCH -H "Content-Type: application/json" -d '{"rating":"1"}'
{
  "id": 15,
  "success": true
}
