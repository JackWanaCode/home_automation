import logging

from api import app
from flask import request, jsonify, make_response
from models.light import Light
from models.air_conditioner import AirC


@app.route('/')
def home():
    return "Hello World!"


@app.route('/light', methods=['POST', 'GET', 'PUT'])
def light():
    try:
        data = request.get_json()
    except Exception as e:
        logging.info("Payload is not provided or failed to deserialize. Error %s", e)
        data = None
    if request.method == 'POST':
        try:
            if data is None:
                logging.error("There is no payload in request")
                data = {
                    "error": "Couldn't find payload in request"
                }
                return make_response(jsonify(data), 400)
            name = data['name']
            light_obj = Light.query.filter(Light.name==name).first()
            if light_obj:
                logging.info("Name is being used. Light id %s", light_obj.id)
                return make_response({
                    "message": "Name is being used. Please use another name"
                }, 400)
            new_light = Light(status=False, name=name)
            new_light.add()
            logging.info("Adding new Light. Light id: %s", new_light.id)
            data = [{
                "id": new_light.id,
                "name": name,
                "status": False,
                "date_created": new_light.date_updated,
                "date_updated": new_light.date_updated
            }]
            return make_response(jsonify(data), 201)
        except Exception as e:
            logging.error("Couldn't add new light. Error is: %s", e)
            data = {
                "error": "Couldn't add new light"
            }
            return make_response(jsonify(data), 400)
    elif request.method == 'PUT':
        if data and 'name' in data and 'status' in data:
            name = data['name']
            status = data['status']
            light_obj = Light.query.filter(Light.name==name).first()
            if light_obj is None:
                data = [{
                    "message": "Object is not found in database"
                }]
                logging.info("Light is not found. Name: %s", name)
                return make_response(jsonify(data), 404)
            light_obj.status = status
            light_obj.save()
            data = [{
                "id": light_obj.id,
                "name": light_obj.name,
                "status": light_obj.status,
                "date_created": light_obj.date_updated,
                "date_updated": light_obj.date_updated
            }]
            logging.info("Updated light %s to %s", light_obj.name, light_obj.status)
            return make_response(jsonify(data), 201)
        elif data and 'name' not in data and 'status' in data:
            light_objs = Light.query.all()
            if light_objs:
                status = data['status']
                data = []
                for obj in light_objs:
                    obj.status = status
                    obj.save()
                    data.append({
                        "id": obj.id,
                        "name": obj.name,
                        "status": obj.status,
                        "date_created": obj.date_updated,
                        "date_updated": obj.date_updated
                    })
                logging.info("Updated all lights to %s", status)
                return make_response(jsonify(data), 201)
        else:
            logging.error("There is no payload or invalid payload. Payload: %s", data)
            data = {
                "message": "There is not payload or invalid payload"
            }
            return make_response(jsonify(data), 400)
    elif request.method == 'GET':
        if data and 'name' in data:
            name = data['name']
            light_obj = Light.query.filter(Light.name==name).first()
            if light_obj is None:
                data = {
                    "message": "Object is not found in database"
                }
                logging.info("Light is not found. Name: %s", name)
                return make_response(jsonify(data), 404)
            data = [{
                "id": light_obj.id,
                "name": light_obj.name,
                "status": light_obj.status,
                "date_created": light_obj.date_updated,
                "date_updated": light_obj.date_updated
            }]
            logging.info("Get light %s", light_obj.name)
            return make_response(jsonify(data), 200)
        else:
            light_objs = Light.query.all()
            data = []
            for obj in light_objs:
                data.append({
                    "id": obj.id,
                    "name": obj.name,
                    "status": obj.status,
                    "date_created": obj.date_updated,
                    "date_updated": obj.date_updated
                })
            logging.info("Get all light objects")
            return make_response(jsonify(data), 200)
    else:
        logging.error("Request is not accepted. Request: %s", request.method)
        data = {
            "message": "Bad request"
        }
        return make_response(jsonify(data), 400)


@app.route('/ac', methods=['POST', 'GET', 'PUT'])
def ac():
    try:
        data = request.get_json()
    except Exception as e:
        logging.info("Payload is not provided or failed to deserialize. Error %s", e)
        data = None
    if request.method == 'POST':
        if AirC.query.filter().first():
            logging.error("The AC is existed.")
            data = {
                "error": "Object is existed, couldn't create new one"
            }
            return make_response(jsonify(data), 400)
        try:
            if data is None:
                logging.error("There is no payload in request")
                data = {
                    "error": "Couldn't find payload in request"
                }
                return make_response(jsonify(data), 400)
            power = data['power']
            temp = data['temp']
            new_ac = AirC(power=True, temp=temp)
            new_ac.add()
            logging.info("Adding new Air Conditioner. AC id: %s", new_ac.id)
            data = {
                "id": new_ac.id,
                "power": power,
                "temp": temp,
                "date_created": new_ac.date_updated,
                "date_updated": new_ac.date_updated
            }
            return make_response(jsonify(data), 201)
        except Exception as e:
            logging.error("Couldn't add ac. Error is: %s", e)
            data = {
                "error": "Couldn't add ac"
            }
            return make_response(jsonify(data), 400)
    elif request.method == 'PUT':
        if data and 'power' in data and 'temp' in data:
            power = data['power']
            temp = data['temp']
            ac_obj = AirC.query.filter().first()
            if ac_obj is None:
                data = {
                    "message": "Object is not found in database"
                }
                logging.info("AC is not found.")
                return make_response(jsonify(data), 404)
            ac_obj.power = power
            ac_obj.temp = temp
            ac_obj.save()
            data = {
                "id": ac_obj.id,
                "power": ac_obj.power,
                "temp": ac_obj.temp,
                "date_created": ac_obj.date_updated,
                "date_updated": ac_obj.date_updated
            }
            logging.info("Updated ac is %s and temperature %s", ac_obj.power, ac_obj.temp)
            return make_response(jsonify(data), 201)
        else:
            logging.error("There is no payload or invalid payload. Payload: %s", data)
            data = {
                "message": "There is not payload or invalid payload"
            }
            return make_response(jsonify(data), 400)
    elif request.method == 'GET':
        ac_obj = AirC.query.filter().first()
        if ac_obj is None:
            data = {
                "message": "Object is not found in database"
            }
            logging.info("AC is not found.")
            return make_response(jsonify(data), 404)
        data = {
            "id": ac_obj.id,
            "power": ac_obj.power,
            "temp": ac_obj.temp,
            "date_created": ac_obj.date_updated,
            "date_updated": ac_obj.date_updated
        }
        logging.info("Get ac object. %s", data)
        return make_response(jsonify(data), 200)

