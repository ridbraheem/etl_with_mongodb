from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import pyodbc

DB = {'servername': '',
      'database': 'AdventureWorksDW2019',
      'driver': 'driver=SQL Server Native Client 11.0'}
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' 
                      + DB['servername'] 
                      + ';DATABASE=' 
                      + DB['database'] 
                      + ';Trusted_Connection=yes')
cursor = conn.cursor()
engine = create_engine('mssql+pyodbc://' 
                       + DB['servername'] + '/' 
                       + DB['database'] + "?" 
                       + DB['driver'])

class ExtractData:
    
    def getcustomers():
        
        query = ("""SELECT CustomerKey AS 'CustomerID'
            , FirstName
            , LastName
            , EmailAddress
            , BirthDate 
            FROM DimCustomer
            """)
          
        df = pd.read_sql(query,con=engine)
        
        return df

    
    def getsubcats():
        
        query = ("""SELECT ProductSubcategoryKey AS 'SubCategoryID'
            , EnglishProductSubcategoryName AS 'SubcategoryName'
            FROM DimProductSubcategory
            """)
        
        df = pd.read_sql(query,con=engine)
        
        return df
        
    def getorders():
        
        query = ("""SELECT SalesOrderNumber AS 'OrderID'
            , CONVERT(date,OrderDate) AS 'OrderDate'
            , CustomerKey AS 'CustomerID'
            , ProductKey AS 'ProductID'
            , OrderQuantity
            , SalesAmount  
            FROM FactInternetSales
            """)
        
        df = pd.read_sql(query,con=engine)
        
        return df
        
    def getproductnull():
        
        query = ("""SELECT ProductKey AS 'ProductID'
            , EnglishProductName AS 'ProductName'
            , Color
            FROM DimProduct
            WHERE ProductSubcategoryKey IS NULL
            """)
        
        df = pd.read_sql(query,con=engine)
        
        return df
    
    def getproduct():
        
        query = ("""SELECT ProductKey AS 'ProductID'
            , EnglishProductName AS 'ProductName'
            , Color
            , ProductSubcategoryKey  AS 'SubCategoryID'
            FROM DimProduct
            WHERE ProductSubcategoryKey IS NOT NULL
            """)
        
        df = pd.read_sql(query,con=engine)
        
        return df

