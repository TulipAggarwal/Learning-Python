#Python program for dictionaries
#converting 3 letter month names to full month names
#Example jan -> january

monthConversions = {  
    "Jan":"January",  #the first parameter here are called keys and they should be unique for all of them
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
}

#Accessing a key or value from the above dictionary
print(monthConversions["Mar"]) #First method by entering the key in []
print(monthConversions.get("Apr")) #Method two by using .get()
print(monthConversions.get("abc")) #putting a value not inside of the dictionary will print 'None'
print(monthConversions.get("abc", "Not a valid key")) #Will the print the message 'Not a valid key'
