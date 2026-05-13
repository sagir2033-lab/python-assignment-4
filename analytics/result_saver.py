import json

class ResultSaver:
    def __init__(self, result, filename):
        self.result = result
        self.filename = filename

    def save_json(self):
        with open(self.filename, 'w') as file:
            json.dump(self.result, file, indent=4)

        print(f"Result saved to {self.filename}")