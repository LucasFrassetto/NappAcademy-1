class FileHandler():
    def __init__(self, file_name, file_mode):
        self._file_name = file_name
        self._file_mode = file_mode

    def __enter__(self):
        self._file = open(self._file_name, self._file_mode)
        return self._file

    def __exit__(self, exc_type,exc_value, exc_traceback):
        self._file.close()


if __name__ == "__main__": 
    with FileHandler('cm1.txt', 'w') as f:
        f.write('Test')