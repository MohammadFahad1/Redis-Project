import os
import sys
import django
from faker import Faker
import random

# 1. Get the path to the project root (one level up from /api)
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# 2. Set settings (Check if your folder is named 'Redis_Project' or something else)
# If your settings.py is in a folder named 'core', use 'core.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'redis_project.settings') 

django.setup()

# Now import your models
from api.models import Product, Order

fake = Faker()

def seed_data(n=200):
    for _ in range(n):
        # Create Product
        product = Product.objects.create(
            name=fake.catch_phrase(),
            description=fake.text(),
            price=round(random.uniform(10.0, 500.0), 2),
            stock=random.randint(1, 100),
            image=fake.image_url()
        )
        
        # Create Order
        Order.objects.create(
            customer=fake.name(),
            address=fake.address(),
            total=product.price * random.randint(1, 3),
            products=product.name
        )
    print(f"Successfully added {n} dummy records!")

if __name__ == "__main__":
    seed_data(9000) # Change number as needed
    print("Done!")