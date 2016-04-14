from unittest import TestCase
from driver import Driver


class TestDriver(TestCase):

    def test_do_some(self):
		driver = Driver()
		result = driver.do_some()
		self.assertIsNotNone(result)
		