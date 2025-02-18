global_init(input().strip())
db_sess = create_session()
users = db_sess.query(User).filter(User.address == 'module_1', User.age < 21).all()
for item in users:
    item.address = 'module_3'
db_sess.commit()