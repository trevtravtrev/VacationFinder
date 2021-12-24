
class TextFile:
    def __init__(self, text_file):
        self.file = text_file

    def write_file(self, data):
        with open(self.file, 'w') as file:
            file.write(data)

    def read_file(self):
        try:
            with open(self.file, 'r') as file:
                return int(file.read())
        except FileNotFoundError as e:
            print(f'read_file error: {e}')
            return None
