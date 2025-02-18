global_init(input().strip())
db_sess = create_session()
jobs = db_sess.query(Jobs).all()
jobs = [(item.team_leader, len(item.collaborators.split(', '))) for item in jobs]
jobs.sort(key=lambda x: -x[1])
max_len = jobs[0][1]
jobs = [item[0] for item in jobs if item[1] == max_len]
unique = []
for item in jobs:
    if item not in unique:
        unique.append(item)
for item in unique:
    lead = str(db_sess.query(User).filter(User.id == item).all()[0]).split()
    print(lead[-1], lead[-2], sep=' ')