from data import db_session
from data.jobs import Jobs
from data.users import User
from random import randint, choice
from string import ascii_lowercase
import datetime


def generate_user() -> User:
    user = User()
    user.surname = ''.join([choice(ascii_lowercase) for _ in range(3, 10)]).capitalize()
    user.name = ''.join([choice(ascii_lowercase) for _ in range(3, 10)]).capitalize()
    user.age = randint(18, 50)
    user.position = 'colonist'
    user.speciality = 'engineer'
    user.address = 'module_' + str(randint(1, 5))
    user.email = (user.surname + '_' + user.position + '@mars.org').lower()
    user.set_password(''.join([choice(ascii_lowercase) for _ in range(3, 10)]))
    return user


def main():
    db_session.global_init('db/planet.db')
    db_sess = db_session.create_session()
    # Добавляем капитана
    captain = User()
    captain.surname = 'Scott'
    captain.name = 'Ridley'
    captain.age = 21
    captain.position = 'captain'
    captain.speciality = 'research engineer'
    captain.address = 'module_1'
    captain.email = 'scott_chief@mars.org'
    captain.set_password('123')
    db_sess.add(captain)
    db_sess.commit()
    # Добавляем колонистов
    for _ in range(5):
        db_sess.add(generate_user())
        db_sess.commit()

    # Добавляем работу
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborations = '2, 3'
    job.start_date = datetime.date.today()
    job.is_finished = False
    db_sess.add(job)
    db_sess.commit()


if __name__ == '__main__':
    main()