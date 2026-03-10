def reflex_vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move Right"
    elif location == "B":
        return "Move Left"
    
environment = {
    "A": "Dirty",
    "B": "Dirty"
}

location = "A"

for step in range(4):
    status = environment[location]
    
    action = reflex_vacuum_agent(location, status)
    
    print("Location:", location)
    print("Status:", status)
    print("Action:", action)
    print("-------------------")
 
    if action == "Suck":
        environment[location] = "Clean"
    elif action == "Move Right":
        location = "B"
    elif action == "Move Left":
        location = "A"
        
    if environment["A"] == "Clean" and environment["B"] == "Clean":
        print("Floor is clean")
        break
