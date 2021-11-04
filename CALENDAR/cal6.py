# 코드 정리
days = ( 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

year = 2023
month = 9

isLeapYear = year % 400 == 0 or ( year % 4 == 0 and year % 100 != 0  )	# 올해가 윤년인가

leapCount = (year-1) // 4 - (year-1) // 100 + (year-1) // 400			# 작년까지 윤년의 갯수
dayOfWeek = ((year-1) + leapCount) % 7									# 1월 1일이 요일

for i in range(0, month - 1 ):
	dayOfWeek += days[i]

if month > 2 and isLeapYear:
	dayOfWeek += 1

dayOfWeek = dayOfWeek % 7	# year 년 month 월 1일의 요일

print(f'{year} 년 {month}월 1일의 요일 : {dayOfWeek}') #6






