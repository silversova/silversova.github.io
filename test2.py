from bs4 import BeautifulSoup
from scrapingant_client import ScrapingAntClient

# Define URL with a dynamic web content
url = "https://kami4ka.github.io/dynamic-website-example/"

# Create a ScrapingAntClient instance
client = ScrapingAntClient(token='7914a7fb2d6c447d9232c020c7c07909')

# Get the HTML page rendered content
page_content = client.general_request(url).content

# Parse content with BeautifulSoup
soup = BeautifulSoup(page_content, 'lxml')
print(soup.find(id="test").get_text())
