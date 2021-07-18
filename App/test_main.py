import unittest as ut

import requests

from main import driver_function, get_urls


class TestKogan(ut.TestCase):
    def setUp(self) -> None:
        pass

    def test_process(self):
        urls = get_urls()
        answer = driver_function(urls, "Air Conditioners")
        print(answer)







