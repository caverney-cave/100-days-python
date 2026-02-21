capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }
#
# # print lille
# print(travel_log["France"][1])

# print "D"
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

# Nested Dictionary in Dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 6,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visites": 9,
    }
}

# print Stuttgart
print(travel_log["Germany"]["cities_visited"][2])
