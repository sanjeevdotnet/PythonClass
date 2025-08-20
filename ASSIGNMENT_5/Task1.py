dic_studentmark = {
    'sanjeev':150,
    'rajeev':50,
    'rohit': 70,
    'alice': 80,
    'shyam': 59,
    'mohan': 5,
}

Name = input("Enter the Student's Name:").lower().lstrip().rstrip()
if Name in dic_studentmark:
    Mark = dic_studentmark[Name]
    print(Name+"'s Marks :",Mark)
else:
    print("Student not found")