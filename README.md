# Hepsiburada Web Scraper

Scraping hepsiburada.com products. This is a small project I did for my job interview. 

### Prerequisites

* A working PC
* Docker Desktop
* MySQL

### Installing and Initialization

* Copy-paste the links of the products you want to scrape to hbapp/app/links.txt. Separate them with a comma(,).

### Usage

* Open your terminal and go to the project folder, then just type: 

```
$ docker-compose up
```

The program will add the names, images and prices of the products to a table called ProductTable in a MySQL database called Products.

* If you want to see the table in the database, open up another terminal and type ```$ docker exec -it hbapp_db_1 mysql -uroot -p```, then enter the password ```root```. Then type these:

* ```use Products```,

* ```SELECT * FROM ProductTable```

## Troubleshooting

* In case you can't see Turkish characters when inspecting the MySQL table, copy and paste this in mysql console:

```
SET NAMES utf8mb4 COLLATE utf8mb4_turkish_ci;
```
