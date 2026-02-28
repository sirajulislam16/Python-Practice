info={
    "name": "Mahin",
    "age": 23,
    "city": "Narayanganj"
}
print("Your city is: ",info["city"])

#another method
print(info.get("city"))

# Print a value with a default fallback if the key is missing
print(info.get("union","not found"))