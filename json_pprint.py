import json
import sys

def json_pprint():
    data = input("JSON data:")
    json_dict = json.loads(data)
    print("=" * 100)
    json_output = json.dumps(json_dict, indent=4)
    print(json_output)

if __name__ == '__main__':
    json_pprint()
