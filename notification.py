from smtplib import SMTP_SSL, SMTP
from dotenv import load_dotenv
import os
from data_manager import DataManager
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

class Notification:
    def __init__(self):
        self.scraped_data = DataManager()
        self.scrape_title = self.scraped_data.title
        self.scrape_total_value = self.scraped_data.total_amount

    def send(self):
        my_email = os.getenv("EMAIL")
        my_app_password = os.getenv("PASSWORD")
        dest_email = os.getenv("TO")

        if None in [my_email, my_app_password, dest_email]:
            print("make sure you have your EMAIL, APP PASSWORD, and DESTINATION EMAIL and try again")
            return None

        msg = MIMEMultipart()
        msg["From"] = my_email
        msg["To"] = dest_email
        msg["Subject"] = "Amazon Price Alert!"

        body = f"{self.scrape_title}. The price is now "\
               f"${self.scrape_total_value}\n\n{self.scraped_data.amazon_url}"

        msg.attach(MIMEText(body, "plain", "utf-8"))

        with SMTP(host="smtp.gmail.com", port=587) as connection:
            print("sending...")
            connection.starttls()
            connection.ehlo()
            connection.login(user=my_email, password=my_app_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=dest_email,
                msg=msg.as_string()
            )
