def get_names(*names):
    antwort = "Names:\n"
    print(type(names))
    for i in range(len(names)):
        antwort = antwort + f'{i+1} {names[i]} \n'
    return antwort
print(get_names("Abdullah", "Ali", "Alena", "Maria"))