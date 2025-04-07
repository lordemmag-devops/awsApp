from flask import Flask

application = Flask(__name__) # 'application' is required by Elastic Beanstalk

@application.route('/')
def home():
    return "Hello, AWS from Flask!"

if __name__ == '__main__':
    application.run(debug=True)