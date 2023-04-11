from flask import Flask, render_template, request, url_for, redirect
from bson.objectid import ObjectId
from pymongo import MongoClient
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '5ce4035efd7075109bc7139adaba2ff1c853035b'

app.debug = True

# Setting up the MongoDB database connection
client = MongoClient("mongodb+srv://lucasbandeira06:Password1@flaskapp.pajmk5z.mongodb.net/?retryWrites=true&w=majority")
db = client.test

# Setting up the database and collections
db = client.FlaskApp
todos = db.ToDos


@app.route('/', methods=('GET', 'POST'))
def index():

    if request.method == 'POST':
        # Get the content, degree of priority, and due date from the form
        content = request.form['content']
        degree = request.form['degree']
        due_date = request.form['frequency']

        # Insert the new todos into the todos collection
        todos.insert_one({'content': content, 'degree': degree, 'due_date': due_date})

        # Redirect to the index page to show the updated list of todos
        return redirect(url_for('index'))

    # Find all todos in the database
    all_todos = todos.find()

    # Render the index.html template with the todos data
    return render_template('index.html', todos=all_todos)


# Delete the todo with the given id from the Atlas database.
@app.post('/<id>/delete/')
def delete(id):
    # Delete the todos from the todos collection using its ID
    todos.delete_one({"_id": ObjectId(id)})

    # Redirect to the index page to show the updated list of todos
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(ssl_context=None)