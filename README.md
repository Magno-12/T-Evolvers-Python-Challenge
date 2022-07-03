# T-Evolvers-Python-Challenge

## Requirements
This project consists of simulating a sensor, which is an electronic device that sends random data in a range between 10 and 100 with 
python, using an activator to start measuring or in this case send data.
##

## Minimum requirements for a machine:
1. Python and Flask Installed in your machine
2. Windows 10 or superior or Linux (ubuntu,debian,mint,etc)
3. Visual Studio Code
4. Virtual enviroment

## Development architecture
![image](https://user-images.githubusercontent.com/66977118/177058345-91a8fda3-9deb-464b-b472-81c5788b1dc2.png)

## API usage

The models of the database are for the moment: id, metrics, device id and timestamp, these will be the data that is sent from the application, those used for proper operation are and complete the concept of crud:

- GET event/ We use it to define the structure and what type of data should reach each of the elements: Id is numeric, this is assigned by the database since it is a primary key, the device id is an alphanumeric value that is assigned each time the program runs, the metric is a random number between 10 and 100 and the time it takes for the current time.
parameters: 'id'
            'device_id'
            'metric'
            'timestamp'

- POST event/ a data parse is made to ensure that the arguments are correct and generate the enevto in the database (saved).
parameters: 'device_id'
            'metric'
            'timestamp'
            
- PUT event/ update object stored in database after being generated.

- DELETE event/ delete record from database

## Responses usage
- 200 The request succeeded. 
- 400 The server cannot or will not process the request due to something that is perceived to be a client error. 

# EXECUTION OF THE PROGRAM

1. $ git clone https://github.com/Magno-12/T-Evolvers-Python-Challenge
2. install virtual enviroment: $ pip install virtualenv env
3. activate the virtual environment: $ cd ./env/Scripts/source activate (this is in gitbash)
4. install requirements file (env)$ pip install -r requirements.txt

5. run flask server side
6. Run development server (env)$ cd ./T-Evolvers/server/export FLASK_ENV=development
7. Run server (env)$ cd t-evolvers/server/python run.py
       
8. run flask client side
9. (env)$ cd ./T-Evolvers/client/python simulator.py

## Client program interface

![image](https://user-images.githubusercontent.com/66977118/177061023-867a8eb8-990f-4787-9d6a-a25f59bd2328.png)

![image](https://user-images.githubusercontent.com/66977118/177061063-e1f98114-9f6d-47d4-913e-24b9621b5aad.png)
