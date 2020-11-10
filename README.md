# HOME AUTOMATION

### Description:
This is a small application that can help to set up light and temperature controller automatically.


### Instruction

1. Create environment:

`sudo apt update`

`sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools`

`python3 -m venv project`

`source project/bin/activate`

2. Install dependencies:

Make sure you are in project directory and run

`pip install -m requirement.txt`

3. Set up database:

Make sure you comment out 2 lines in api/apis.py

`from models.light import Light`

`from models.air_conditioner import AirC`

and run this script

`python3 - m setup_table_database`

Then, please bring 2 lines above back when you done.

4. Run the app:

Open a terminal and run:

`python3 -m run`

Open another terminal and run controller:

`python3 -m home_automation_controller`

The app will read the current light and temperature every 5 seconds then check current light and ac objects; if it request to change the current status, it will return a proper value and update new condition in database, otherwise it does nothing.

5. For debuging, please import Postman collection from the link 
`https://www.getpostman.com/collections/23fbb9402a2bdb6cf54c` to connect application server