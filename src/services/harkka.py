import sys
sys.path.insert(0, './src')
from services.main_service import MainClass as logic
from ui import create_ui

class Harkkatyo:
    """Main class"""
    def main(self):
        """Main loop for running the application"""
        topics = logic.get_topics(self=logic)
        logic.db_operations(logic, topics)
        create_ui.main_loop(topics)

Harkkatyo.main(self=Harkkatyo)
