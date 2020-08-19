import json

def ReadReport():
    try:
        index = int(input("Input entry number: "))
        with open('incident_log.json', 'r') as myfile:
            data = myfile.read()

            # parse file
            obj = json.loads(data)

            # show values
            print("Name: {}".format(obj['reports'][index]['name']))
            print("Date: {}".format(obj['reports'][index]['date']))
            print("Type: {}".format(obj['reports'][index]['incidentType']))
            print("Info: {}".format(obj['reports'][index]['otherInfo']))
    except:
        input("ERROR: Argument is not an intiger")
    


def WriteReport():
    
    nameInput = input("Who was hurt?                       ")
    dateInput = input("What day did this happen?           ")
    typeInput = input("What kind of incident was it?       ")
    infoInput = input("Any other additional information?   ")
    incidentObject = { "name": nameInput,
        "date": dateInput,
        "incidentType": typeInput,
        "otherInfo": infoInput
        }
    with open('incident_log.json') as myfile:
        obj = json.load(myfile)
        log = obj["reports"]
        log.append(incidentObject)
        json.dumps(obj)

    with open('incident_log.json','w') as f: 
        json.dump(obj, f, indent=4) 
    print("")
