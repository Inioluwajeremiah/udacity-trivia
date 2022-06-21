# Trivia API

## Setting up the Backend

### Install Dependencies

* Python 3.7 or Python 3.7+ - You can read the official documentation of the latest version [here](https://docs.python.org/3/)
* Virtual Environment - (NB: This operation should be done in your backend folder). When using Python for projects, we recommend working in a virtual environment. This keeps your project dependencies distinct and structured. The python documentation include instructions for creating a virtual environment for your platform. You can visit this [resource](https://phoenixnap.com/kb/install-flask) for additional information on how to setup virtual environment for various OS. The core dependencies are Flask, Flask-CORS and SQLAlchemy.
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

### Running the Server
Navigate to your backend folder in your terminal and run the command below
<pre>
    set FLASK_APP=flaskr
    set FLASK_ENV=development
    flask run 
</pre>

## Frontend

The frontend is built using React JS. Developers should ensure they use the latest React JS library. 
To intall React JS, run <pre>   npm install or npm i </pre>

### Starting the Server
To start the server run <pre>   npm start </pre>


## API Documentation

### Getting Started

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration.
Authentication: This version of the application does not require authentication or API keys.


### GET '/categories'
General: 
* Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
* Returns an object with a single key, categories, that contains an object of id: category_string key: value pairs.
Sample: <code>curl http://127.0.0.1:5000/categories </code>

<pre>
    {
      "1": "Science",
      "2": "Art",
      "3": "Geography",
      "4": "History",
      "5": "Entertainment",
      "6": "Sports"
    }
</pre>

### GET '/questions'

General:
* Creates an endpoint to handle GET requests for questions, including pagination (every 10 questions).
* Returns a list of questions, number of total questions, current category, categories.
Sample: <code> curl http://127.0.0.1:5000/questions </code>

<pre>
    {
    "Success": true,
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "questions": [
        {
            "answer": "Apollo 13",
            "category": "5",
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
            "answer": "Tom Cruise",
            "category": "5",
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Maya Angelou",
            "category": "4",
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Muhammad Ali",
            "category": "4",
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        },
        {
            "answer": "Brazil",
            "category": "6",
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": "6",
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "George Washington Carver",
            "category": "4",
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        },
        {
            "answer": "Lake Victoria",
            "category": "3",
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": "3",
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
            "answer": "Agra",
            "category": "3",
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        }
    ],
    "total_questions": 26
    }
    
</pre>

### DELETE '/questions/{id}'

General:
* Creates an endpoint to DELETE question using a question ID.
* Returns the id of the deleted question, success value, total questions, and question list based on current page number to update the frontend
Sample: <code> curl -X DELETE http://127.0.0.1:5000/questions/9 </code>

<pre>
    {
    "current_questions": [
        {
            "answer": "Apollo 13",
            "category": "5",
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
            "answer": "Tom Cruise",
            "category": "5",
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Maya Angelou",
            "category": "4",
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Brazil",
            "category": "6",
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": "6",
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "George Washington Carver",
            "category": "4",
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        },
        {
            "answer": "Lake Victoria",
            "category": "3",
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": "3",
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
            "answer": "Agra",
            "category": "3",
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        },
        {
            "answer": "Escher",
            "category": "2",
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
        }
    ],
    "deleted": 9,
    "success": true,
    "total_questions": 25
    }
</pre>

### POST '/questions'
General:
* Creates an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score.
* Returns the id of the created question, success value, total questions, and question list based on current page number to update the frontend
Testing
Sample: <code> curl http://127.0.0.1:5000/books?page=3 -X POST -H "Content-Type: application/json" -d '{"question": "Who is the 45th president of the United States?", "answer":"Donald Trump", "category":"5", "difficulty":"4"}' </code>

<pre>
    {
    "created": 33,
    "questions": [
        {
            "answer": "Apollo 13",
            "category": "5",
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
            "answer": "Tom Cruise",
            "category": "5",
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Maya Angelou",
            "category": "4",
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Brazil",
            "category": "6",
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": "6",
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "George Washington Carver",
            "category": "4",
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        },
        {
            "answer": "Lake Victoria",
            "category": "3",
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": "3",
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
            "answer": "Agra",
            "category": "3",
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        },
        {
            "answer": "Escher",
            "category": "2",
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
        }
    ],
    "success": true,
    "total_questions": 26
}
</pre>

### If Search Term

### POST '/questions'

General: 
* Creates a POST endpoint to get questions based on a search term.
* Returns any questions, total number of questions for whom the search term is a substring of the question and success true value
Sample:  <code> curl http://127.0.0.1:5000/books?page=3 -X POST -H "Content-Type: application/json" -d '{"searchTerm": "movie"}' </code>

<pre>
    {
        "questions": [
            {
                "answer": "Apollo 13",
                "category": "5",
                "difficulty": 4,
                "id": 2,
                "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
            }
        ],
        "success": true,
        "total_questions": 1
    }
</pre>

### GET  /'categories/{int:id}/questions'

General:
* Creates a GET endpoint to get questions based on category.
* Returns a success true value, categories of questions, current category and a list of questions in the category querried 
Sample: <code> curl http://http://127.0.0.1:5000/categories/4/questions </code>

<pre>
    {
    "Success": true,
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "current_category": {
        "id": 4,
        "type": "History"
    },
    "questions": [
        {
            "answer": "Maya Angelou",
            "category": "4",
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "George Washington Carver",
            "category": "4",
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        },
        {
            "answer": "Scarab",
            "category": "4",
            "difficulty": 4,
            "id": 23,
            "question": "Which dung beetle was worshipped by the ancient Egyptians?"
        }
    ],
    "total_questions": 26
   }
</pre>


### POST '/quizzes'
General:
* Sends a POST equest to get questions to play the quiz. This endpoint takes category and previous question parameters
* Returns a random questions within the given category, if provided, and that is not one of the previous questions.
Sample: <code> curl http://localhost:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions":[10], "quiz_category":{"type":"Sport","id":"6"}}' </code>

<pre>
    {
    "question": {
        "answer": "Uruguay",
        "category": "6",
        "difficulty": 4,
        "id": 11,
        "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    "success": true
}
</pre>



## Testing

To deploy the tests, run

<pre>
    dropdb trivia_test
    createdb trivia_test
    psql trivia_test < trivia.psql
    python test_flaskr.py
</pre>



## Error Handling
Errors are returned as JSON objects in the following format:

{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
The API will return three error types when requests fail:

404: Resource Not Found
405: Method Not Allowed
422: Unprocessable
