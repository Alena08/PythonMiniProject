def get_sum_avg(*marks):
    sum = 0
    counter = 0
    for mark in marks:
        sum += mark
        counter +=1
    avg = sum/counter
    return f'SUMME: {sum}\nAVG: {avg:.2f}'
print(get_sum_avg(60,80,95,56,77,84,97))

# Sum: ....
# Avg: ...