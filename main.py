import scrubadub
import json

inputFile = open('data/morgantownlogs.json')
jsonText = json.load(inputFile)

for item in jsonText:
    item['request']['context']['integrations'] = "REDACTED"
    item['request']['input']['text'] = scrubadub.clean(json.dumps(item['request']['input']['text']), replace_with='placeholder')
    item['response']['input']['text'] = scrubadub.clean(json.dumps(item['response']['input']['text']), replace_with='placeholder')
    item['response']['context']['integrations'] = "REDACTED"

    for output in item['response']['output']['generic']:
        if output["response_type"] == "text":
            output['text'] = scrubadub.clean(json.dumps(output['text']), replace_with='placeholder')

    for texts in item['response']['output']['text']:
        texts = scrubadub.clean(texts, replace_with='placeholder')

    item['response']['input']['text'] = scrubadub.clean(json.dumps(item['response']['input']['text']), replace_with='placeholder')

with open("data/morgantownlogs.json", "w") as inputFile:
    json.dump(jsonText, inputFile)
