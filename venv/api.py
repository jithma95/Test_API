from enum import unique
from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db=SQLAlchemy(app)


class Drink(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),unique=True,nullable=False)
    description=db.Column(db.String(120))

    def __reper__(self):
        
        return f"{self.name}-{self.description}"


    


@app.route('/')
def hello_world():
    return 'Hello'
    

@app.route('/drinks')
def get_drinks():
   return {"Drinks":"Kasiya"}

app.run(host='localhost', port=3002)

 
    

