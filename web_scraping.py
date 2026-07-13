import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Store data
books = []

# Find all book cards
for book in soup.find_all("article", class_="product_pod"):
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    availability = book.find("p", class_="instock availability").text.strip()

    books.append({
        "Title": title,
        "Price": price,
        "Availability": availability
    })

# Create DataFrame
df = pd.DataFrame(books)

# Save as CSV
df.to_csv("books_dataset.csv", index=False)

# Print data
print(df)

print("\nData saved successfully as books_dataset.csv")