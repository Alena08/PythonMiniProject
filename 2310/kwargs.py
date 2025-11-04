def print_info(name,age):
    print(name, age)

def get_infos(**person):
    for key,value in person.items():
        print(f'{key}, {value}')

get_infos(name="ali", age = 30)
