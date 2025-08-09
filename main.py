from jinja2 import Environment, FileSystemLoader
import os

import wiki_scraper

wiki_prophesies = wiki_scraper.get_data()

# Setup Jinja2
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("index.html")

# Render HTML with scraped data
output = template.render(prophecies=wiki_prophesies)

# Save to dist/
os.makedirs("dist", exist_ok=True)
with open("dist/index.html", "w", encoding="utf-8") as f:
    f.write(output)

print("✅ Site generated at dist/index.html")
