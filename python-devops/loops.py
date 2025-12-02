start_point = 1
finish_point = 10
#current_point = start_point
sum_=0

while start_point <= finish_point:
    print(f'Current Point: {start_point}')
    sum_ += start_point
    start_point += 1

print(f'Sum: {sum_}')
