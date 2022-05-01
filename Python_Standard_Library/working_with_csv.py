import csv
from pprint import pprint

"""write file with csv"""
'''
with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([100,1,5])
    writer.writerow([101,2,15])
'''
"""read file with csv"""   
list_rows =[]
with open("koji-info.csv", "w") as file:
    writer = csv.writer(file)
    rows = ["Koji", "kojibello", "Devops", "2000k", "234566xx"]
    writer.writerow(["Name", "Email", "Possition", "Salary", "contact"])       
    for i in range(20):
        for each_row in rows:
            writer.writerow(rows)
            break
        

# with open("data.csv", "r") as file:
#     reader = csv.reader(file)
#     # print(list(reader))
#     row = [row for row in reader]
#     #print(row)