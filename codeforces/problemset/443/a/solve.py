ss = str(input()).replace('{', '').replace('}', '').replace(',', '').replace(' ','')
print(len(set(ss)))
