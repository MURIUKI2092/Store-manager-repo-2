market=[
]
class Products():
    def __init__(self,productId,category,name,price):
        self.productId=productId
        self.category=category
        self.name=name
        self.price=price
# This method returns all the items in the market
    def all_product(self):
        return market
#this methods return a single Item in the market list using the productId already defined in the constructor
    def singleProduct(self):
        return market[self.productId]
# This method adds a product to the market list. the product has  an Id which is automatically generated and the other features
    def add_product(self):
        
        product=[self.productId==len(market)+1,
                self.category=='category',
                self.name=='name',
                self.price=='price'
        ]
        market.append(product)
        return product
# This method delete a product from the market.
    def deleteProduct(self):
        for product in market:
            product=[self.productId=='id',
                    self.category=='category',
                    self.name=='name',
                    self.price=='price'

                ]
            market.remove(product)
        return product


p=Products()