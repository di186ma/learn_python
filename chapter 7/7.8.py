# убрать наименьшую оценки и посчитать новое среднее значение с -1 элементом

def main():
    scores = [7, 9, 6, 12, 6, 2, 9, 3]
    total = sum_scores(scores)
    lowest = min(scores)
    total -= lowest
    average = total / (len(scores) - 1)
    print('The average score is:', average)

def sum_scores(scores):
    total = 0
    for score in scores:
        total += score
    return total

if __name__ == '__main__':
    main()