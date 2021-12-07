import sys
sys.path.insert(0, './src')
from main_service import MainClass as logic
from ui import create_ui

class Harkkatyo:
    def main():
        topics = logic.get_topics(self=logic)
        logic.db_operations(topics)
        create_ui.main_loop(topics)

Harkkatyo.main()
