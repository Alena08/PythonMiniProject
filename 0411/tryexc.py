import logging

values = [10,4,6,2,0,"ALI",8,9]

for value in values:
    try:
        print(10/int(value))
        #raise AttributeError
    # except (ZeroDivisionError,ValueError) as e:
    #     print(f"Error: {str(e)}")
    #     #print("Error occured!!")
    # except AttributeError as e:
    #     print(f"Error: {str(e)}")
    except Exception as e:
        logging.exception(e)
        #print(f"Error: {str(e)}")
    else:
        print("no exception")
    finally:
        print("Hallo BBQ")

print("Hello")