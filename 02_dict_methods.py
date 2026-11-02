marks = {
    "Naman": 100,
    "Rohan": 72,
    "priya": 67,
    0: "Harry"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry": 99,"Renuka": 100})
# print(marks)

print(marks.get("Naman")) # Prints None 
print(marks["Naman"]) # Return an error.
print(marks.pop("priya"))
