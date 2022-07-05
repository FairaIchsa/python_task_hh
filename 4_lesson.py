# написать функцию, которая получает на вход словарь с интервалами
# и возвращает время общего присутствия ученика и учителя на уроке (в секундах)
def intersection(timestamp):
    lesson = timestamp['lesson']
    tutor = timestamp['tutor']
    pupil = timestamp['pupil']

    intersections = []
    i = 0
    j = 0

    while i < len(tutor) and j < len(pupil):
        interval = (max(tutor[i][0], pupil[j][0]), min(tutor[i][1], pupil[j][1]))
        if interval[0] < interval[1]:
            intersections.append(interval)
        if tutor[i][1] < pupil[j][1]:
            i += 1
        else:
            j += 1

    if not intersections:
        return []

    while lesson[0] >= intersections[0][1]:
        intersections.pop(0)
    if not intersections:
        return []
    intersections[0] = (max(lesson[0], intersections[0][0]), intersections[0][1])

    while lesson[1] <= intersections[-1][0]:
        intersections.pop()
    if not intersections:
        return []
    intersections[-1] = (intersections[-1][0], min(lesson[1], intersections[-1][1]))

    return intersections


time = {
    'lesson': (3, 12),
    'tutor': [(1, 5), (6, 9), (10, 16)],
    'pupil': [(1, 2), (3, 5), (6, 11), (12, 15)]
}
print(intersection(time))
