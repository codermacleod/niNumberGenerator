import rstr


def create_ni_number():
    ni = rstr.xeger(r'[A-Z]{2}[0-9]{6}[A-Z]')
    return ni


def create_ni_number_file():
    file_object = open('ni_number_list.txt', 'a')
    for i in range(1000):
        file_object.write(create_ni_number() + '\n')
    file_object.close()


create_ni_number_file()
