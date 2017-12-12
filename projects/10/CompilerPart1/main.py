import re
a = "dd!!dd;"
c = re.split(r'[`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?]', a)
print(a,c);