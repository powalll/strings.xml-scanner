# strings.xml scanner
## Purpose
Simple scanner for the strings.xml Android apk configuration file - used to enumerate potentially insecure storage buckets, Firebase endpoints, API keys, and HTTP/API endpoints.
Automatically scans and outputs notable strings.xml entries and contains a keyword search option.
## Instructions
```
git clone github.com/powalll/strings.xml-scanner
pip3 install xmltodict argparse
```
In order to extract the strings.xml from the android APK, utilize [APKTool](https://github.com/iBotPeaches/Apktool) and type the following command:
```
apktool d -s <name>.apk
```
Then find the file at \<name\>/res/values/strings.xml
## Usage
```
python3 scanner.py [--keyword KEYWORD] <path to strings.xml>
```
## Limitations
The current method for finding additional API/HTTP endpoints isn't comprehensive and will be improved. Identifies storage buckets and firebase but doesn't check for level of permission

