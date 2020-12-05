from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from api.resources.set_resources import add_new_relay, update_relay
from api.resources.get_resources import get_all_relays
from gpio_control.gpio_control import turn_on_relays, turn_off_relays

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)


class Relay(Resource):
    def get(self):
        data = get_all_relays()
        return {'data': data}, 200


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('relay_number', required=True)
        parser.add_argument('state', required=False)
        args = parser.parse_args()

        data = get_all_relays()

        for i in range(len(data)):
            if data[i]['relay_number'] == int(args['relay_number']):
                return 'Relay with ID: {id} already exists.'.format(id=args['relay_number']), 400

        add_new_relay(args['name'], int(args['relay_number']), args['state'])

        return 200

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('relay_number', required=True)
        parser.add_argument('state', required=True)
        args = parser.parse_args()

        data = get_all_relays()

        for i in range(len(data)):
            if data[i]['relay_number'] == int(args['relay_number']):
                if data[i]['state'] == args['state']:
                    return 'Relay is already {current_state}'.format(current_state=args['state']), 400
                else:
                    data[i]['state'] = args['state']
                    update_relay(data)

                    if args['state'] == "on":
                        turn_on_relays()
                    else:
                        turn_off_relays()
                    return 200


api.add_resource(Relay, '/relay')

