import os
from appmodule import BaseModule
import json


class FileModule(BaseModule):
    def run(self):
        self.output = FileModule.get_info()

    def get_info():
        try:
            files=[]
            counter = 0
            print("If you want all the excel file, for example write .xlsx")
            for r, d, f in os.walk("C:\\"):
                for file in f:
                    filepath = os.path.join(r, file)
                    counter += 1
                    files.append(filepath)
                    if counter == 2000:
                        break
            return json.dumps(files)
        except Exception as e:
            pass

def get_module():
    return FileModule