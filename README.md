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

`pip install -r requirement.txt`

3. Set up database:

Make sure you comment out 2 lines in api/apis.py

`from models.light import Light`

`from models.air_conditioner import AirC`

and run this script

`python3 setup_table_database.py`

Then, please bring 2 lines above back when you done.

4. Run the app:

Open 1st terminal and run:

`python3 -m run`

5. Open 2nd terminal, initialize light and air conditioner object in database in project env:

`python3 add_light_or_ac.py [option] [arg]`

option: is "light", "ac" or "set_ac".

arg. if light, please give the name (bedroom, living_room) else please give default temperature for ac

light: adding light to system

ac: adding air conditioner to system

set_ac: default set temperature for ac

for example:

`python3 add_light_or_ac.py light bedroom`

`python3 add_light_or_ac.py ac 72`

`python3 add_light_or_ac.py set_ac 68`

6. Stay in 2nd terminal and run controller in project env:

`python3 -m home_automation_controller`

The app will read the current light and temperature every 5 seconds then check current light and ac objects; if it request to change the current status, it will return a proper value and update new condition in database, otherwise it does nothing.

7. For debuging, please import Postman collection from the link 
`https://www.getpostman.com/collections/23fbb9402a2bdb6cf54c` to connect application server