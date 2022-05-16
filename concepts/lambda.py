people = [
    {"name": "Winky D", "genre": "Dancehall"},
    {"name": "Jah Prayzah", "genre": "Chinyakare"},
    {"name": "Holy Ten", "genre": "Hip Hop"},
    {"name": "Alick Macheseo", "genre": "Sungura"}
]

people.sort(key=lambda person: person["genre"])

print(people)