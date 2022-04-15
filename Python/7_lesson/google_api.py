import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Specify path to your file with credentials
path_to_credential = 'karpovcourses-v1-5328e2197a70.json' 

# Specify name of table in google sheets
table_name = 'name of your table'

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(path_to_credential, scope)

gs = gspread.authorize(credentials)
work_sheet = gs.open(table_name)

# Select 1st sheet
sheet1 = work_sheet.sheet1

# Get data in python lists format
data = sheet1.get_all_values()

# Get header from data
headers = data.pop(0)

# Create df
df = pd.DataFrame(data, columns=headers)
df.head()