global_init(input().strip())
db_sess = create_session()
users = db_sess.query(Jobs).filter(Jobs.work_size < 20, not Jobs.is_finished).all()
[print(f'<Job> {item.job}') for item in users]