class _FakeJobs(Jobs):
    def __repr__(self):
        return '<Job>' + self.job
    

Jobs = _FakeJobs
global_init(input().strip())
db_sess = create_session()
users = db_sess.query(Jobs).filter(Jobs.work_size < 20, not Jobs.is_finished).all()
[print(item) for item in users]