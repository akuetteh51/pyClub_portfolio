from flask import Flask, render_template, redirect, url_for,session,request
#from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from form import Form
#install Flask-WTF
app = Flask(__name__)


photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'images'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Data.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mysecret'
# db.init_app(app)

configure_uploads(app, photos)

#db = SQLAlchemy(app)
# migrate = Migrate(app, db)

manager = Manager(app)
#manager.add_command('db', MigrateCommand)



@app.route('/')
def profile():
    return render_template('AboutMe.html')

@app.route('/cert')
def cert():
    return render_template('certificates.html')

@app.route('/Mentors')
def Mentors():
    return render_template('Mentors.html')

@app.route('/admin')
def admin():
    return render_template('admin/index.html', admin=True)

@app.route('/admin/add')
def add():
    return render_template('admin/view.html', admin=True)

@app.route('/SignIn',methods=["GET","POST"])
# def signIn():
#     form=signIn()
#     if request.method == "POST":
#         if form.validate == False:
#             return render_template('admin/SignIn.html',signIn=True)
#         else:
#             user=form.Name.Data
#             password=form.password.Data
#             print(user,password)
#                 user=User.query.filter_by(Name=user).first()
#                 if user is not None and user.check_password(password)
#                 session['user']=user.Name
#              return redirect(url_for('admin/view.html', admin=True))
#                 else:
#                     return redirect(url_for(SignIn))
#             elif request.method == 'GET':
#                 return render_template('admin/SignIn.html'form=form,signIn=True)
# @app.route('/SignIn')
def signIn():
    form=Form()
    return render_template('admin/SignIn.html',signIn=True,form=form)

if __name__ == '__main__':
    manager.run()
