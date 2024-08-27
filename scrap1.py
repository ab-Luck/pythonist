import requests
from bs4 import BeautifulSoup

def scrape_amazon(url):
  headers = {'User-Agent': 'Your User-Agent'}
  response = requests.get(url, headers=headers)
  soup = BeautifulSoup(response.content, 'html.parser')

  # Find specific elements and extract data
  title = soup.find('span', id='productTitle').text.strip()
  price = soup.find('span', id='priceblock_ourprice').text.strip()
  # ... other elements ...

  return {'title': title, 'price': price}

# Example usage:
url = 'https://www.amazon.com/Headphone-4-Zipper-Pockets-Traveling-Outdoors/dp/B07WYKJXXY/ref=sr_1_2?crid=D49GCXA6ZZCT&dib=eyJ2IjoiMSJ9.4n2XrA0KirdiepjjjD66Ag7j4eyTk8hQMFqQ2cDIx8Vs-VKlnDKCTKTdMlfSR8Dnfq2OmKQkTi2OeIhYSidKmycEPpGe9Fc1YCOL1dHFIj6q2YAD_qNYj8MuB06zHmQO8eKiZ02MSkIE7JbTq6eZ1aQXAInPeq8qLnp00adCfW1KDgGz755W5usETqqErIMhfckr5lTZnbPxqPMXT9J8i7w3iW1IbAqG_OqlVafRvqD3zmaxjTX4DJKWej5xqMgjm4GF1aPQ4NZEf_P5Qi731TCIqgu-qzWf-ZJ22vyBySw.xP9nojMKbgmJ21jCjSVP8AVrfSo50HixRDnGxMgxnu8&dib_tag=se&keywords=cross%2Bbody%2Bbag%2Bfor%2Bmen&qid=1723814270&sprefix=cross%2Bbody%2Bbag%2Bfor%2Bmen%2Caps%2C274&sr=8-2&th=1'
product_data = scrape_amazon(url)
print(product_data)