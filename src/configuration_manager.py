import os
import sys
import json

class ConfigurationManager:
    def __init__(self, filename):
        self.configuration_filename = filename

    def load_configuration(self):
        with open(os.path.join(sys.path[0], self.configuration_filename)) as f:
            self.configuration = json.load(f)
