plants = [
    ["Begonia", "Daisy", "Lily", "Peony", "Rose", "Sunflower","Lavender"], 
    [1, 2, 3, 6, 5, None, 4]  # Note: None instead of null
]

current_element = 0
alphabetical_order = []

while current_element is not None:
    alphabetical_order.append(plants[0][current_element])
    current_element = plants[1][current_element]

print(" -> ".join(alphabetical_order) + alphabetical_order[1][current_element] )

# for plant in plants[0]:
#     if plant [0] < 

# Run the code - does it work as expected?
# If there are issues, identify and fix them
# Modify it to also print the position number of each plant
# Add a new plant "Iris" in the correct alphabetical position