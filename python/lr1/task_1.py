numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
len_ = len(numbers)
numbers2 = numbers[:4] + numbers[5:]
sum_ = sum(numbers2)
none_ = sum_/len_
numbers[4]=none_
print("Измененный список:", numbers)
