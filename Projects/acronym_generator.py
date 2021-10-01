text = str(input("Enter you input :"))
data = text.split()
acronym = ""
for i in data:
    acronym = acronym + str(i[0]).upper()
print(acronym)

