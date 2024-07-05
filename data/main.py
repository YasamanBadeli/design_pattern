from src import Student
from src.Data_loader import DataLoader


def print_data(data):
    #print all instances returned by data_loader
    for item in data:
        print(item)
def main():
    data_loader = DataLoader(new_id=1, data_path='')
    print(f'DataLoader ID: {data_loader.id}')
    # load students from file using the data_loader instance
    students = data_loader.read_data_from_file(file_name = 'students.txt', obj_type=Student)
    print_data(students)

    # create a new DataLoader : checking if it is a new instance or not
    new_data_loader = DataLoader(new_id=2, data_path='')
    print(f'DataLoader ID: {new_data_loader.id}')
    students = new_data_loader.read_data_from_file(file_name = 'students.txt', obj_type=Student)
    print_data(students)


if __name__ == "__main__":
    main()