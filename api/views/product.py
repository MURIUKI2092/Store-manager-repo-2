from flask import Flask,jsonify,Blueprint,Response
from flask_restful import Resource,reqparse,Api


app=Flask(__name__)
api=Api(app,prefix='/api')
apiBp=Blueprint('api',__name__)
market={
    1:{'iphone':2000},
    2:{'tekno':1500},
    3:{'samsung':2500},
    4:{'dell':35000},
    5:{'macbook':100000},
    6:{'asus':1300},
    7:{'lenovo':23000}
}
market_post_args=reqparse.RequestParser()
market_post_args.add_argument('name',type=str,help='name required',required=True)
market_post_args.add_argument('price',type=int,help='price required',required=True)
class ProductsApi(Resource):
    def get(self):
      
        return market
api.add_resource(ProductsApi,"/products")
app.register_blueprint(apiBp)

class Product(Resource):
    def get(self,productId):
        if productId not in market:
            response=jsonify('product Id not present')
            return response
        Response(jsonify('The following products were found'))
        return market[productId]

    def post(self,productId):
        args=market_post_args.parse_args()
        
        if productId in market:
            return Response(jsonify('product already exist'))

        market[productId]={"name":args["name"],"price":args["price"]}
        return market[productId]

api.add_resource(Product,"/products/<int:productId>")
app.register_blueprint(apiBp)



if __name__=="__main__":
    app.run(debug=True)