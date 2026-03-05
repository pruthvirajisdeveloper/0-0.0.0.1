import json
import os


class JsonDB:
    def __init__(self, filename="db.json"):
        self.filename = filename
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump({}, f)

    def read(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def write(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def insert(self, table, record):
        data = self.read()
        data.setdefault(table, [])
        data[table].append(record)
        self.write(data)

    def get_all(self, table):
        data = self.read()
        return data.get(table, [])
    

    def delete(self, table, key, value):
        data = self.read()
        data[table] = [r for r in data.get(table, []) if r.get(key) != value]
        self.write(data)


    def update(self, table, key, value, new_data):
        data = self.read()
        for record in data.get(table, []):
            if record.get(key) == value:
                record.update(new_data)
        self.write(data)