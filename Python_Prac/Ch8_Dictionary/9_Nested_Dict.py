#Example 1
"""
You can also constitute a for loop to traverse nested dictionary, as in the previous section."""
markslist={
    "Shary": {"HCI":80,"maths":70},
    "Umair": {"HCI":67,"maths":60},
    "Fahad":{"HCI":87,"maths":50}
}

for k,v in markslist.items():
    print(k," : ",v)

#Example 2
"""
It is possible to access value from an inner dictionary with [] notation or get() method."""
#print shary maths marks
print("Shary maths marks: ",markslist.get("Shary")['maths'])

#Also from this tecnique geting 
obj=markslist["Shary"]
print("Shary HCI marks: ",obj.get('HCI'))

