a = int(input())
month_list = {}

for i in range(a):
    name = input(f"กรอกชื่อคนที่ {i+1}:")
    month = int(input(f'กรอกเดือนเกิดคนที่ {i+1}:'))
    
    if month not in month_list:
        month_list[month] = []
    month_list[month].append(name)

for month,friends in month_list.items():
    print(f'เดือน {month}: {' '.join(friends)}')
    