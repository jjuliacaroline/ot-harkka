"""Modules"""
import unittest
from services.main_service import MainClass

class TestMainClass(unittest.TestCase):
    """Testing the main class"""
    def setUp(self):
        """Setup"""
        print("Set up goes here")

    def test_store_topics(self):
        """Store topics test"""
        output = MainClass.store_topics(self=MainClass, items=["a"])
        self.assertEqual(output, None)
    