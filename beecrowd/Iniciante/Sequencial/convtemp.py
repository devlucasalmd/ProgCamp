n = int(input())

hr = n//3600
min = (n // 60) % 60
sec = n % 60

print("{:01d}:{:01d}:{:01d}".format(hr, min, sec))