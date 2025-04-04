from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
import os

# Get the absolute path of the current directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Create Flask app with explicit instance path
app = Flask(__name__, instance_path=os.path.join(basedir, 'instance'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Print the absolute path of the database
print(f"Database path: {os.path.abspath(os.path.join(app.instance_path, 'test.db'))}")

# Create database tables if they don't exist
with app.app_context():
    db.create_all()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))


    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        
        except:
            return 'There was an issue adding your task'
        
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    
    except:
        return 'There was a problem deleting that task'
    
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']
        
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('update.html', task=task)
        

if __name__ == '__main__':
    app.run(debug=True)