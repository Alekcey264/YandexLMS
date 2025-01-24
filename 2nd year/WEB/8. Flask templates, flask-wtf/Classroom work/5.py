from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from conf import config_key

app = Flask(__name__)
app.config['SECRET_KEY'] = config_key


class LoginForm(FlaskForm):
    user_id = StringField('ID астронавта', validators=[DataRequired()])
    user_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    captain_id = StringField('ID капитана', validators=[DataRequired()])
    captain_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Войти')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('success')
    return render_template('5.html', title='Панель аварийного доступа', form=form)


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == "__main__":
    app.run(host='localhost', port=8080)