# aws-iot-shadow-rest-api
HTTP Calls to Amazon Web Services Rest API  for IoT Core Shadow Actions 💻🌐💡

This simple script implements the following aws iot calls via Rest Api:

1) GetThingShadow
2) UpdateThingShadow
3) ListNamedShadowForThing


## Installation

Run the following command to install the necessary dependencies
```bash
pip install -r requirements.txt
```

## Usage

1) Edit app-config.json and modify properties by entering your data (e.g. AWS API Secrets, endpoint url etc).

2) Launch api-client.py 

```bash
python3 api-client.py
```
3) You will be offered 3 options:
```bash
Type 1 for GetThingShadow, 2 for UpdateThingShadow, 3 for ListNamedShadowsForThing
```
4) Choose the preferred option and test the corresponding shadow action, via REST Api call.





## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
