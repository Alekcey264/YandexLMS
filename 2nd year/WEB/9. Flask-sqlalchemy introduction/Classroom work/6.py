global_init(input().strip())
db_sess = create_session()
users = db_sess.query(User).filter(User.address == 'module_1', 
                                   User.position.notlike('%engineer%'), 
                                   User.speciality.notlike('%engineer%')).all()
[print(item.id) for item in users]