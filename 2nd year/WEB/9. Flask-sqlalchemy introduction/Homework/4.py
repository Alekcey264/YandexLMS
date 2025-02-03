global_init(input().strip())
db_sess = create_session()
jobs = db_sess.query(Jobs).all()
jobs = [(item.team_leader, len(item.collaborators.split(', '))) for item in jobs]
jobs.sort(key=lambda x: x[1])
max_len = jobs[0][1]
jobs = list(filter(lambda x: x[1] == max_len, jobs))
for item in jobs:
    leader = db_sess.query(User).filter(User.id == item[0]).first()
    print(leader.name, leader.surname)

