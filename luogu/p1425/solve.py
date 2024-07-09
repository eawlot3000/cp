time = str(input()).split()
for i in range(len(time)):
  time[i] = int(time[i])
result = (time[2]*60+time[3]) - (time[0]*60+time[1])
print("{} {}".format(result//60 ,result%60))
