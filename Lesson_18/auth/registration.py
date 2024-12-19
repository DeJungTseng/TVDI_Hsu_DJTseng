from . import auth
from flask import render_template,request,redirect,url_for
from wtforms import EmailField,PasswordField,SubmitField,StringField, validators
from wtforms import StringField,PasswordField,EmailField,validators
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash
from datasource import is_email_duplicate,add_user


class RegistrationForm(FlaskForm):
    username = StringField('使用者名稱',
                           [validators.Length(min=4,max=25),
                           validators.InputRequired("不輸入名字我就叫你「欸」喔")])
    email = EmailField('電子郵件',
                       [validators.Length(min=6, max=35),
                       validators.InputRequired("不輸入電子郵件我就沒辦法聯絡你")])
    password = PasswordField('密碼',
                             [validators.DataRequired("記得設定通關密語啊"),
                             validators.EqualTo("password",
                                              message='密碼不一致')])
    confirm =PasswordField('再次確認密碼',
                           [validators.InputRequired("確認你的通關密語")])


@auth.route('/registration',methods=['GET','POST'])
def registration():
    myForm = RegistrationForm(request.form)
    if request.method=='POST' and myForm.validate():
        name=myForm.username.data
        email=myForm.email.data
        password=myForm.password.data
        password_hash = generate_password_hash(password=password,method='pbkdf2:sha256',salt_length=8)
        print(password_hash)        
        if not is_email_duplicate(email):
            #email沒有重覆
            if add_user(name,email,password_hash):
                return redirect(url_for('auth.success'))
            else:
                print("加入失敗")
        else:
            print('email有重覆')
        return redirect(url_for('auth.success'))
    return render_template('auth/registration.j2',form = myForm)
