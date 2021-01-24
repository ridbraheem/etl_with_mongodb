# https://medium.com/@joshuacordoba/how-to-update-records-in-salesforce-using-python-c60bdd1f05b1
from mongo.mongocollections import Subcat, Customer, Product, Orders
from sql.extract import ExtractData
from pymongo import MongoClient
from mongoengine import *
import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["NewDB"]
connect('NewDB', host='localhost', port=27017)

q = ExtractData


def load_sub():
    pairs = list(q.getsubcats().itertuples(index=False, name=None))
    for i, v in pairs:
        subcat = Subcat(SubCategoryID=i, SubcategoryName = v)
        subcat.save() 


def load_product():
    pairs = list(q.getproduct().itertuples(index=False, name=None))
    for a, b, c, d in pairs:
        product = Product(ProductID=a, ProductName = b, Color = c, SubCategoryID = d)
        product.save() 


def load_customer():
    pairs = list(q.getcustomers().itertuples(index=False, name=None))
    for a, b, c, d, e in pairs:
        customer = Customer(CustomerID=a, FirstName = b, LastName = c, EmailAddress = d, BirthDate = e)
        customer.save() 


def load_product_n():
    pairs = list(q.getproductnull().itertuples(index=False, name=None))
    for a, b, c in pairs:
        product = Product(ProductID=a, ProductName = b, Color = c)
        product.save() 


def load_orders():
    pairs = list(q.getorders().itertuples(index=False, name=None))
    for a, b, c, d, e, f in pairs:
        orders = Orders(OrderID  =a, OrderDate = b, CustomerID = c, ProductID = d, OrderQuantity = e, SalesAmount = f)
        orders.save() 

