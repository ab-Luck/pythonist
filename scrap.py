import requests
from bs4 import BeautifulSoup

# Define the URL of the website to scrape
url = 'https://example-blog.com/robots.txt'

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all elements with the class 'post-title' (replace with actual class)
    titles = soup.find_all(class_='post-title')

    # Print the titles
    for title in titles:
        print(title.get_text())
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
