### Process of deploying my python app to AWS

1. mkdir
2. navigate to the directory
3. create a virtual environment (python3-m venv venv | source venv/bin/activate)
4. Install flask (pip install flask)
5. Create the python file.
6. Create a requirement file .txt
7. Create a file named ".ebetensions/python.config”

## Set up AWS Elastic Beanstalk
1. install AWS CLI
2. configure AWS CLI (aws configure)
3. install elastic beanstalk CLI ﻿
4. initialize your elastic beanstalk app ( eb init -p python-3.8 myPythonApp)

## Create an environment and deploy
1. eb create myPythonEnv
2. eb open

## Updating the App
1. make changes to application.py
2. deploy updates (eb deploy)

Clean up
1. After testing use (eb terminate myPythonEnv) to terminate
