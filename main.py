# importing libraries
from flask import Flask, request, render_template, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app) # instantiate the mail class

# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'chepurivarun10@gmail.com'
app.config['MAIL_PASSWORD'] = 'wizxqzixnfjhivzq'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# message object mapped to a particular URL ‘/’

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route("/email", methods=['GET'])
def index():
    receipent = request.args.get('email')
    msg = Message(
				'Emergency Alert',
				sender ='chepurivarun10@gmail.com',
				recipients = [receipent]
			)
    msg.body = 'person has fell down'
    mail.send(msg)
    return 'Sent'

if __name__ == '__main__':
    app.run(debug = True)
