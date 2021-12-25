"""Modules"""
import sys
import unittest
sys.path.insert(0, './src')
from services.main_service import MainClass

class TestMainClass(unittest.TestCase):
    """Testing the main class"""
    def setUp(self):
        """Setup"""
        print("Set up goes here")

    def test_store_topics(self):
        """Store topics test"""
        self.assertEqual(MainClass.store_topics(TestMainClass, items=["a"]), None)

    def test_db_operations(self):
        """Database operations test"""
        self.assertEqual(MainClass.db_operations(TestMainClass, topics=[]), None)

    def test_print_topics(self):
        """Test printing topics from db"""
        self.assertEqual(MainClass.print_topics(TestMainClass), None)
