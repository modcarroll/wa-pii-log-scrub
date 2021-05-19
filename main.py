import scrubadub
import json
import sys
import re

# Use this for just one file
# fileName = "data/log1.json"

# Use this for many files
fileName = sys.argv[1]

## Plain text search on specific keywords
with open(fileName, "r") as file:
    filedata = file.read()

regex = re.compile(r'(?=(.))(?:word1|word2|word3|word4)', flags=re.IGNORECASE)
filedata = regex.sub('REDACTED', filedata)

# check for phone numbers
regex = re.compile("(\d{3}\D\d{3}\D\d{4})")
filedata = regex.sub('REDACTED', filedata)

with open(fileName, "w") as file:
    file.write(filedata)

## The rest of this uses scrubadub to remove PII ##
inputFile = open(fileName)
jsonArray = json.load(inputFile)

print("Scrubbing " + fileName + "...")

for item in jsonArray:
    item['request']['context']['metadata'] = "REDACTED"
    item['request']['context']['integrations'] = "REDACTED"
    if('source' in item['request']['input']):
        item['request']['input']['source']['id_s'] = "REDACTED"
    if('source' in item['response']['input']):
        item['response']['input']['source']['id'] = "REDACTED"
    item['request']['input']['text'] = scrubadub.clean(json.dumps(item['request']['input']['text']), replace_with='placeholder')
    item['response']['input']['text'] = scrubadub.clean(json.dumps(item['response']['input']['text']), replace_with='placeholder')
    item['response']['context']['integrations'] = "REDACTED"

    for output in item['response']['output']['generic']:
        if output["response_type"] == "text":
            output['text'] = scrubadub.clean(json.dumps(output['text']), replace_with='placeholder')

    for texts in item['response']['output']['text']:
        texts = scrubadub.clean(texts, replace_with='placeholder')

    item['response']['input']['text'] = scrubadub.clean(json.dumps(item['response']['input']['text']), replace_with='placeholder')

with open(fileName, "w") as inputFile:
    json.dump(jsonArray, inputFile)
