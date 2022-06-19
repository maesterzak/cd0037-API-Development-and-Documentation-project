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
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            'abubakar', '2019', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)    

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
    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res._status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertTrue(len(data['categories']))

       

    def test_get_paginated_qestions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))
        self.assertEqual(data['current_category'], None)
        


    def test_404_requesting_questions_for_invalid_pages(self):
        res = self.client().get('/questions?page=900')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource(s) Not Found')
        


    def test_delete_qestion(self):
        question = Question(
            question='example question',
            answer= 'example answer',
            difficulty= 1,
            category= 1
            )
        question.insert()
        id = question.id
        
        res = self.client().delete(f'/questions/{id}')
        data = json.loads(res.data)

        question = Question.query.filter(Question.id == id).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], id)


    def test_404_request_deletion_of_non_existing_question(self):
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource(s) Not Found')

    def test_add_question(self):
        question = {
            "question":"example question",
            "answer": 'example answer',
            "difficulty": 1,
            "category": 1
        }
        
        res = self.client().post('/questions', json=question)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_400_add_question_error(self):
        question = {
            "question":"",
            "answer":"",
            "category":1,
            "difficulty":1        
        }

        res = self.client().post('/questions', json=question)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')    


    def test_get_questions_by_category(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)

        category = Category.query.get(1)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))
        self.assertEqual(data['current_category'], category.format())


    def test_get_questions_by_non_existing_category(self):
        res = self.client().get('/categories/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource(s) Not Found')


    def test_get_search_questions(self):
        data = {"searchTerm":"yo"}
        res = self.client().post('/questions/search', json=data)
        data = json.loads(res.data)


        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))
        self.assertEqual(data['current_category'], None)
    
    
    def test_get_search_non_existing_question(self):
        data = {"searchTerm":"halala"}
        res = self.client().post('/questions/search', json=data)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource(s) Not Found')    


            


    def test_get_random_quiz_by_category(self):
        category = Category.query.get(6)
        data = {
            "previous_questions": [],
            "quiz_category": category.format()
        }
        res = self.client().post('/quizzes', json=data)
        data = json.loads(res.data)
        
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])
        self.assertTrue(data['totalQuestions'])


    def test_get_random_quiz_question(self):
        data = {
            "previous_questions": [10],
            "quiz_category": {"type":"all", "id":0}
        }
        res = self.client().post('/quizzes', json=data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])  
        self.assertTrue(data['totalQuestions'])


    def test_422_quiz_question_error(self):
        category = Category.query.get(3)
        data = {
            
            "quiz_category": category.format()
        }
        res = self.client().post('/quizzes', json=data)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Processable')    

    



        
           
        



        


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()