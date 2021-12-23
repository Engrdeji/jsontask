import json

with open('data/data_1.json') as json_file, open('data/data_2.json') as b:
    data = json.load(json_file)
    d2 = json.load(b)
    print(d2['message'], data['message'])


    def mergfiles(a,b):
        jsonMerged = {**a['message'], **b['message']}
        asString = json.dumps(jsonMerged)
        outfile = {"rusult": asString, "required":False}
        print(outfile)

        with open('schema/output.json', 'w') as f:
            json.dump(asString, f)
            print(asString)

mergfiles(data,d2)