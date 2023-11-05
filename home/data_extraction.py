from .models import Laptops,Mobiles
from .data import One_plus_data,laptop_details



def Mobiles_data_exctraction():
    try:
        oneplus = One_plus_data()
        one_plus_data = []
        for dt in oneplus:
            try:
                obj, _ = Mobiles.objects.get_or_create(
                    Product_Name=dt['Product_Name'],
                    Product_Price=dt['Product_Price'],
                    Product_Reviews=dt['Product_Reviews']
                )
                one_plus_data.append(obj)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)

def Laptop_data_extraction():
    try:
        lapy_list = []
        laptops = laptop_details()
        for dt in laptops:
            try:
                obj,_ = Laptops.objects.get_or_create(
                    brand_name = dt['brand Name'],
                    price = dt['price'],
                    discription = dt['discription'],
                    reviews = dt['reviews'],
                )
                lapy_list.append(obj)

            except Exception as e:
                print(e)
    except Exception as e:
        print(e)