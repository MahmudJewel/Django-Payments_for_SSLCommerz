# Payment Integrations SSLCOMMERZ
## PIP package
Click [here](https://pypi.org/project/sslcommerz-python/) to install pip package.

## Doc
Click [here](https://developer.sslcommerz.com/doc/v4/#technical-or-backend-integration-process) to read the documents

# Tools
### Back-end
#### Language:
	Python (3.8.6)

#### Frameworks:
	Django(3.2)
	
#### Other libraries / tools:
	python-dotenv==0.21.0
	sslcommerz-python==0.0.7
	
	
### Database:
	SQLite

# Setup
The first thing to do is to clone the repository:
```sh
$ https://github.com/MahmudJewel/Django-Payments_for_SSLCommerz
```
### Back-end
Create a virtual environment to install dependencies in and activate it:
```sh
$ cd Django-Payments_for_SSLCommerz
$ python -m venv venv
$ source venv/bin/activate
```
Then install the dependencies:
```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ python manage.py migrate
(venv)$ python manage.py runserver 8000
```
# ScreenShot
## Home page
![homepage](https://github.com/MahmudJewel/Django-Payments_for_SSLCommerz/blob/main/screenshot/p1.png)

## SSLCOMMERZ integration page
![SSLCOMMERZ](https://github.com/MahmudJewel/Django-Payments_for_SSLCommerz/blob/main/screenshot/p2.png)

## OTP Page
![OTP Page](https://github.com/MahmudJewel/Django-Payments_for_SSLCommerz/blob/main/screenshot/p3.png)

## Success Page
![Success Page](https://github.com/MahmudJewel/Django-Payments_for_SSLCommerz/blob/main/screenshot/p4.png)


# Happy Coding
## From ==> Juwel Mahmud

