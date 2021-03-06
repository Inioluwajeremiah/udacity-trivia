import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    # cors = CORS(app, resources={r"*/api/*": {origins: '*'}})
    CORS(app, resources={"/": {"origins": "*"}})
    # CORS(app)

    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """

    @app.route('/categories', methods=['GET'])
    def get_category():
        all_category = Category.query.all()
        category = {category.id: category.type for category in all_category}

        if not all_category:
            abort(404)
        else:
            # print(category)
            return jsonify({
                "Success": True,
                "categories": category
            }), 200

    """
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """

    @app.route('/questions', methods=['GET'])
    def get_question():
        selection = Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request, selection)

        all_Category = Category.query.all()
        get_category = {
            category.id: category.type for category in all_Category}

        if len(current_questions) == 0:
            abort(404)

        return jsonify({
            "Success": True,
            "questions": current_questions,
            "categories": get_category,
            "total_questions": len(Question.query.all()),
        }), 200

        # selection = Question.query.order_by(Question.id).all()
        # current_questions = paginate_questions(request, selection)

        # if len(current_questions) == 0:
        #     abort(404)

        # # This endpoint should return a list of questions,
        # # number of total questions, current category, categories.
        # return jsonify({
        #     'success': True,
        #     'questions': current_questions,
        #     'total_questions': len(selection),
        #     'current_category': [],
        #     'categories': [cat.type for cat in Category.query.all()],
        # }), 200

    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """

    @app.route("/questions/<int:question_id>", methods=["DELETE"])
    def delete_question(question_id):
        try:
            question = Question.query.filter(
                Question.id == question_id).one_or_none()

            if question is None:
                abort(404)

            question.delete()
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)

            return jsonify(
                {
                    "success": True,
                    "deleted": question_id,
                    "current_questions": current_questions,
                    "total_questions": len(Question.query.all()),
                }
            ), 200

        except:
            abort(422)

    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """

    @app.route("/questions", methods=["POST"])
    def create_question():
        body = request.get_json()

        question = body.get("question", None)
        answer = body.get("answer", None)
        category = body.get("category", None)
        difficulty = body.get("difficulty", None)
        search = body.get("searchTerm", None)

        try:
            if search:
                selection = Question.query.order_by(Question.id).filter(
                    Question.question.ilike("%{}%".format(search))).all()
                current_questions = paginate_questions(request, selection)

                return jsonify(
                    {
                        "success": True,
                        "questions": current_questions,
                        "total_questions": len(selection),
                    }
                )
            else:

                new_question = Question(
                    question=question, answer=answer, category=category, difficulty=difficulty)
                new_question.insert()

                select_questions = Question.query.order_by(Question.id).all()
                current_questions = paginate_questions(
                    request, select_questions)

                return jsonify(
                    {
                        "success": True,
                        "created": new_question.id,
                        "questions": current_questions,
                        "total_questions": len(Question.query.all()),
                    }
                )

        except:
            abort(400)

    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """

    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """

    @app.route("/categories/<int:id>/questions", methods=["GET"])
    def get_questions_by_category(id):

        get_category = Category.query.filter(Category.id == id).one_or_none()

        if get_category is None:
            abort(404)

        try:
            selection = Question.query.order_by(
                Question.id).filter_by(category=str(id)).all()
            current_questions = paginate_questions(request, selection)

            if len(current_questions) == 0:
                abort(404)

            return jsonify(
                {
                    "Success": True,
                    "questions": current_questions,
                    "current_category": get_category.format(),
                    'categories': {category.id: category.type for category in Category.query.all()},
                    "total_questions": len(Question.query.all()),
                }
            ), 200

        except:
            abort(422)

    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """

    @app.route('/quizzes', methods=['POST'])
    def start_quiz():

        body = request.get_json()
        quiz_category = body.get('quiz_category', "")
        previous_questions = body.get('previous_questions', "")

        print(quiz_category)
        print(previous_questions)
        try:

            if quiz_category['id']:
                questions = Question.query.filter(
                    Question.category == quiz_category['id']).all()
            else:
                questions = Question.query.filter(
                    Question.id.not_in(previous_questions)).all()

            random_question = random.choice(questions)

            return jsonify({
                'success': True,
                'question': random_question.format()
            })

        except Exception:
            abort(404)

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad Request'
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource Not Found"
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method not allowed"
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable"
        }), 422

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Internal Server Error.'
        }), 500

    return app
