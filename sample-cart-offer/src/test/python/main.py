import unittest
from unittest.mock import patch
from zomato import Zomato


class TestZomato(unittest.TestCase):
    @patch('requests.post')
    def test_add_offer_p1(self, mock_post):
        mock_post.return_value.json.return_value = {"response_msg": "success"}
        z = Zomato()
        response = z.add_offer(1, "FLATX", 10, ["p1"])
        print(response)
        self.assertEqual(response, {"response_msg": "success"})

    @patch('requests.post')
    def test_add_offer_p2(self, mock_post):
        mock_post.return_value.json.return_value = {"response_msg": "success"}
        z = Zomato()
        response = z.add_offer(2, "FLATX", 10, ["p2"])
        print(response)
        self.assertEqual(response, {"response_msg": "success"})

    @patch('requests.post')
    def test_add_offer_p3(self, mock_post):
        mock_post.return_value.json.return_value = {"response_msg": "success"}
        z = Zomato()
        response = z.add_offer(3, "FLATX%", 10, ["p3"])
        print(response)
        self.assertEqual(response, {"response_msg": "success"})

    @patch('requests.post')
    def test_apply_offer_p1(self, mock_post):
        mock_post.return_value.json.return_value = {"cart_value": 190}
        z = Zomato()
        response = z.apply_offer(200, 1, 1)
        print(response)
        self.assertEqual(response, {"cart_value": 190})

    @patch('requests.post')
    def test_apply_offer_p2(self, mock_post):
        mock_post.return_value.json.return_value = {"cart_value": 190}
        z = Zomato()
        response = z.apply_offer(200, 1, 2)
        print(response)
        self.assertEqual(response, {"cart_value": 190})

    @patch('requests.post')
    def test_apply_offer_p3(self, mock_post):
        mock_post.return_value.json.return_value = {"cart_value": 180}
        z = Zomato()
        response = z.apply_offer(200, 1, 3)
        print(response)
        self.assertEqual(response, {"cart_value": 180})


if __name__ == '__main__':
    unittest.main()
