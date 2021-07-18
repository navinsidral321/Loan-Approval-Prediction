#!C:\python\python.exe
import cgi,cgitb 
import pandas as pd
import os.path
import pickle
import numpy as np
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, _tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

form = cgi.FieldStorage() 
file1=form['filename']
#data=pd.read_csv(filename)

if file1.filename:
    fn=os.path.basename(file1.filename)
    open(fn,'wb').write(file1.file.read())
    filename1=file1.filename
    """
    #Aglorithm build
    
    data=pd.read_csv("file1.csv")
    data1=data.drop(["Loan_ID","Dependents"],axis=1)
    
    c1=LabelEncoder()
    c2=LabelEncoder()
    c3=LabelEncoder()
    c4=LabelEncoder()
    c5=LabelEncoder()
    c6=LabelEncoder()
    
    data1["Gender1"]=c1.fit_transform(data1["Gender"])
    data1["Married1"]=c2.fit_transform(data1["Married"])
    data1["Property_Area1"]=c3.fit_transform(data1["Property_Area"])
    data1["Education1"]=c4.fit_transform(data1["Education"])
    data1["Self_Employed1"]=c5.fit_transform(data1["Self_Employed"])
    data1["Loan_Status1"]=c6.fit_transform(data1["Loan_Status"])
    a=data1.drop(["Gender","Married","Property_Area","Education","Self_Employed","Loan_Status","Loan_Status1"],axis=1)
    b=data1["Loan_Status1"]
    
    X_train, X_test, y_train, y_test = train_test_split(a, b, test_size=0.30, random_state=4)

    model1=tree.DecisionTreeClassifier()
    
    model1=model1.fit(X_train,y_train)
    import pickle
    with open("model_file",'wb') as file1:
        pickle.dump(model1,file1)
    #with open("model_file",'rb') as file2:
        #m1=pickle.load(file2)
    #t1=m1.predict(a)

     

    """

    #predict
 
    data=pd.read_csv(filename1)
    data2=list(data["Loan_ID"])
    data1=data.drop(["Loan_ID","Dependents"],axis=1)
    c1=LabelEncoder()
    c2=LabelEncoder()
    c3=LabelEncoder()
    c4=LabelEncoder()
    c5=LabelEncoder()
    c6=LabelEncoder()
    
    data1["Gender1"]=c1.fit_transform(data1["Gender"])
    data1["Married1"]=c2.fit_transform(data1["Married"])
    data1["Property_Area1"]=c3.fit_transform(data1["Property_Area"])
    data1["Education1"]=c4.fit_transform(data1["Education"])
    data1["Self_Employed1"]=c5.fit_transform(data1["Self_Employed"])
    
    a=data1.drop(["Gender","Married","Property_Area","Education","Self_Employed"],axis=1)
    
with open("model_file",'rb') as file2:
    m1=pickle.load(file2)
t1=m1.predict(a)
status=[]
for i in range(len(t1)):
    if t1[i]==0:
        status.append("Yes")
    else:
        status.append("No")


j=0
import csv
with open('file2.csv','r') as csvinput:
    with open('output.csv', 'w',newline="") as csvoutput:
        writer = csv.writer(csvoutput)
        for row in csv.reader(csvinput):
            if row[0] == "Loan_ID":
                writer.writerow(row+["Status"])
            else:
                writer.writerow(row+[status[j]])
                j=j+ 1
            



print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Bank Loan Approval</title>")
#print('<link rel="icon" href="icon.png" type="image/png>')
print("<style>")
print('div {padding: 150px; background-color:white}')

print("#table1 {font-family: Arial, Helvetica, sans-serif;border-collapse: collapse;width: 100%} #table1 td, #table1 th {border: 1px solid #ddd;padding: 8px;}#table1 tr:nth-child(even){background-color: grey;}#table1 tr:hover {background-color: #ddd;}#table1 th {padding-top: 12px;padding-bottom: 12px;text-align: left;background-color: black;color: white;}")
print("body {background-color: lightgrey;}")



"""
print("table, td, th ")

print("table{border-collapse: collapse;width: 50%;}")

print("th {height: 70px;}")
"""
print("</style>")


print("</head>")
print("<body>")
print("<h1> Loan Approved Details!</h1>")
print("<div>")
print('<table id='+'"table1"'+'border='+"1"+">")
 
print("<tr>")
print("<th>")
print("Loan_ID")
print("</th>")
print("<th>")
print("Status")
print("</th>")

print("</tr>")

for i in range(len(t1)):
    
    if t1[i]==0:

        print("<tr>")
        print("<td>"+str(data2[i])+"</td>")
        print("<td>Yes</td>")
       

  
        print("</tr>")
    else:
        print("<tr>")
        print("<td>"+str(data2[i])+"</td>")
        print("<td>No</td>")
       

  
        print("</tr>")
    
print("</div>")
print("</body>")
print("</html>")