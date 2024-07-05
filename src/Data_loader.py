"""class DataLoader: # normall version of proj not singlton

  def __init__(self, new_id, data_path=None):
     self.id = new_id
     self.data_path = data_path

  def read_data_from_file(self, file_name: str, obj_type: Any):
    objects = []
    file_path = self.data_path + '/' + file_name \
        if self.data_path else file_name

      #  if self.data_path:
      #      file_path = self.data_path + '/' + file_name
      #  else:
      #      file_path = file_name

    with open(file_path, 'r') as file:
        for line in file:
            attributes = line.strip().split(', ')
            # dynamically creat an object of obj_type
            obj = obj_type(*attributes)
            objects.append(obj)
    return objects
"""
from typing import Any
import threading

class DataLoader:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, new_id, data_path=None):
        with cls._lock:
            if cls._instance is None:
                # Create a new instance of DataLoader
                cls._instance = super(DataLoader, cls).__new__(cls)
        return cls._instance

    def __init__(self, new_id, data_path=None):
        if not hasattr(self, '_initialized'):
            self._initialized = True
            self.id = new_id
            self.data_path = data_path
        else:
            print(f'Warning: DataLoader class is singleton, your request is denied.')

    def read_data_from_file(self, file_name: str, obj_type: Any):
        objects = []
        file_path = f"{self.data_path}/{file_name}" if self.data_path else file_name

        try:
            with open(file_path, 'r') as file:
                for line in file:
                    attributes = line.strip().split(', ')
                    # Dynamically create an object of obj_type
                    obj = obj_type(*attributes)
                    objects.append(obj)
        except FileNotFoundError:
            print(f"File {file_name} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

        return objects