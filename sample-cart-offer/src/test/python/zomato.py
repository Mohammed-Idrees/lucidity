import requests
import json

class Zomato:
    def __init__(self):
        self.base_url = "http://localhost:9001/api/v1/"  # Assuming local host

    def add_offer(self, restaurant_id, offer_type, offer_value, customer_segment):
        url = self.base_url + "offer"
        payload = {
            "restaurant_id": restaurant_id,
            "offer_type": offer_type,
            "offer_value": offer_value,
            "customer_segment": customer_segment
        }
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url, data=json.dumps(payload), headers=headers)
        return response.json()

    def apply_offer(self, cart_value, user_id, restaurant_id):
        url = self.base_url + "cart/apply_offer"
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "cart_value": cart_value,
            "user_id": user_id,
            "restaurant_id": restaurant_id
        }

        response = requests.post(url, data=json.dumps(payload), headers=headers)
        return response.json()

    def get_user_segment(self, user_id):
        url = self.base_url + "user_segment"
        params = {
            "user_id": user_id
        }

        response = requests.get(url, params=params)
        return response.json()
