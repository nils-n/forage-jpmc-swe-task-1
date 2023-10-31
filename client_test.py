import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {
                "top_ask": {"price": 121.2, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 121.68, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]
        """ ------------ Add the assertion below ------------ """
        for i, quote in enumerate(quotes):
            stock, bid_price, ask_price, price = getDataPoint(quote)

            self.assertEqual(stock, quotes[i].get("stock"))
            self.assertEqual(ask_price, quotes[i].get("top_ask").get("price"))
            self.assertEqual(bid_price, quotes[i].get("top_bid").get("price"))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {
                "top_ask": {"price": 119.2, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 121.68, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
            {
                "top_ask": {"price": 0.0, "size": 4},
                "timestamp": "2019-02-01 22:06:30.572453",
                "top_bid": {"price": 1.0, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]
        """ ------------ Add the assertion below ------------ """

        expected_ratios = [120.48 / 119.2, 117.87 / 121.68, None]

        for i, quote in enumerate(quotes):
            stock, bid_price, ask_price, price = getDataPoint(quote)
            ratio = getRatio(bid_price, ask_price)
            expected_ratio = expected_ratios[i]

            self.assertEqual(ratio, expected_ratio)

    """ ------------ Add more unit tests ------------ """


if __name__ == "__main__":
    unittest.main()
