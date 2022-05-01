
point = {
    "First_Name": "Koji",
    "Last_Name": "Bello",
    "Date_Of_Birth": 000
}

point["Date_Of_Birth"] = 1990
#print(point["Date_Of_Birth"])
#print(point.get("First_Name"))

"""similarly we can change the settings"""

point1 = dict(first="koji", lastname="Bello", data=1990)
point1["country"] = "Cameroon"

print(point1)

"""loop over dictionary"""
for key in point1:
    print(x)

