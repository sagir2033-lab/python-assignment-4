import csv

class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        with open(self.filename, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            self.students = list(reader)

    def preview(self):
        print("Preview:")
        for student in self.students[:5]:
            print(student)