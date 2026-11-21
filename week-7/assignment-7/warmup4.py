# Use datetime module
from datetime import datetime 
now = datetime.now()
# .strftime() converts a datetime into a formatted string
#  %B = Full month name /  %d = Day of the month / %Y = Four-digit year
print(now.strftime("Today is %B %d, %Y."))