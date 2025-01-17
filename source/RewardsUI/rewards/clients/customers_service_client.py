import requests
import json

class CustomersServiceClient:

    def __init__(self):
        self.get_customer_url = "http://rewardsservice:7050/customer/"
        self.get_all_customers_url = "http://rewardsservice:7050/customers/"
        self.process_order_url = "http://rewardsservice:7050/processOrder/"

    def get_all_customers(self):
        response = requests.get(self.get_all_customers_url)
        return response.json()

    def process_order(self, emailPassed, order_totalPassed):
        response = requests.post(self.process_order_url, params={
                                 "email": emailPassed, "order_total": order_totalPassed})
        return response.json()