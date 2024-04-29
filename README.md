# 220-Project
## Github CI/CD
## Overview

Contributors: Louis Spann & Madison Myers

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
