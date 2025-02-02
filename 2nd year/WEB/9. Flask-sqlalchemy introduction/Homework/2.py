global_init(input().strip())
db_sess = create_session()
users = db_sess.query(User).filter((User.position.like('%chief%')) | (User.position.like('%middle%'))).all()
[print(item + item.position) for item in users]