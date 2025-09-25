import resources

#get and validate current time
current_time = resources.get_time_input('Please input the current time (HH:MM:SS): ')
#get and validate the amount of time that the alarm will be rung in
alarm_amount = resources.get_alarm_input("Please input the amount of time you'd like the alarm to go off in (HH:MM:SS): ")
#calculate the time the alarm will ring at
alarm_ring_time = resources.calculate_alarm_ring_time(current_time, alarm_amount)

print("Your alarm will ring at: " + alarm_ring_time)