import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']
pukpoom = ServiceAccountCredentials.from_json_keyfile_name('pukpoom.json', scope)	# assign JSON file
gc = gspread.authorize(pukpoom)
sheet = gc.open('User Login')					# open SpreadSheet
upattr = sheet.worksheet('UPATTR')				# open WorkSheet

def Register_User(gid, username, password):
	idx = 0 ; write_idx = 0
	gid_list = []
	result = ''

	gid_list = upattr.col_values(1)				# get column data (GID)
	print('GID List : ', gid_list)

	for i in range(len(gid_list)):
		if gid_list[i] == gid:					# exited GID
			idx = i
			write_idx = idx+1
			result = 'Exited GID at index ' + str(write_idx) + ', please log-in'
			print()
			print(result)
			return
			##break
		else:
			idx = len(gid_list)			# new GID
			write_idx = idx+1
			result = 'New GID at index ' + str(write_idx) + ', you are regsited please contact admin'

	print()		
	print(result)
	upattr.update_cell(write_idx, 1, gid)
	upattr.update_cell(write_idx, 2, username)
	upattr.update_cell(write_idx, 3, password)
	upattr.update_cell(write_idx, 4, 'NO')

def Check_User(gid, password):
	idx = 0 ; write_idx = 0
	gid_list = []
	result = ''

	gid_list = upattr.col_values(1)				# get column data
	print('GID List : ', gid_list)

	for i in range(len(gid_list)):
		if gid_list[i] == gid:					# exited GID
			print('GID matched at index', i)
			idx = i
			write_idx = idx+1
			break
		else:
			##print('GID not matched : ', gid_list[i])
			idx = len(gid_list)			# new GID
			write_idx = idx+1

	user_data = upattr.row_values(write_idx)	# get row data
	print('User data : ', user_data)
	print()

	if user_data != []:
		result = 'Valid User Name'
		if password == user_data[2]:
			result = 'Correct Password'
			print(result)
			if user_data[2] == 'YES':
				result = 'You are now log-in'
				print(result)
			else:
				result = 'You need permission, please contact admin'
				print(result)
		else:
			result = 'Incorrect Password'
			print(result)
	else:
		result = 'Invalid User Name'
		print(result)

	return(result)

gid = '437806'
username = 'PUKPOOM SOMPOBKULVECH'
password = 'qaz'

Register_User(gid, username, password)
##result = Check_User(gid, password)