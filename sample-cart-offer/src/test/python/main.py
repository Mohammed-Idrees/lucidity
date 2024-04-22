import unittest
from unittest.mock import patch
from zomato import Zomato


class TestZomato(unittest.TestCase):
    def test_add_offer_p1(self):
        z = Zomato()
        response = z.add_offer(1, "FLATX", 10, ["p1"])
        self.assertEqual(response, {"response_msg": "success"})

    def test_add_offer_p2(self):
        z = Zomato()
        response = z.add_offer(2, "FLATX", 10, ["p2"])
        self.assertEqual(response, {"response_msg": "success"})

    def test_add_offer_p3(self):
        z = Zomato()
        response = z.add_offer(3, "FLATX%", 10, ["p3"])
        self.assertEqual(response, {"response_msg": "success"})

    @patch('requests.get')
    def test_apply_offer_p1(self, mock_get):
        mock_get.return_value.json.return_value = {"segment": "p1"}
        z = Zomato()
        response = z.apply_offer(200, 1, 1)
        self.assertEqual(response, {"cart_value": 190})

    @patch('requests.get')
    def test_apply_offer_p2(self, mock_get):
        mock_get.return_value.json.return_value = {"segment": "p2"}
        z = Zomato()
        response = z.apply_offer(200, 1, 1)
        self.assertEqual(response, {"cart_value": 190})

    @patch('requests.get')
    def test_apply_offer_p3(self, mock_get):
        mock_get.return_value.json.return_value = {"segment": "p3"}
        z = Zomato()
        response = z.apply_offer(200, 1, 1)
        self.assertEqual(response, {"cart_value": 190})

    @patch('requests.get')
    def test_apply_offer_negative(self, mock_get):
        mock_get.return_value.json.return_value = {"segment": "p1"}
        z = Zomato()
        response = z.apply_offer(300, 1, 1)
        self.assertEqual(response, {"cart_value": 290})


if __name__ == '__main__':
    unittest.main()
