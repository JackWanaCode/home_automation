import requests
import sys

def light(name):
    data = {'name': name}
    resp = requests.post('http://127.0.0.1:5000/light', json=data)
    if resp.status_code != 201:
        print("The post request is not completed.")
    else:
        print("Light object is created")


def ac(temp):
    data = {'power': True, 'temp': int(temp)}
    resp = requests.post('http://127.0.0.1:5000/ac', json=data)
    if resp.status_code != 201:
        print("The post request is not completed.")
    else:
        print("AC object is created")


def set_default_temperature(temp):
    data = {'power': True, 'temp': int(temp)}
    resp = requests.put('http://127.0.0.1:5000/ac', json=data)
    if resp.status_code != 201:
        print("The put request is not completed.")
    else:
        print("AC is updated as power off")


if __name__ == "__main__":
    if sys.argv[1] == "light":
        light(sys.argv[2])
    elif sys.argv[1] == "ac":
        ac(sys.argv[2])
    elif sys.argv[1] == "set_ac":
        set_default_temperature(sys.argv[2])
    else:
        print("command is not valid!")
