u = {'sezan':43,"HOQU":84,"rewqan":54,"MR":44,"mango":97}
print(len(u))
print(u.keys())
print(u.values())
u["HOQU"]= 100
print(u.pop("sezan")) 
u.update ({"rimu":80 })
print(u)


# part 2

students_scores = {
    "Alice": {"Math": 85, "Economics": 90, "Physics": 78},
    "Bob": {"Math": 92, "Economics": 88, "Physics": 84},
    "Charlie": {"Math": 80, "Economics": 75, "Physics": 89}
}
 
print(students_scores["Alice"]["Economics"])
del(students_scores["Bob"]["Math"])
students_scores["Alice"]["Economics"] = 100
students_scores.update({"sezan":{"math": 100,"economics": 93}})
print(students_scores)
print(students_scores)
students_scores["Alice"].update ({"chemeistry":96})
print(students_scores)


# part 3

students_scores = {
    "Alice": {"Math": 85, "Economics": 90, "Physics": 78},
    "Bob": {"Math": 92, "Economics": 88, "Physics": 84},
    "Charlie": {"Math": 80, "Economics": 75, "Physics": 89}
}
print(len(students_scores))
print(students_scores.keys())
print(students_scores["Alice"]["Economics"])
students_scores["Alice"]["Math"] = 90
print(students_scores)
students_scores.update({"sezan":{"math": 100,"economics": 93}})
print(students_scores)
del (students_scores["Bob"]["Economics"])
print(students_scores)
students_scores["Alice"].update ({"chemeistry":96})
print(students_scores)

# part 4
u = {'sezan':43,"HOQU":84,"rewqan":54,"MR":44,"mango":97}
print(len(u))
print (u.keys())
print(u.values())
print(u['MR'])
print(u)
for key in u .keys():
    print(u [key])
print(u.items())
for key,value in u .items():
    print(f"the value corresponding to the key {key} is {value}")


# part 5
students_scores = {
    "Alice": {"Math": 85, "Economics": 90, "Physics": 78},
    "Bob": {"Math": 92, "Economics": 88, "Physics": 84},
    "Charlie": {"Math": 80, "Economics": 75, "Physics": 89}
}

print(len(students_scores))
print(students_scores.keys())
print(students_scores.values())
del(students_scores["Bob"]["Math"])
students_scores["Alice"]["Economics"] = 100
print(students_scores)

students_scores.update({"sezan":{"math": 100,"economics": 93}})
print(students_scores)
students_scores["Alice"].update ({"chemeistry":96})
print(students_scores)