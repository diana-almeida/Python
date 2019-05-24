import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('.json file path',scope)

client = gspread.authorize(creds)

sheet = client.open('Name of the file').sheet1

LeaderForm = sheet.get_all_records()
print (LeaderForm)
