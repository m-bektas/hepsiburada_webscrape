from bs4 import BeautifulSoup
import urllib.request
import mysql.connector
import time

time.sleep(10)

"""
From the given links finds the names, images and prices of the products and stores them in the ProductTable
"""
# get url's from the file
linkfile = open("links.txt", "r")
links = linkfile.read().split(',')

# configuration for database login information
config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'Products'
}

# connect to database
mydb = mysql.connector.connect(**config)

mycursor = mydb.cursor()

for link in links:
    # read url
    url = link
    url_read = urllib.request.urlopen(url)
    soup = BeautifulSoup(url_read, 'html.parser')

    # get product-image class
    image_cls = soup.find('img', attrs={'class': 'product-image'})

    # get product image
    image_split = image_cls["data-cloudzoom"].split("'")
    product_image = image_split[1]

    # get product name
    product_name = image_cls["alt"]

    # get product price
    product_price = soup.find('span', attrs={'class': 'price'})['content']

    # add the info to the table as a new row
    sql = 'INSERT INTO ProductTable (name, image, price) VALUES (%s, %s, %s)'
    val = (product_name, product_image, product_price)
    mycursor.execute(sql, val)

    mydb.commit()

    print("1 record inserted, ID:", mycursor.lastrowid)

mycursor.close()
mydb.close()
