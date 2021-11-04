days = ( 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

year = 2023
month = 9

# year 년 1월 1일의 요일을 구하는 공식
leapCount = (year-1) // 4 - (year-1) // 100 + (year-1) // 400
dayOfWeek = ((year-1) + leapCount) % 7

print(f'{year} 년 1월 1일의 요일 : {dayOfWeek}') #6

# year 년 month 월 1일의 요일
isLeapYear = year % 400 == 0 or ( year % 4 == 0 and year % 100 != 0  )

# 1월 ~ month-1 까지의 날자수 더하기
for i in range(0, month - 1 ):
	dayOfWeek += days[i]

if month > 2 and isLeapYear:
	dayOfWeek += 1

dayOfWeek = dayOfWeek % 7

print(f'{year} 년 {month}월 1일의 요일 : {dayOfWeek}') #6






