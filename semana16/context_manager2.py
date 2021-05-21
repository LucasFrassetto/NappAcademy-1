import contextlib

@contextlib.contextmanager
def file_handler(file_name,file_mode):
    file = open(file_name,file_mode)
    yield file
    file.close()

if __name__ == "__main__":
   with file_handler("cm2.txt","w") as f:
       f.write("Test")
