monthConversion = {"Jan": "January",
                   "Feb": "February",
                   "Mar": "March",
                   "Apr": "April",
                   "May": "May",
                   "Jun": "June",
                   "Jul": "July"}

print(monthConversion)
print(monthConversion.get("Jun"))
print(monthConversion.get("Tue", "Not a valid value."))
