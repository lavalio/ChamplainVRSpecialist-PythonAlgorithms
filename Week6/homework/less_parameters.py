def describe_pet(pet_name='spot', animal_type='dog'):
    my_pet = {"name":pet_name,"type":animal_type}
    return my_pet

a_pet=describe_pet(animal_type='dolphin')
print(a_pet)