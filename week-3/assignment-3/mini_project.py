day_of_the_week = input("What day is it? ").capitalize()
time_of_day = input("What time of day? ").lower()

if day_of_the_week == "Monday" and time_of_day == "morning":
    print(f"Today is {day_of_the_week} and time is {time_of_day}, good time to study Python.")
elif day_of_the_week == "Wednesday" and time_of_day == "morning":
    print(f"Todday is {day_of_the_week} and time is {time_of_day}, good time for doing yoga!")
elif day_of_the_week == "Saturday" and time_of_day == "morning":
    print(f"Today is {day_of_the_week} and time is {time_of_day}, good time for going on a hike!")
elif day_of_the_week == "Monday" and time_of_day == "afternoon":
    print(f"Todday is {day_of_the_week} and time is {time_of_day}, good time to go to the library!")
elif day_of_the_week == "Wednesday" and time_of_day == "afternoon":
    print(f"Todday is {day_of_the_week} and time is {time_of_day}, good for cooking dinner!")
elif day_of_the_week == "Saturday" and time_of_day == "afternoon":
    print(f"Today is {day_of_the_week} and time is {time_of_day}, good time for going out with friends!")
elif day_of_the_week == "Monday" and time_of_day == "evening":
    print(f"Todday is {day_of_the_week} and time is {time_of_day}, good time for writting!")
elif day_of_the_week == "Wednesday" and time_of_day == "evening":
    print(f"Todday is {day_of_the_week} and time is {time_of_day}, good time for reading!")
elif day_of_the_week == "Saturday" and time_of_day == "evening":
    print(f"Today is {day_of_the_week} and time is {time_of_day}, is a good time for going out to the movies!")
else:
    print(f"Today is {day_of_the_week} and time is {time_of_day}, have a nice day!")

