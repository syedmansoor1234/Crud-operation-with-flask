from flask import Flask,jsonify,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:123@localhost:5432/student"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)
ma=Marshmallow(app)

class Student(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(40),nullable=False)
    age=db.Column(db.Integer,nullable=False)
    Class=db.Column(db.Integer,nullable=False)
    phone=db.Column(db.Integer,nullable=False)
    
def __repr__(self):
    return "f{self.id}-{self.name}"

class StudentSchema(ma.SQLAlchemySchema):
    class Meta:
        model=Student
    id=ma.auto_field()
    name=ma.auto_field()
    age=ma.auto_field()
    Class=ma.auto_field()
    phone=ma.auto_field()
student_schema=StudentSchema()
student_schema=StudentSchema(many=True)


@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="POST":
        name=request.form['name']
        age=request.form['age']
        Class=request.form['Class']
        phone=request.form['phone']
        new_user=Student(name=name,age=age,Class=Class,phone=phone)
        db.session.add(new_user)
        db.session.commit()
    show=Student.query.all()
    return render_template("index.html",show=show)
@app.route('/student',methods=["POST","GET"])
def get_details():
    get_data=Student.query.all()
    return student_schema.jsonify(get_data)


@app.route('/des',methods=["POST"])
def des():
    student=Student.query.all()
    data=request.get_json()
    name = data.get("name")
    age = data.get("age")
    Class = data.get("class")
    phone = data.get("phone")
    new_student = Student(name=name, age=age, Class=Class, phone=phone)

    db.session.add(new_student)
    db.session.commit()

    return student_schema.jsonify({'message':'successfully','user':new_student}), 201 

@app.route("/lis")
def lis():
    li=['Rahul',23,'CSE','RRCE']
    return jsonify(li)

@app.route("/tup")
def tup():
    t=("syed",22,20000,"CSE")
    return jsonify({"data":t})

@app.route("/dict")
def dic():
    d={'name':'Tejas','age':22,'Salary':25000}
    return  jsonify(d)

if __name__=="__main__":
    app.run(debug=True)





# @app.route("/ser")
# def Serialization():
#     data={'id':2,'name':'tejas','age':24,'course':'python'}
#     return jsonify(data)

# @app.route("/des",methods=['GET',"POST"])
# def Deserialization():
#     data=request.get_json()
#     return jsonify({'message':'user created successfully',"data":data})



