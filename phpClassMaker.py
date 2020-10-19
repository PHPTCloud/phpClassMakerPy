import sys
import json

def makeGetter(file, fieldName, fieldType):
    # getter for current field
    method = 'get' + fieldName[0].capitalize() + fieldName[1:len(fieldName)]

    file.write(tab + '/**\n')
    file.write(tab + ' * @return ' + fieldType + '\n')
    file.write(tab + ' */\n')
    file.write(tab + 'public function ' + method + '(): ?'+fieldType+'\n')
    file.write(tab + '{\n')
    file.write(tab*2 + 'return $this->'+fieldName+';\n')
    file.write(tab + '}\n\n')

def makeSetter(file, fieldName, fieldType):
    #setter for current field
    method = 'set' + fieldName[0].capitalize() + fieldName[1:len(fieldName)]

    file.write(tab + '/**\n')
    file.write(tab + ' * @param '+fieldType+' $'+fieldName+'\n')
    file.write(tab + ' * @return this\n')
    file.write(tab + ' */\n')
    file.write(tab + 'public function ' + method + '('+fieldType+' $'+fieldName+'): self\n')
    file.write(tab + '{\n')
    file.write(tab*2 + '$this->'+fieldName+' = $'+fieldName+';\n')
    file.write(tab*2 + 'return $this;\n')
    file.write(tab + '}\n\n')

def makeField(file, fieldModificator, fieldType, fieldName):
    phpClassFile.write(tab + '/**\n')
    phpClassFile.write(tab + ' * @var ' + fieldType + '\n')
    phpClassFile.write(tab + ' */\n')
    phpClassFile.write(tab + fieldModificator + ' $' + fieldName + '; \n\n')


args = []

if __name__ == "__main__":
    for param in sys.argv:
        args.append(param)

# path to save php class
newFilePath = args[1] + '/'
# path of class description by json
path = args[1] + '/' + args[2]
# tab sign
tab = '\t'

with open(path) as jsonFile:
    data = json.load(jsonFile)

if data:
    phpClassFile = newFilePath + data['name'] + '.php'
    phpClassFile = open(phpClassFile, 'w+')
    phpClassFile.write('<?php\n/**\n * @class '+data['name']+'\n * @package '+data['package']+' \n */\n\n')
    phpClassFile.write('namespace ' + data['package'] + ';' + '\n\n')    
    phpClassFile.write('class ' + data['name'])

    if 'extends' in data:
        phpClassFile.write(' extends ' + data['extends'])

    if 'implements' in data:
        phpClassFile.write(' implements ' + data['implements'])

    phpClassFile.write('\n{\n')

    if 'fields' in data:
        # Private class fields processing
        if 'private' in data['fields']:
            for fieldName, fieldType in data['fields']['private'].items():
                makeField(phpClassFile, 'private', fieldType, fieldName)

        # Protected class fields processing
        if 'protected' in data['fields']:
            for fieldName, fieldType in data['fields']['protected'].items():
                makeField(phpClassFile, 'protected', fieldType, fieldName)

        # Public class fields processing
        if 'public' in data['fields']:
            for fieldName, fieldType in data['fields']['public'].items():
                makeField(phpClassFile, 'public', fieldType, fieldName)

        # Private class fields getters and setters processing
        if 'private' in data['fields']:
            for fieldName, fieldType in data['fields']['private'].items():
                makeGetter(phpClassFile, fieldName, fieldType)
                makeSetter(phpClassFile, fieldName, fieldType)

        # Private class fields getters and setters processing
        if 'protected' in data['fields']:
            for fieldName, fieldType in data['fields']['protected'].items():
                makeGetter(phpClassFile, fieldName, fieldType)
                makeSetter(phpClassFile, fieldName, fieldType)

        # Public class fields getters and setters processing
        if 'public' in data['fields']:
            for fieldName, fieldType in data['fields']['public'].items():
                makeGetter(phpClassFile, fieldName, fieldType)
                makeSetter(phpClassFile, fieldName, fieldType)
    
    phpClassFile.write('}')

    phpClassFile.close()