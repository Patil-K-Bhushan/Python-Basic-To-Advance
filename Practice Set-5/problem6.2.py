products = {
    "Laptop": 55000,
    "Phone": 25000,
    "Tablet": 30000,
    "Monitor": 15000
}

highest_product = max(products, key=products.get)

print("Product with highest price:", highest_product)
print("Highest price:", products[highest_product])
