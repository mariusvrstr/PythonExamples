import requests
import json
from datetime import date

class APIWrapper(object):

    def show_result_details(self, result):
        print (f"Result code: {result.status_code}")
        if result.status_code == 200:
            print (self.get_json_text(result.json()))
        print (result.headers)
        print ("==================================================================")
        print()

    def get_json_text(self, obj):
        # create a formatted string of the Python JSON object
        return json.dumps(obj, sort_keys=True, indent=4)

    def get_json_object(self, obj):
        # create a json object that can be traversed
        return json.loads(self.get_json_text(obj))

    def http_get(self, url, parameters):
        if parameters == None:
           response = requests.get(url)
        else:
           response = request.get(url, parms = parameters)
        return response  

    def http_put_auth(self, url, data, username, password):
        return requests.put(url, json=data, auth=(username, password), verify=False) #only VERIFY FALSE for dev environments

class HydriotAdapter(object):

    def transform_sensor_data(self, sensor_list):

        # date.today()

        data = [
            {
                "name": "Water Level",
                "type": 1,
                "stringValue": "0",
                "readTime": "2021-03-13T20:03:29.605Z",
            }
        ]

        return data
    
    def update_sensor_readings(self, sensor_list):
        client = APIWrapper()

        node_id = '508728DE-F6AC-48C9-9D12-F18E0674A70A' # Get from config
        base_url = 'https://localhost:44333/api'
        update_location = 'node/UpdateNodeSensors'

        url = f"{base_url}/{update_location}/{node_id}"
        data = self.transform_sensor_data(sensor_list)

        response = client.http_put_auth(url, data, "replace_with_user", "replace_with_pass")

        client.show_result_details(response)

        return None


adapter = HydriotAdapter()
adapter.update_sensor_readings({})
