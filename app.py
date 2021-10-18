from flask import Flask,render_template,request,redirect
from flask_pymongo import PyMongo

app=Flask(__name__)
app.config['MONGO_URI']='mongodb+srv://<user name>:<your password>@cluster0.qeyfn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

mongo=PyMongo(app)

@app.route('/',methods=['GET','POST'])
def index():
    
    if request.method=='POST':
        firstname=request.form['fname']
        lastname=request.form['lname']
        #print(firstname)
        mongo.db.names.insert_one({'firstname' : firstname,'lastname':lastname})
        #print(dict(firstname=data['fname'],lastname=data['lname']))
        #print(data['fname'])
    
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)        
