#!C:\python\python.exe
import cgi,cgitb 

import pandas as pd
data=pd.read_csv("output.csv")
a=list(data['Education'].unique())
c=list(data['Status'].unique())
data1=pd.DataFrame(data)
b=list(data1.groupby(['Education','Status']).size())



a1=list(data['Property_Area'].unique())
data1=pd.DataFrame(data)
b1=(data1.groupby(['Property_Area','Status']).size())



a2=list(data['Gender'].unique())
data1=pd.DataFrame(data)
b2=list(data1.groupby(['Gender','Status']).size())




a3=list(data['Married'].unique())
data1=pd.DataFrame(data)
b3=list(data1.groupby(['Married','Status']).size())


a4=list(data['Loan_Amount_Term'].unique())
data1=pd.DataFrame(data)
b4=list(data1.groupby(['Loan_Amount_Term','Status']).size())





a5=list(data['Self_Employed'].unique())
data1=pd.DataFrame(data)
b5=list(data1.groupby(['Self_Employed','Status']).size())

print("Content-type:text/html\r\n\r\n")

print("<html>")



print("<head>")
print("<title>Bank Loan Approval</title>")
print('<link rel="icon" href="icon.png" type="image/png">')
print('<script type='+'"text/javascript"'+' src='+'"https://www.gstatic.com/charts/loader.js"'+'></script>')
print('<script type='+'"text/javascript">')
print("google.charts.load('current', {'packages':['corechart']});")
print("google.charts.setOnLoadCallback(drawVisualization);")

print("function drawVisualization() {")
        #Some raw data (not necessarily accurate)
#print("var data = google.visualization.arrayToDataTable([['Status', '"+a[0]+"', '"+a[1]+"'],['"+c[0]+"',"+str(b[0])+", "+str(b[2])+"],['"+c[1]+"',"+str(b[1])+","+str(b[3])+"]]);")

print("var data = google.visualization.arrayToDataTable([['Status', '"+a[0]+"', '"+a[1]+"'],['"+c[0]+"',"+str(b[0])+", "+str(b[2])+"],['"+c[1]+"',"+str(b[1])+","+str(b[3])+"]]);")
#print("var data = google.visualization.arrayToDataTable([['Status', 'Graduate', 'Not Graduate'],['No',333, 84],['Yes',147,50]]);")
print("var options = {title : 'Education by Loan-Status',vAxis: {title: 'LOAN_Status'},hAxis: {title: 'EDUCATION'},seriesType: 'bars',series: {5: {type: 'line'}}};")

print("var chart = new google.visualization.ComboChart(document.getElementById('chart_div'));")
print("chart.draw(data, options);")





print("var data1 = google.visualization.arrayToDataTable([['Status', '"+a1[0]+"', '"+a1[1]+"', '"+a1[2]+"'],['"+c[0]+"',"+str(b1[0])+", "+str(b1[2])+", "+str(b1[4])+"],['"+c[1]+"',"+str(b1[1])+","+str(b1[3])+", "+str(b1[5])+"]]);")
print("var options1 = {title : 'Property_Area by Loan-Status',vAxis: {title: 'LOAN_Status'},hAxis: {title: 'Property_Area'},seriesType: 'bars',series: {5: {type: 'line'}}};")
print("var chart1 = new google.visualization.ComboChart(document.getElementById('chart_div1'));")
print("chart1.draw(data1, options1);")




print("var data2 = google.visualization.arrayToDataTable([['Status', '"+a2[0]+"', '"+a2[1]+"'],['"+c[0]+"',"+str(b2[0])+", "+str(b2[2])+"],['"+c[1]+"',"+str(b2[1])+","+str(b2[3])+"]]);")
#print("var data = google.visualization.arrayToDataTable([['Status', 'Graduate', 'Not Graduate'],['No',333, 84],['Yes',147,50]]);")
print("var options2 = {title : 'Gender by Loan-Status',vAxis: {title: 'LOAN_Status'},hAxis: {title: 'Gender'},seriesType: 'bars',series: {5: {type: 'line'}}};")
print("var chart2 = new google.visualization.ComboChart(document.getElementById('chart_div2'));")
print("chart2.draw(data2, options2);")




print("var data3 = google.visualization.arrayToDataTable([['Status', '"+a3[0]+"', '"+a3[1]+"'],['"+c[0]+"',"+str(b3[0])+", "+str(b3[2])+"],['"+c[1]+"',"+str(b3[1])+","+str(b3[3])+"]]);")
print("var options3 = {title : 'Married by Loan-Status',vAxis: {title: 'LOAN_Status'},hAxis: {title: 'Married'},seriesType: 'bars',series: {5: {type: 'line'}}};")
print("var chart3 = new google.visualization.ComboChart(document.getElementById('chart_div3'));")
print("chart3.draw(data3, options3);")



"""
print("var data1 = google.visualization.arrayToDataTable([['Status', '"+a4[0]+"', '"+a4[1]+"', '"+a4[2]+"'],['"+c[0]+"',"+str(b1[0])+", "+str(b1[2])+", "+str(b1[4])+"],['"+c[1]+"',"+str(b1[1])+","+str(b1[3])+", "+str(b1[5])+"]]);")
print("var options1 = {title : 'Property_Area by Loan-Status',vAxis: {title: 'LOAN_Status'},hAxis: {title: 'Property_Area'},seriesType: 'bars',series: {5: {type: 'line'}}};")
print("var chart1 = new google.visualization.ComboChart(document.getElementById('chart_div1'));")
print("chart1.draw(data1, options1);")
"""




print("var data5 = google.visualization.arrayToDataTable([['Status', '"+a5[0]+"', '"+a5[1]+"'],['"+c[0]+"',"+str(b5[0])+", "+str(b5[2])+"],['"+c[1]+"',"+str(b5[1])+","+str(b5[3])+"]]);")
print("var options5 = {title : 'self Employed by Loan-Status',vAxis: {title: 'LOAN_Status'},hAxis: {title: 'Self Employed'},seriesType: 'bars',series: {5: {type: 'line'}}};")
print("var chart5 = new google.visualization.ComboChart(document.getElementById('chart_div5'));")
print("chart5.draw(data5, options5);")

print("}")
print("</script>")
print("</head>")
print("<body>")
print('<div id='+'"chart_div" style='+'"width: 900px; height: 500px;"></div>')
print('<div id='+'"chart_div1" style='+'"width: 900px; height: 500px;"></div>')
print('<div id='+'"chart_div2" style='+'"width: 900px; height: 500px;"></div>')
print('<div id='+'"chart_div3" style='+'"width: 900px; height: 500px;"></div>')
print('<div id='+'"chart_div5" style='+'"width: 900px; height: 500px;"></div>')
print("</body>")
print("</html>")
