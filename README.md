Backend - Trivia API
Setting up the Backend
Install Dependencies

    Python 3.7 - Follow instructions to install the latest version of python for your platform in the python docs

    Virtual Environment - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the python docs

    PIP Dependencies - Once your virtual environment is setup and running, install the required dependencies by navigating to the /backend directory and running:

pip install -r requirements.txt

Key Pip Dependencies

    Flask is a lightweight backend microservices framework. Flask is required to handle requests and responses.

    SQLAlchemy is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in app.pyand can reference models.py.

    Flask-CORS is the extension we'll use to handle cross-origin requests from our frontend server.

Set up the Database

With Postgres running, create a trivia database:

createbd trivia

Populate the database using the trivia.psql file provided. From the backend folder in terminal run:

psql trivia < trivia.psql

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
