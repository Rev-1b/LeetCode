def data_merge(dataset: list[list[str]]) -> list[tuple[int, str]]:
    result = []
    for cluster in dataset:
        if not result:
            for node in cluster:
                date1, info1 = node.split(' ', 1)
                result.append((int(date1), info1))

        else:
            for node in cluster:
                date, info = node.split(' ', 1)
                date = int(date)
                if date <= result[0][0]:
                    result.insert(0, (date, info))

                if date >= result[-1][0]:
                    result.append((date, info))

                start, end = 0, len(result) - 1
                while start <= end:
                    mid = (start + end) // 2
                    if result[mid - 1][0] < date <= result[mid][0]:
                        result.insert(mid, (date, info))
                        break
                    elif result[mid][0] > date and result[mid - 1][0] > date:
                        end = mid - 1
                    else:
                        start = mid + 1
    return result


dataset = [
    [
        '1 amogus super',
        '7 amogus super',
        '13 amogus super',
        '27 amogus super',
        '29 amogus super',
        '54 amogus super',
        '96 amogus super'
    ],
    [
        '2 amogus super',
        '5 amogus super',
        '10 amogus super',
        '23 amogus super',
        '34 amogus super',
        '51 amogus super',
        '87 amogus super'
    ]
]

if __name__ == '__main__':
    for elem in data_merge(dataset):
        print(elem)
