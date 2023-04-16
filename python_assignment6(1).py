import json

# Create a dictionary of Indian states and their capitals
states = {
    "Maharashtra": "Mumbai",
    "Delhi": "New Delhi",
    "Karnataka": "Bengaluru",
    "Tamil Nadu": "Chennai",
    "Uttar Pradesh": "Lucknow",
    "Gujarat": "Gandhinagar",
    "Rajasthan": "Jaipur"
}

# Open the JSON file in write mode
with open("states.json", "w") as file:
    # Write the dictionary data to the file in JSON format
    json.dump(states, file)
