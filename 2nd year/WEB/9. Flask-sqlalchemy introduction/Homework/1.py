global_init(input().strip())
db_sess = create_session()
users = db_sess.query(User).filter(User.age < 18).all()
for item in users:
    print(item, end=' ')
    print(str(item.age) + ' years')