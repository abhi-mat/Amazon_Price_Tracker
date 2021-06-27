import bs4
import urllib.request
import smtplib
import time

prices_list = []

def check_price():
    url = 'https://www.amazon.in/Silver-Storage-Additional-Exchange-Offers/dp/B08LRDK8Z5/ref=sr_1_1_sspa?crid=3CI8ZMCSPKM10&dchild=1&keywords=redmi+note+10+pro+%2B&qid=1624808415&sprefix=redmi+%2Caps%2C345&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzSTBDVDVUVDZCUlEmZW5jcnlwdGVkSWQ9QTAyNTQyNDAzNDdGUEU1QzJIRjNLJmVuY3J5cHRlZEFkSWQ9QTA1NjAxNjEzS0ZSSDRZQ000SzNLJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

    sauce = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(sauce, "html.parser")

    prices = soup.find(id="priceblock_ourprice_row").get_text()
    prices = float(prices.replace(",", "").replace("₹", ""))
    prices_list.append(prices)
    return prices

def send_email(message, sender_email, sender_password, receiver_email):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email, sender_password)
    s.sendmail(sender_email, receiver_email, message)
    s.quit()

def price_decrease_check(price_list):
    if prices_list[-1] < prices_list[-2]:
        return True
    else:
        return False

count = 1
while True:
    current_price = check_price()
    if count > 1:
        flag = price_decrease_check(prices_list)
        if flag:
            decrease = prices_list[-1] - prices_list[-2]
            message = f"The price has decrease please check the item. The price decrease by {decrease} rupees."
            send_email(message,test1@gmail.com,1234,test3@gmail.com) 
    time.sleep(43000)
    count += 1