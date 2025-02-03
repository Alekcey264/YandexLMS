import datetime
import sqlalchemy


class Jobs(SqlAlchemyBase): # type: ignore
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    leader = sqlalchemy.orm.relationship('User')
    job = sqlalchemy.Column(sqlalchemy.String)
    work_size = sqlalchemy.Column(sqlalchemy.Integer)
    collaborators = sqlalchemy.Column(sqlalchemy.String)
    start_date = sqlalchemy.Column(sqlalchemy.Date, default=datetime.date.today)
    end_date = sqlalchemy.Column(sqlalchemy.Date, default=datetime.date.today)    
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean)