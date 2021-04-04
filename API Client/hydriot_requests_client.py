
import requests
import json

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

    def http_post(self, url, data):
        return requests.post(url, data=data)

    def http_post_auth(self, url, data, username, password):
        return requests.post(url, data=data, auth=(username, password))



# Basic Get Command with no parameters
def do_get():

    endpoint = "http://api.open-notify.org/iss-now.json"
    client = APIWrapper()

    # Basic GET command without parameters and JSON response
    response = client.http_get(endpoint, None)

    if response.status_code == 200:
        # Print entire payload
        client.show_result_details(response)

        # Read individual fields from payload
        json_obj = client.get_json_object(response.json())

        print(f"Lattetude: {json_obj['iss_position']['latitude']}, Longetude: {json_obj['iss_position']['longitude']}")
        print()

    else:
        print(f"Failed to make API call. HTTP Error Code: {response.status_code}")


def do_post():
    endpoint = "http://api.open-notify.org/iss-now.json"
    client = APIWrapper()

    payload = {
        'some': 'data'
    }

    # Basic GET command without parameters and JSON response
    response = client.http_post(endpoint, payload)

    client.show_result_details(response)

# do_get()
do_post()