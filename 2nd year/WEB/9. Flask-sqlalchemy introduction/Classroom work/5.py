global_init(input().strip())
db_sess = create_session()
users = db_sess.query(User).filter(User.address == 'module_1').all()
[print(item) for item in users]