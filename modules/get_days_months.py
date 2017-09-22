def get_no_of_days(month, year):
	if(month==2):
		if(year%100==0):
			if(year%4==0):
				return 29
			else:
				return 28
		if(year%4==0):
			return 29
		else:
			return 28
	if((month<=7 and month%2==1) or (month>7 and month%2==0)):
		return 31
	else:
		return 30

