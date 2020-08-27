start_date = input()
[start_hour, start_min, start_sec] = [int(x) for x in input().split(' : ')]
end_date = input()
[end_hour, end_min, end_sec] = [int(x) for x in input().split(' : ')]

seconds = end_sec - start_sec
minutes = end_min - start_min
hours = end_hour - start_hour
days = int(end_date[4:]) - int(start_date[4:])

if seconds < 0:
    seconds += 60
    minutes -= 1

if minutes < 0:
    minutes += 60
    hours -= 1

if hours < 0:
    hours += 24
    days -= 1

print('%d dia(s)' %days)
print('%d hora(s)' %hours)
print('%d minuto(s)' %minutes)
print('%d segundo(s)' %seconds)
