def configure_printer(**settings):
    print("Settings: ")
    for key,value in settings.items():
        print(f'{key}: {value}')

configure_printer(papierformate = "A4", duplex = False, farbe = True, qualitaet = "normal")


