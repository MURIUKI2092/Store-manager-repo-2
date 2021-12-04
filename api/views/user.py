from flask import Flask,jsonify,Blueprint,request
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app,prefix='/api')
apiBp=Blueprint('api',__name__)
users={
    'james':{'age':22,'title':'intern','category':'laptops'},
    'sammy':{'age':32,'title':'Admin','category':'General'},
    'Alice':{'age':24,'title':'worker','category':'phones'}
}
class Users(Resource):
    def get(self):
        return jsonify(users) 
api.add_resource(Users,'/users')
app.register_blueprint(apiBp)

class Singleuser(Resource):
    def get(self,user):
        if user not in users:
            response='the user entered is not in the store'
            return jsonify (response)
        else:
            return users[user]
api.add_resource(Singleuser,'/users/<string:user>')
app.register_blueprint(apiBp)

class AddUser(Resource):
    def post(self):
        person=request.get_json()

        if not person:
            return {"message":"field cannot be empty"}
        else:
            personId=len(users)+1
            personName=person.get('name')
            personAge=person.get('age')
            persontitle=person.get('title')
            personCategory=person.get('category')
            userAdded=users.add(personId,personName,personAge,persontitle,personCategory)
            newUser=jsonify(userAdded)
            return newUser

    def get(self):
        return users
api.add_resource(Singleuser,'/users/add')
app.register_blueprint(apiBp)

if __name__=="__main__":
    app.run(debug=True)