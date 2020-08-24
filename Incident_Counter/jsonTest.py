def dumb(): 
    import json 
    
    a = '{"name": "date", "incidentType": "otherInfo"}'
    
    y = json.loads(a) 
    
    print("JSON string = ", y) 
    print() 

    f = open ('incident_log.json', "r") 
    
    data = json.loads(f.read()) 
    
    for i in data['reports']: 
        print(i) 
    
    f.close() 