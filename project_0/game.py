import numpy as np
    
def random_predict(number: int = 1) -> int:
    count = 0
    min = 1
    max = 101
    
    while True:
        count += 1
        predict_number = np.random.randint(min, max)
        if number == predict_number:
            break  
        elif number > predict_number:
            min = predict_number
        elif number < predict_number:
            max = predict_number
    
    return count

count_ls = []
random_array = np.random.randint(1, 101, size=(10)) 

for number in random_array:
    count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

print(count_ls)