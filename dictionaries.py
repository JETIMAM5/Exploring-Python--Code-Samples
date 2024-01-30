#plakalar = {"Kocaeli":41, "İstanbul":34}
#print(plakalar["İstanbul"])
#print(plakalar["Kocaeli"])

#plakalar["Ankara"] = 6
#plakalar["Kocaeli"] = "New Value"
#print(plakalar)

users = {
"BeratYetis" :{
    "Age" : 20,
    "Roles":["User"],
    "Email" : "berat_yetis5859@outlook.com",
    "Address" : "Istanbul",
    "Phone" : 5536912058

}
,
"EsmaYetis" :{
    "Age" : 11,
    "Roles":["Admin","User"],
    "Email" : "esma_yetis5859@outlook.com",
    "Address" : "Istanbul",
    "Phone" : 559656565

}
}
print(users["EsmaYetis"]["Roles"][0])