kilometer_input = float(input("How many kilometer race did you run?"))
miles_converted = kilometer_input/1.61
ideal_proportion = 6.211180124223602/2562
ideal_time_in_seconds = miles_converted/ideal_proportion
ideal_time_in_minutes = ideal_time_in_seconds/60
ideal_time_in_hour = ideal_time_in_minutes/60
time_per_mile_in_seconds = ideal_time_in_seconds/miles_converted
time_per_mile_in_minutes = ideal_time_in_minutes/miles_converted
speed = miles_converted/ideal_time_in_hour
print(f'You ran {round(miles_converted,2)} miles in {ideal_time_in_seconds} seconds')
print(f'Your average paces are:\nTime per mile in seconds: {round(time_per_mile_in_seconds, 2)} seconds per mile\nTime per mile in minutes: {round(time_per_mile_in_minutes, 2)} minutes per mile')
print(f'Your average speed is {round(speed,2)} mile per hour')