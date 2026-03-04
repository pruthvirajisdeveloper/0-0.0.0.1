from modules.manager import Manager
if __name__ == "__main__":
    manager=Manager()
    manager.new_student()
    print(manager.get_id_card())
    print('\n\nthis is a list of all student:', manager.list_all_students())