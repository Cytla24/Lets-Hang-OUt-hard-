people_num = input("Number of people attending\n")
people_num = int(people_num)
time_arrival = []
time_end = []
time_arrivalnew =[]
time_endnew = []

int_i = 1
while people_num > 0:
  print("Antendee " + str(int_i))
  start = input("Enter a start time\n(Please, input '06:00AM' instead of '6:00AM' and likewise")
  time_arrival.append(start)
  end = input("Enter an end time\n")
  time_end.append(end)
  people_num -= 1
  int_i += 1

def new_time(time):
  y=[]
  for j in time:
    if "A" in j:
      n_time = str(j[0:2]) + str(j[3:5])
      n_time = int(n_time)
      y.append(n_time)
    elif "P" in j:
      n_time = str(j[0:2]) + str(j[3:5])
      n_time = int(n_time) + 1200
      y.append(n_time)
  return y



def convert_time(time):

  if time <= 1200:
    if time<1000:
      time="0"+str(time)
    time = str(time)
    n_time = time[0:2] + ":"  + time[2:4] + "AM"
  else:
    time -= 1200
    if time<1000:
      time="0"+str(time)
    time = str(time)
    n_time = time[0:2] + ":" + time[2:4] + "PM"
  return n_time


time_arrivalnew=new_time(time_arrival)
time_endnew=new_time(time_end)

meeting_time = max(time_arrivalnew)
ending_time = min(time_endnew)

meeting_time=convert_time(meeting_time)
ending_time=convert_time(ending_time)

if meeting_time >= ending_time:
  print("No available time")
else: 
  print("Y'all should meet between " + str(meeting_time)+" and "+ str(ending_time))

input()

