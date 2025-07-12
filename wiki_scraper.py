import requests
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader
import os

# Dummy data: Replace this URL with a real prophecy source
url = "https://en.wikipedia.org/wiki/List_of_dates_predicted_for_apocalyptic_events"  # Replace with real URL
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Scrape example data (e.g. <h2> tags)
prophecies = [h2.text.strip() for h2 in soup.find_all("h2")]
print(prophecies)

# Setup Jinja2
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("index.html")

# Render HTML with scraped data
output = template.render(prophecies=prophecies)

# Save to dist/
os.makedirs("dist", exist_ok=True)
with open("dist/index.html", "w", encoding="utf-8") as f:
    f.write(output)

print("✅ Site generated at dist/index.html")
