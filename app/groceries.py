
# READ INVENTORY OF PRODUCTS

#products_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
#products_df = read_csv(products_filepath)
#products = products_df.to_dict("records")

import os

from app.utils import to_usd #from foldername.filename import __
from pandas import read_csv


# checks to see if a products.csv file exists. If not, it uses the default
if os.path.isfile(os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")) == True:
    print("USING CUSTOM PRODUCTS CSV FILE...")
    products = read_csv(os.path.join(os.path.dirname(__file__), "..", "data", "products.csv"))
else:
    print("USING DEFAULT PRODUCTS CSV FILE...")
    products = read_csv(os.path.join(os.path.dirname(__file__), "..", "data", "default_products.csv"))

#reads the csv file into products variable
#pandas transforms the data into a list of dictionaries
products = products.to_dict('records')



# PRINTED INVENTORY REPORT

print("---------")
print("THERE ARE", len(products), "PRODUCTS:")
print("---------")
    


all_prices = []
for p in products: #simplified into one loop
    print("..." + p["name"] + "   " + to_usd(p["price"]))
    all_prices.append(float(p["price"]))

import statistics
avg_price = statistics.median(all_prices)

print("---------")
print("AVERAGE PRICE:", to_usd(avg_price))





# EMAIL INVENTORY REPORT
