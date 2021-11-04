# year 년 1월 1일의 요일을 구하는 방법. 

year = 2021

# (year-1) 년 까지의 윤년의 갯수
leapCount = (year-1) // 4 - (year-1) // 100 + (year-1) // 400

# year 년 1월 1일의 요일을 구하는 공식
dayofweek = ((year-1) + leapCount) % 7

print( dayofweek )



