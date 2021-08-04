from traceback import print_tb
import requests
import json
from aws_requests_auth.aws_auth import AWSRequestsAuth

auth = ""
url = ""
thing_name=""

#Reads a single o multiline json from shell
def read_json_from_shell():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = '\n'.join(lines)
    return text

#Returns an 'obfuscated' string: '*' instead of string char
def blur_string(string):
    return (''.join([elem for elem in ['*' for char in string]]))

#Reads arguments from config file
def get_args(filename='app-config.json'):
    print("")
    print('Reading configuration from file ===> \r\n')
    with open(filename, 'r') as file:
        dict = json.load(file)
        global thing_name
        thing_name = str(dict["thing_name"])
        global url 
        url = str(dict["url"])+f"{thing_name}/shadow"
        print(f"url:  {url}")
        acces_key = str(dict["acces_key"])
        print(f"acceskey:  {blur_string(acces_key)}")
        secret_key = str(dict["secret_key"])
        print(f"secretkey:  {blur_string(secret_key)}")
        region = str(dict["region"])
        print(f"region: {region}")
        service = str(dict["service"])
        print(f"service: {service}")
        print("")

        global auth
        auth = AWSRequestsAuth(aws_access_key=acces_key,
                            aws_secret_access_key=secret_key,
                            aws_host= url.split('/')[2],
                            aws_region=region,
                            aws_service=service)

#Execute 'GetThingShadow' action via REST API Call
def getThingShadow():
    global url
    global auth
    response = requests.get(f'{url}',
                        auth=auth)
    print('\n Executing \'GetThingShadow\' Api Call, returning response: \n')
    print(response.content.decode('utf-8')+"\n")

#Execute 'UpdateThingShadow' action via REST API Call
def updateThingShadow():
    global url
    global auth
    print("""Insert payload for update, must match your shadow document 
             Payload Example: 

             {
              "state":{
                "desired": {
                   "device_name": "New_Device_Name",
                   "cpu_load": 19
                }
             }
             } \r\n""")
    
    payload = read_json_from_shell()
    payload = payload.replace("\n","")
    
    response = requests.post(f'{url}',
                               data=payload,
                               auth=auth)
    print('\n Executing \'UpdateThingShadow\' Api Call, returning response: \n')
    print(response.content.decode('utf-8'))

#Execute 'UpdateThingShadow' action via REST API Call
def listNamedShadowsForThing():
    global url
    global auth
    global thing_name
    const_list_named_shadows_url = f"/api/things/shadow/ListNamedShadowsForThing/{thing_name}"
    url_parts=url.split('/')
    url = url_parts[0]+"//"+url_parts[2]+const_list_named_shadows_url
    response = requests.get(f'{url}',
                        auth=auth)
    print('\n Executing \'ListNamedShadowsForThing\' Api Call, returning response: \n')
    print(response.content.decode('utf-8'))


if __name__ == "__main__":
    try:
        get_args()
        choice = input("Type 1 for GetThingShadow, 2 for UpdateThingShadow, 3 for ListNamedShadowsForThing \r\n")
        if(int(choice)==1):
            getThingShadow()
        elif(int(choice)==2):
            updateThingShadow()
        elif(int(choice)==3):
            listNamedShadowsForThing()
        print("")
    except BaseException:
        import sys
        print(sys.exc_info()[0])
        import traceback
        print(traceback.format_exc())