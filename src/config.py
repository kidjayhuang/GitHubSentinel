import json
import os
class Config:
    def __init__(self):
        self.load_config()
    
    def load_config(self):
        # current_dir = os.path.dirname(os.path.abspath(__file__))
        # with open(os.path.join(current_dir, '../config.json'), 'r') as f:
        with open('config.json', 'r') as f:
            config = json.load(f)
            self.github_token = os.getenv('GITHUB_TOKEN')
            self.notification_settings = config.get('notification_settings')
            self.subscriptions_file = config.get('subscriptions_file')
            self.update_interval = config.get('update_interval', 24 * 60 * 60)  # Default to 24 hours
