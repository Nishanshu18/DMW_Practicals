import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_snapdeal(product_name):
    print("\nScraping Snapdeal for:", product_name.upper())
    
    url = f"https://www.snapdeal.com/search?keyword={product_name}"
    response = requests.get(url, headers=headers)
    
    soup = bs(response.text, "html.parser")
    products = soup.find_all("div", class_="product-tuple-listing")
    
    data = []
    
    for product in products:
        name = product.find("p", class_="product-title")
        name = name.text.strip() if name else "N/A"
        
        price = product.find("span", class_="product-price")
        price = price.text.strip() if price else "N/A"
        
        discount = product.find("div", class_="product-discount")
        discount = discount.text.strip() if discount else "No Discount"
        
        data.append({
            "Search Item": product_name,
            "Name (Description)": name,
            "Price (Rs)": price,
            "Discount": discount
        })
    
    return data

laptop_data = scrape_snapdeal("laptop")
phone_data = scrape_snapdeal("phone")

all_data = laptop_data + phone_data

df = pd.DataFrame(all_data)

df.to_excel("Snapdeal_Laptop_Phone.xlsx", index=False)

print("\nFinal Output:")
print(df)
