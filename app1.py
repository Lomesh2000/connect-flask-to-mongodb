from flask import Flask,render_template,request,redirect
from pymongo import MongoClient

app=Flask(__name__)
client=MongoClient('mongodb://127.0.0.1:27017')
db=client['names']
collection=db.record



@app.route('/',methods=['GET','POST'])
def index():
    
    if request.method=='POST':
        firstname=request.form['fname']
        lastname=request.form['lname']
        print(firstname)
        db.record.insert_one({'firstname' : firstname,'lastname':lastname})
        #print(dict(firstname=data['fname'],lastname=data['lname']))
        #print(data['fname'])
    
    return render_template('index.html') 


if __name__=='__main__':
    app.run(debug=True)        
