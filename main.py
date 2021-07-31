
from math import ceil
import sys, os, json
import os.path as Path


def LinearRegression(minParam, maxParam):
    # the minLvl is 1
    # the maxLvl is 99
    # the formula is y = ax + b where (y) is the value of paramter at (x) level
    param = []
    for i in range(99):
        y = ceil((((i + 1) - 1) * (int(maxParam) - int(minParam)) / (99 - 1)) + int(minParam))
        param.append(y)
    
    return param

def ErrorCommandPrint(errCode):
    if(errCode == 0):
        print('[Error Code: 0] (Command Error)')
        print(
            'Correct command is: $ python main.py [CSV Filename] [Output]')
        print(
            'Output options must be: [Enemies, Actors, Troops, Armors, Classes, Items, Skills, States, Weapons]')
    elif(errCode == 1):
        print('[Error Code: 1] (File not found)')
        print('File not found! Make sure put the file on the same folder with main.py')
    else:
        print('[Error Code: Undefined]')
        print(
            'Unknown Error found! Please contact the author for debug request. Thank you.')

    sys.exit()


def main(argv):
    print('### Checking Command ###')
    if(len(argv) < 2):
        ErrorCommandPrint(0)

    filename = argv[0]
    output = argv[1]
    outputDir = './outputs/'
    acceptable_output = ['Enemies', 'Actors', 'Classes',
                         'Armors', 'Weapons', 'Items', 'Skills', 'States']

    print('### Checking Filename Argument ###')
    if(filename == '' or filename == None):
        ErrorCommandPrint(0)
    elif(filename != '' and filename != None):
        if(not Path.isfile(filename)):
            ErrorCommandPrint(1)
        else:
            print('### Checking Output Argument ###')
            if(output == '' or output == None):
                ErrorCommandPrint(0)
            elif(output != '' and output != None):
                if output in acceptable_output:
                    result = []
                    idx = 0
                    print('### Opening File ###')
                    with open(filename, 'r') as f:
                        print('### Reading CSV Lines ###')
                        for line in f:
                            if(idx == 0):
                                idx += 1
                                continue

                            words = line.strip().split(',')
                            result.append(words)
                            
                    #create JSON file
                    #exportJson = '[null,'
                    listEntries = []
                    listEntries.append(None)
                    ids = 1
                    print('### Creating Dictionary List ###')
                    if(output == "Enemies"):
                        for entry in result:
                            entries = {}
                            entries["id"] = ids
                            entries["actions"] = [{"conditionParam1":0,"conditionParam2":0,"conditionType":0,"rating":5,"skillId":1}]
                            entries["battlerHue"] = 0
                            entries["battlerName"] = ""
                            entries["dropItems"] = [{"dataId":1,"denominator":1,"kind":0},{"dataId":1,"denominator":1,"kind":0},{"dataId":1,"denominator":1,"kind":0}]
                            entries["exp"] = entry[10]
                            entries["traits"] = [{"code":22,"dataId":0,"value":0.95},{"code":22,"dataId":1,"value":0.05},{"code":31,"dataId":1,"value":0}]
                            entries["gold"] = entry[9]
                            entries["name"] = entry[0]
                            entries["note"] = ""
                            entries["params"] = [entry[1], entry[2], entry[3], entry[4], entry[5], entry[6], entry[7], entry[8]]
                            
                            listEntries.append(entries)
                            ids += 1
                            
                    elif(output == "Actors"):
                        for entry in result:
                            entries = {}
                            entries['id'] = ids
                            entries['battlerName'] = ''
                            entries['characterIndex'] = 0
                            entries['characterName'] = ''
                            entries['classId'] = 1
                            entries['equips'] = [0,0,0,0,0]
                            entries['faceIndex'] = 0
                            entries['faceName'] = ''
                            entries['traits'] = []
                            entries['initialLevel'] = entry[3]
                            entries['maxLevel'] = entry[4]
                            entries['name'] = entry[0]
                            entries['nickname'] = entry[1]
                            entries['note'] = ''
                            entries['profile'] = entry[2]
                            
                            listEntries.append(entries)
                            ids += 1
                            
                    elif(output == "Weapons"):
                        for entry in result:
                            entries = {}
                            entries['id'] = ids
                            entries['animationId'] = 0
                            entries['description'] = entry[1]
                            entries['etypeId'] = 1
                            entries['traits'] = [{"code":31,"dataId":1,"value":0},{"code":22,"dataId":0,"value":0}]
                            entries['iconIndex'] = 0
                            entries['name'] = entry[0]
                            entries['note'] = ''
                            entries['params'] = [entry[3], entry[4], entry[5], entry[6], entry[7], entry[8], entry[9], entry[10]]
                            entries['price'] = entry[2]
                            entries['wtypeId'] = 0
                            
                            listEntries.append(entries)
                            ids += 1
                            
                    elif(output == "Armors"):
                        for entry in result:
                            entries = {}
                            entries['id'] = ids
                            entries['atypeId'] = 0
                            entries['description'] = entry[1]
                            entries['etypeId'] = entry[3]
                            entries['traits'] = [{"code":22,"dataId":1,"value":0}]
                            entries['iconIndex'] = 0
                            entries['name'] = entry[0]
                            entries['note'] = ''
                            entries['params'] = [entry[4], entry[5], entry[6], entry[7], entry[8], entry[9], entry[10], entry[11]]
                            entries['price'] = entry[3]
                            
                            listEntries.append(entries)
                            ids += 1
                            
                    elif(output == "States"):
                        print('### Not yet developed ###')
                    elif(output == "Items"):
                        print('### Not yet developed ###')
                    elif(output == "Skills"):
                        print('### Not yet developed ###')
                    elif(output == "Classes"):
                        for entry in result:
                            entries = {}
                            entries['id'] = ids
                            entries['expParams'] = [30,20,30,30]
                            entries['traits'] = [{"code":23,"dataId":0,"value":1},
                                                {"code":22,"dataId":0,"value":0.95},
                                                {"code":22,"dataId":1,"value":0.05},
                                                {"code":22,"dataId":2,"value":0.04}]
                            entries['learnings'] = []
                            entries['name'] = entry[0]
                            entries['note'] = ''
                            
                            mhp = LinearRegression(entry[1], entry[2])
                            mmp = LinearRegression(entry[3], entry[4])
                            atk = LinearRegression(entry[5], entry[6])
                            defn = LinearRegression(entry[7], entry[8])
                            mat = LinearRegression(entry[9], entry[10])
                            mdf = LinearRegression(entry[11], entry[12])
                            agi = LinearRegression(entry[13], entry[14])
                            luk = LinearRegression(entry[15], entry[16])
                            entries['params'] = [mhp, mmp, atk, defn, mat, mdf, agi, luk]
                            
                            listEntries.append(entries)
                            ids += 1
                            
                    else:
                        ErrorCommandPrint(-1)
                        
                    print('### Checking Output Folder ###')
                    if(Path.exists(outputDir)):
                        print('### Folder Exist, Proceeding ###')
                    else:
                        print('### Folder Is Missing, Creating New Folder')
                        os.mkdir(outputDir)
                        print('### Folder Creation Complete, Proceeding ###')
                        
                    print('### Generating JSON File ###')
                    with open(outputDir + output + '.json', 'w') as jsonFile:
                        json.dump(listEntries, jsonFile, indent=4)
                        
                    print('### Process Complete ###')

                else:
                    ErrorCommandPrint(0)
    else:
        ErrorCommandPrint(-1)

if __name__ == '__main__':
    main(sys.argv[1:3])
