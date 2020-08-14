seconds = int(input())

hours = int(seconds / 3600)
seconds = seconds % 3600
minutes = int(seconds / 60)
seconds = seconds % 60

print("%d:%d:%d" % (hours, minutes, seconds))
