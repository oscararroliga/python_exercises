original_list = [['Volkswagen', 'Mercedes', 'BMW'],['Honda', 'Toyota', 'Mazda']]
flattened_list = []

for cars_list in original_list:
    for car in cars_list:
        flattened_list.append(car)

print(flattened_list)

