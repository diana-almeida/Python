import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('Z:\Interns\Ana Carmiña\GoogleSheets info with Python\leadershipForm_secret.json',scope)

client = gspread.authorize(creds)

sheet = client.open('heello').sheet1

LeaderForm = sheet.get_all_records()
print (LeaderForm)
