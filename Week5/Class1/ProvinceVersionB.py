province_list = {"QC":"Quebec","ON":"Ontorio"}

prov_key = input("Enter the province code > ")

if prov_key.upper() not in province_list:
    print("Sorry")
else:
    result = province_list[prov_key.upper()]
    print("The provine name is {0}".format(result))


