from mongoengine import *

class Subcat(Document):
    SubCategoryID = LongField(required=True, primary_key = True)
    SubcategoryName = StringField(max_length=50, unique = True)
    
class Customer(Document):
    CustomerID = LongField(required=True, primary_key = True)
    FirstName = StringField(max_length=50, required=True)
    LastName = StringField(max_length=50, required=True)
    EmailAddress = StringField(required=True, max_length=80, unique = True)
    BirthDate = DateTimeField(required=True)
    
class Product(Document):
    ProductID = LongField(required=True, primary_key = True)
    ProductName = StringField(max_length=50, required=True)
    Color = StringField(max_length=50)
    SubCategoryID = ReferenceField(Subcat)
    
class Orders(Document):
    OrderID = StringField(required=True, primary_key = True)
    OrderDate = DateTimeField(required=True)
    CustomerID = ReferenceField(Customer)
    ProductID = ReferenceField(Product)
    OrderQuantity = LongField(required=True)
    SalesAmount = FloatField(required=True)

