import scrubadub
import json

inputFile = open('data/morgantownlogs.json')
jsonText = json.load(inputFile)

for item in jsonText:
    print()
    print(json.dumps(item, indent=4))
    print()

inputFile.close()

# jsonText.forEach(function (item, index) {
#   console.log("---------------------");
#   console.log(item);
#
#   # need to handle both input and output in item.request and item.response
#
#   const redactedInput = redactor.redact(item.input.text);
#   item.input.text = redactedInput;
#
#   # will need output.text and output.generic.text
#
#   const redactedOutput = redactor.redact(item.output.generic.text);
#   item.output.generic.text = redactedOutput;
#
# // let jsonString = JSON.stringify(jsonText);
#
#
# // make a loop
# // for each input do the below method
# // then take the new string and do a .replace(input, redactedText)
#
# // const redactedText = redactor.redact(jsonString);
#
# // console.log(redactedText);
