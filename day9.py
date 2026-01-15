'''student = {
    "name": "ved",
    "age": 20,
    "course": "python"
}

print(student)
print(student["course"])
student["grades"]=93
print(student)
print(student.values())
print(student.keys())
std=student.pop("age")
print(student)
for key in student:
    print(key)
student["age"]=20
print(student)

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student, score in student_scores.items():
    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)

capitals={
    "france":"paris",
    "germany":"berlin"
}
#nested list
travel_log={
    "france":{
        "total_time":5,
        "cities_visited":["paris","lile","dijon"]
    },

    "germany":{
        "total_time":3,
        "cities_visited":["berlin","stuttgart"]
    }
}

#print the list
print(travel_log["france"][2])

nestedlist=["a","b","c",["d","e","f"]]
print(nestedlist)
print(nestedlist[0])
print(nestedlist[3][1])




def highest_bid(bidding_dictionary):
    winner = ""
    highest_bid = 0

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with the bid of {highest_bid}")


bids = {}
continue_bidding = True

while continue_bidding:
    name = input("Enter your name: ")
    price = int(input("Enter your bid: "))
    bids[name] = price

    should_continue = input(
        "Do you want to continue? Type 'y' for yes and 'n' for no:\n"
    ).lower()

    if should_continue == "n":
        continue_bidding = False
        highest_bid(bids)
    elif should_continue == "y":
        print("\n" * 20)'''












