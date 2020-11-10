import logging
import requests
import random

from time import time, sleep


def light_json_mock():
    """
    A mock function to simulate how light sensor return value.
    :return: Boolean
    """
    num = random.randint(0, 1)
    if num:
        return {"status": True}
    return {"status": False}

def get_temperature():
    """
    A mock function to simulate temperature return value.
    An additional request to add value of power on or off.
    :return:
    """
    num = random.randint(0, 100)
    return {"temp": num}


def light_controller():
    """
    No parameter needed.
    :return: if Error, return None else return {'status': Boolean}
    """
    light_control = light_json_mock()
    status = light_control['status']
    get_resp = requests.get('http://127.0.0.1:5000/light')
    if get_resp.status_code != 200:
        body = get_resp.json()
        logging.error("The get request is not completed.")
        return None
    else:
        for light in get_resp.json():
            if light['status'] != status:
                data = {'name': light['name'], 'status': status}
                resp = requests.put('http://127.0.0.1:5000/light', json=data)
                if resp.status_code != 201:
                    logging.error("The put request is not completed.")
                    return None
                else:
                    if data['status']:
                        logging.info("Turn on the light %s", light['name'])
                        return {'status': True}
                    else:
                        logging.info("Turn off the light %s", light['name'])
                        return {'status': False}
    return True


def temp_controller():
    """
    No parameter needed
    :return: If error or don't need to change condition, return None
    else return {'power': Boolean, 'temp': int}
    """
    temp_control = get_temperature()
    temp = temp_control['temp']
    get_temp = requests.get('http://127.0.0.1:5000/ac')
    if get_temp.status_code != 200:
        logging.error("The get request is not completed.")
        return None
    else:
        body = get_temp.json()
        if temp == body['temp']:
            data = {'power': False, "temp": body['temp']}
            resp = requests.put('http://127.0.0.1:5000/ac', json=data)
            if resp.status_code != 201:
                logging.error("The put request is not completed.")
                return None
            else:
                logging.info("AC is updated as power off")
                return data
        else:
            data = {'power': True, "temp": body['temp']}
            resp = requests.put('http://127.0.0.1:5000/ac', json=data)
            if resp.status_code != 201:
                logging.error("The put request is not completed.")
                return None
            else:
                logging.info("AC is updated as power on at temp %s", body['temp'])
                return data


if __name__ == "__main__":
    start = time()
    while True:
        light_control = light_controller()
        temp_control = temp_controller()
        if light_control and temp_control:
            sleep(5 - (time() - start) % 5)
        else:
            break
