import json

Person_string = '{"name" : "Ali" , "languages" :["Python","C#"]}'
Person_dict = {"name" : "Berat","languages" : ["Python" , "C#"]}
#JSON string to Dict
# result = json.loads(Person_string)
# #result  = result["name"]
# result = result["languages"]

# Opening a JSON file
# with open("Person.json") as f:
#     data = json.load(f)
#     print(data["name"])
#     print(data["languages"])



#Dict to JSON string
# result = json.dumps(Person_dict)
# print(result)
# print(type(result))


# with open ("Person.json","w") as f :
#     json.dump(Person_dict , f)

Person_dict = json.loads(Person_string)

result = json.dumps(Person_dict , indent=4 , sort_keys=True)
print(Person_dict)
print(result)