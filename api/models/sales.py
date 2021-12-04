from products import Products
sales=[]

class Sales(Products):

    def __init__(self,saleId,):
        self.saleId=saleId
#this method gets all the sales data from the sales structure above
    def allSales(self):
        return sales
# This method returns a single sale using its saleId
    def oneSale(self):
        if self.saleId  in sales:
            return sales[self.saleId]
            

        else:
            return f"The {self.saleId} id is not present"

    #this method adds a single sale in the sales list      
    def addSale(self):
        
        saleInfo={
            self.saleId==len(sales)+1 ,
            self.category=='category',
            self.name=='name',
            self.price=='price'
        }
        sales.append(saleInfo)
        return saleInfo
#this method deletes a single sale in the sale list
    def deleteSale(self):
        for sale in sales:
            sale=[self.saleId=='id',
                self.category=='category',
                self.name=='name',
                self.price=='price'
                
            ]
            sales.remove(sale)
            return sale
s=Sales()        

       
          
           
    
    