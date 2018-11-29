province_list = {"QC":"Quebec","ON":"Ontorio"}

prov_key = input("Enter the province code > ")

try:
    result = province_list[prov_key.upper()]
    print("The provine name is {0}".format(result))
except KeyError:
    print("Sorry")




