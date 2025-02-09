import os

file_path = "descriptions/Eco-Friendly Organic T-Shirt.txt"
product_name = os.path.splitext(os.path.basename(file_path))

print(product_name)