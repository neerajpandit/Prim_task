import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Primeintrn.settings')
django.setup()

from app.models import Dish  

def import_data():
    csv_file = 'E:\Drf\Primeintrn\restaurants_small.csv'

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  

        for row in reader:
       
            field1 = row[0]  
            field2 = row[1]   
            obj = Dish(field1=field1, field2=field2)  
            obj.save()
