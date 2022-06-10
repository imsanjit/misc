import requests
from bs4 import BeautifulSoup
import csv

csv_file = open('Image_Details.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['URL', 'Image_Details'])

url_in=input('Kindly Enter a url or list of urls sepatared by commams:  ').split(sep=' ')

for i, x in enumerate(url_in):
    print(f'Working on url :{i + 1} : {x}')
    response = requests.get(x)
    if response.status_code == 200:
        try:
            html_soup = BeautifulSoup(response.text, 'html.parser')
            cont = html_soup.find("div", {"class":["primary-content-section", "product-content", "bank-prod-page"]})
            list_img = []
            for img in cont.findAll('img'):
                list_img.append(img)
            csv_writer.writerow([x, list_img])
        except:
            pass


csv_file.close()
print('ALL DONE. Download your file....')
