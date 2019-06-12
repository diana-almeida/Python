import smtplib
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope=['https://www.googleapis.com/auth/spreadsheets']

credentials=ServiceAccountCredentials.from_json_keyfile_name('C:/Users/admin/Desktop/PythonSendEmail-cab8afac70b1.json', scope)

gc=gspread.authorize(credentials)

wks=gc.open_by_key('1pspcbKZtZP18sv4HmimwIvOFkfk45yBwxoq3J2BMiRo')

wks2 = wks.worksheet('Sheet1')
allwork=wks2.get_all_values()

print(allwork)

#Columna1 =wks2.col_values(2) #demuestra todo lo que hay en la row
#wks2.acell('A1').value
#NumeroMayor=len(Columna1)
#print(wks2.acell(NumeroMayor).value)

#EmailBody=wks2.cell(len(Columna1),1).value #Description
#FirstEmail=wks2.cell(len(Columna1),2).value ##te da el valor de mas abajo que  haya
#SecondEmail=wks2.cell(len(Columna1),3).value ##correo2


#email_sender='reports@gpmobile.net'
#email_receiver=FirstEmail
#server = smtplib.SMTP('smtp.gmail.com',587)
#server.starttls()
#server.login(email_sender,'Gpmobile1')

#message=EmailBody
#server.sendmail(email_sender,email_receiver,message)
#server.quit()
