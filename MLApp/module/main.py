from flask import Flask
from app import views
app = Flask(__name__)

# url
app.add_url_rule('/base', 'base', views.base)
app.add_url_rule('/', 'index', views.index)
app.add_url_rule('/gender', 'gender', views.gender)
app.add_url_rule('/gender/genderModel', 'genderModel',
                 views.genderModel, methods=['GET', 'POST'])

# run
if __name__ == "__main__":
    app.run(debug=True)
