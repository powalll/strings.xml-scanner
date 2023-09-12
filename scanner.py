import xmltodict
import argparse

parser = argparse.ArgumentParser(description='Static Analysis of strings.xml')
parser.add_argument("path", help="path to strings.xml", type=str)
parser.add_argument("--keyword", help="enumerates keyword in strings.xml in both name and text", type=str)
args = parser.parse_args()

with open(args.path, 'r', encoding='utf-8') as file:
    strings_xml = file.read()

strings_dict = xmltodict.parse(strings_xml)
http_endpoints = set()
api_keys = set()
keyword = set()
print('\nDefault:')
print('------------------------------------------------------------------------------------')
for entry in strings_dict['resources']['string']:
    if '#text' in entry and '@name' in entry:
        if entry['@name'] == 'google_api_key': 
            print(entry['@name'] + ' : ' + entry['#text'])
        elif entry['@name'] == 'google_app_id':
            print(entry['@name'] + ' : ' + entry['#text'])
        elif entry['@name'] == 'google_storage_bucket':
            print(entry['@name'] + ' : ' + entry['#text']) 
        elif entry['@name'] == 'firebase_database_url':
            print(entry['@name'] + ' : ' + entry['#text'])
        elif entry['@name'] == 'AWS_ID':
            print(entry['@name'] + ' : ' + entry['#text'])
        elif entry['@name'] == 'AWS_SECRET':
            print(entry['@name'] + ' : ' + entry['#text'])
        elif "api_key" in entry['@name'].lower():
            api_keys.add(entry['@name'] + ' : ' + entry['#text'])
        elif entry['#text'].lower().startswith('http') or entry['#text'].lower().startswith('www.'):
            http_endpoints.add(entry['#text'])
        
        if args.keyword is not None and (args.keyword.lower() in entry['#text'].lower() or args.keyword.lower() in entry['@name'].lower()):
            keyword.add(entry['@name'] + ' : ' + entry['#text'])

if args.keyword is not None:
    print("\nKeyword matches:")
    print('------------------------------------------------------------------------------------')
    for entry in keyword:
        print(entry)

print("\nAPI Keys:")
print('------------------------------------------------------------------------------------')
for key in api_keys:
    print(key)

if len(http_endpoints) > 0:
    print("\nHTTP Endpoints:")
    print('------------------------------------------------------------------------------------')

for endpoint in http_endpoints:
    if(len(endpoint) > 5):
        print(endpoint)
