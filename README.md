# 220-Project
## Github CI/CD
## Overview
Our project implements Continuous Integration (CI) and mostly implements Continuous Delivery (CD) using the web_counter application. The CI runs tests for functionally and correct formatting. The CD then the CD part should deploy the application into a EC2 Instance. Unfortunately, we have the CD connected into a EC2 instance, but we didn't get to the point where web_counter would be up and running on the EC2 instance. The test.py is used for general testing of the CI/CD process, but the rest of the file besides the workflows are the same. For this project, we also learned how to the password manager Github has called secrets. We made two secrets for this project called EC2_PUBLIC_ADDRESS and LABUSERPEM. The LABUSERPEM is hiding the private IP address, so that it's not in our code publicly. We used EC2_PUBLIC_ADDRESS because it's easier to update the public EC2 IP from secrets than in the code for the CD workflow. 

Contributors: Louis Spann & Madison Myers

## UML Diagram 

![demo  CICD merge with main and doing pull request to show that the tests are running (2)](https://github.com/cs220s24/Louis-Madison--Github-CI-CD/assets/143567041/37421fd1-16db-4635-a46d-c0a2e7b531a4)





## Setup for local 

1.git clone the web_counter repo
	-cd into repo
 
2. make a vitrual environment
   
3. activate virtual environment
   
4. pip install requirements.txt
   
5. python app.py
   
### For Trouble shooting 
6. make second terminal window
    
7. ssh into instance in new terminal window
    
8. Run this command in the second terminal window
    curl http://localhost:8000
    
9. run Gunicorn command
    gunicorn --bind 0.0.0.0:8000 app:app

11. Open a browser and paste http://localhost:8000

## Setup for AWS
1. make EC2 instance
2. ssh into instance
3. sudo yum install git  
4. git clone the web_counter repo
	-cd into repo
5. make a vitrual environment
6. activate virtual environment
7. pip install requirements.txt
8. python app.py

### For Trouble shooting 
10. make second terminal window
11. ssh into instance in new terminal window 
12. Run this command in the second terminal window
    curl http://localhost:8000
13. Run Gunicorn command
    gunicorn --bind 0.0.0.0:8000 app:app
15. Open a browser and paste http://localhost:8000
