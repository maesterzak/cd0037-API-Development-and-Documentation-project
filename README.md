# Project Documentation

## Fullstack Trivia Game 

## Getting Started

### Prerequisites and Dependencies Installations

#### Backend

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

##### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

#### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createdb trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

##### Run the Server

From within the backend directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
Setting the FLASK_ENV variable to development will detect file changes and restart the server automatically.

Setting the FLASK_APP variable to flaskr directs flask to use the flaskr directory and the __init__.py file to find the application.



##### Tests

In terminal execute:

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

#### Frontend 

From the frontend folder, run the following commands to start the client:

```bash
    npm install // only once to install all dependencies
    npm start
```

By default, the frontend will run on localhost:3000
## API Reference

This is the backend api for the udacitrivia game

### Getting Started
- BASE URL: At present this api app can only be run locally is not hosted as a base URL. The app is hosted at the default, http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration.

- AUTHENTICATION: This version of the api does not require any api authentication or keys.

### Error Handling

Errors returned are json objects in the format shown below.

``` json5
{

    "success": False,

    "error": 404,

    "message": "Resource(s) Not Found"
}
```

The Api will return three (3) error types when requests fail:

- 400: Bad Request,
- 404: Request Not Found,
- 422: Not Processable,
- 500: Internal Server Error

### Endpoints

#### GET /categories

- **General**

    - Returns a list of all categories, success value and the total amount of categories.
    
 - **Sample request**:
``` bash
    curl http://127.0.0.1:5000/categories
```

 - **Sample response**

``` json
 {
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true, 
  "total_categories": 6
}
```

#### GET /questions

- **General**
  - Returns a list of all categories, paginated questions, success value and total number of questions in database.
  - The questions are paginated in groups of 10. Including a request argument to choose page number starting from 1.  

- **Request parameters**
    - Current page number (default is 1)

- **Sample request**
  ``` bash
    curl http://127.0.0.1:5000/questions?page=1
  ```

- **Sample response**

```json5
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 34
} 
```

#### DELETE /questions/{id}

- **General**
    - Deletes the question if the given question ID exists. Returns the ID of the deleted question and a success value.

- **Request parameters**
    - ID of the question to be deleted(<int:id>)

- **Sample request**
  ``` bash
    curl -X DELETE http://127.0.0.1:5000/238
  ```

- **Sample response**

```json5
{
  "deleted": 238,
  "success": true
}
```


#### POST /questions

- **General**
    - Creates a new question using the submitted question, answer, category and difficulty.
    - Returns a success value, and the id of the newly created question.

- **Request body**
``` json
{
  "question": string,
  "answer": string,
  "difficulty": int,
  "category": string
}
  ```

- **Sample request**
  ``` bash
    curl -X POST -H "Content-Type":"application/json" -d '{"question":"example question", "answer":"example answer", "category":1,"difficulty":2}' http://127.0.0.1:5000/questions
  ```

- **Sample response**

```json5
{
  "created": 20,
  "success": true
}  
```


#### POST /questions/search

- **General**
    -  Gets all questions where a substring matches the search term (not case-sensitive)
    - Returns paginated list of questions, success value, total number of questions that matched search term and current category.

- **Request body**
``` json
    {"searchTerm":string}
```
    
- **Sample request**
  ``` bash
    curl -X POST -H "Content-Type":"application/json" -d '{"searchTerm":"which"}' http://127.0.0.1:5000/questions/search
  ```

- **Sample response**

``` json
   {
    "current_category": null,
    "questions": [
        {
            "answer": "Jackson Pollock",
            "category": 2,
            "difficulty": 2,
            "id": 19,
            "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
        }
    ],
    "success": true,
    "total_questions": 1
} 
```

#### GET /categories/{id}/questions

- **General**
    - Gets all the questions for the specified category
    - Returns paginated list of questions, total number of questions in specified category, success value and the current category.

- **Request parameters**
    - ID of the category whose questions you seek.

- **Sample request**
  ``` bash
    curl http://127.0.0.1:5000/categories/2/questions
  ```

- **Sample response**

``` json
    {
    "current_category": {
        "id": 5,
        "type": "Entertainment"
    },
    "questions": [
        {
            "answer": "Apollo 13",
            "category": 5,
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }
    ],
    "success": true,
    "total_questions": 3
}
```

#### POST /quizzes

- **General**
    - Returns a random question of the specified category.
    - If no category is specified (all), it returns a random question from the database.
    - Also returns total number of questions in specified category.

- **Request body**
``` json
 {
    "previous_questions":[],
    "quiz_category":{"id":6,"type":"Sports"}  
}
  ``` 

- **Sample request**
  ``` bash
    curl -X POST -H "Content-Type":"application/json" -d '{"searchTerm":"with"}' http://127.0.0.1:5000/quizzes
  ```

- **Sample response**

``` json
    {
    "question": {
        "answer": "Uruguay",
        "category": 6,
        "difficulty": 4,
        "id": 11,
        "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    "success": true,
    "totalQuestions": 2
}
```


## Deployment N/A

## Authors
Abubakar Zakari and Udacity team
## Acknowledgements

The awesome team at Udacity and my fellow students, soon to be fullstack developers!.



