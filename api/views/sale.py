from flask import Flask,jsonify,Blueprint,request
from flask_restful import Resource,Api


app=Flask(__name__)
api=Api(app,prefix='/api')
apiBp=Blueprint('api',__name__)

sales=[
    {'iphone':2000},
    {'tekno':1500},
    {'samsung':2500},
    {'dell':35000},
    {'macbook':100000},
    {'asus':1300},
    {'lenovo':23000}
]

class AllSales(Resource):
    def get(self):
        return sales
api.add_resource(AllSales,'/sales')
app.register_blueprint(apiBp)
class Singlesale(Resource):
    def get(self,salesId):
        return sales[salesId]
class Sales(Resource):
    def post(self):
        item=request.get_json()

        if not item:
            return {'message':'field cannot be empty'}
        saleId=len(sales)+1
        saleName=item.get('name')
        salePrice=item.get('price')
        addedSale=sales.add(saleId,saleName,salePrice)
        response=jsonify(addedSale)

        return response

    def get(self):
        return sales
api.add_resource(Sales,"/sales/add")
app.register_blueprint(apiBp)

class SalesId(Resource):
    def get(self):
        
        salesId=len(sales)+1
        response=jsonify(salesId)
        return response
api.add_resource(SalesId,"/sales/salesId")
app.register_blueprint(apiBp)


if __name__=="__main__":
    app.run(debug=True)
