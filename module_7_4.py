team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'


def challenge_result_2():
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды Волшебники Данных!'
    else:
        result = 'Ничья!'
    return result


def tasks_total_2():
    return score_1 + score_2


def time_avg_2():
    return (team1_time + team2_time) // tasks_total_2()


print('В команде Мастера кода участников: %(team1_num)s!' % {'team1_num': team1_num})
print('Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s!' % {'team1_num': team1_num,
                                                                               'team2_num': team2_num})
print('Команда Волшебники данных решила задач: {score_2}!'.format(score_2=score_2))
print('Команда Волшебники данных решила задач: {team1_time} c!'.format(team1_time=team1_time))
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Результат битвы: {challenge_result_2()}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
print(f'Сегодня было решено {tasks_total_2()} задач, в среднем по {time_avg_2()} секунды на задачу!')
