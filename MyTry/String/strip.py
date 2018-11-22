string = ' xoxo love xoxo   '

# Leading and trailing whitepsace are removed
print("1: "+string.strip()+"end")

print("2: "+string.strip(' xoxoe'))

# Argument doesn't contain space
# No characters are removed.
print("3: "+string.strip('sti'))

string = 'android is awesome'
print("4: "+string.strip('an'))