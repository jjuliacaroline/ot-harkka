"""Modules"""
import sqlite3

connection = sqlite3.connect("news.db")

def get_database_connection():
    """Initialized connection to the database"""
    return connection
