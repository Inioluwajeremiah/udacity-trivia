import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = f'postgresql://postgres:Malibowe100%@localhost:5432/{self.database_name}'
        # "postgresql://{}/{}".format(
        #     'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {"question": "What programming language is used in flask micro framework",
                             "answer": "Python", "category": 5, "difficulty": 2}

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_question_categories(self):
        res = self.client().get("/categories")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["Success"], True)
        self.assertTrue(data["categories"])

    def test_get_question_by_category(self):
        res = self.client().get("/categories/1/questions")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["Success"], True)
        self.assertTrue(data["questions"])
        self.assertTrue(data["categories"])
        self.assertTrue(len(data["questions"]))

    def test_404_get_question_beyond_category_id(self):
        res = self.client().get("/categories/5000/questions")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Resource Not Found")

    def test_405_get_question_by_category_id_not_allowed(self):
        res = self.client().post("/categories/9000/questions", json=self.new_question)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Method not allowed")

    def test_get_paginated_questions(self):
        res = self.client().get("/questions")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["Success"], True)
        self.assertTrue(data["total_questions"])
        self.assertTrue(data["categories"])
        self.assertTrue(len(data["questions"]))

    def test_delete_question(self):
        res = self.client().delete("/questions/10")
        data = json.loads(res.data)
        question = Question.query.filter(Question.id == 10).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["deleted"], 10)
        self.assertTrue(data["total_questions"])
        self.assertEqual(question, None)

    def test_422_if_question_does_not_exist(self):
        res = self.client().delete("/questions/1000")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unprocessable")

    def test_404_beyond_paginated_questions(self):
        res = self.client().get("/questions?page=1000")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Resource Not Found")

    def test_create_new_questions(self):
        res = self.client().post("/questions", json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["created"], 1)
        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["questions"]))

    def test_get_question_search_with_results(self):
        res = self.client().post("/questions", json={"search": "movie"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_questions"])
        self.assertEqual(len(data["questions"]), 10)

    def test_get_question_search_without_results(self):
        res = self.client().post("/questions", json={"search": "apple-jacks"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_questions"])
        self.assertEqual(len(data["questions"]), 10)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
