already = set()


def pupil_number(surname):
    if surname in log:
        print(log.index(surname) + 1)
    else:
        print("Такого ученика нет.")


def add_pupil(surname):
    if surname in log:
        print("Такой ученик уже есть в журнале.")
    else:
        log.append(surname)
        log.sort()
        print(f"Ученик {surname} добавлен.")


def to_the_blackboard(number):
    if log[number - 1] in already:
        print("Сан Саныч, Вы меня уже вызывали!")
    else:
        print(f"{log[number - 1]}, к доске!")
        already.add(log[number - 1])

log = ['Иванов', 'Кузнецов', 'Петрова']
pupil_number("Петрова")
add_pupil("Смирнов")
add_pupil("Иванов")
to_the_blackboard(4)
add_pupil("Васильев")
pupil_number("Смирнов")
to_the_blackboard(5)