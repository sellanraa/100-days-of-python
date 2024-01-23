# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in a dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Hamburg", "Berlin", "Rostock"],
}

# Nesting a dictionary in a dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Hamburg", "Berlin", "Rostock"], "total_visits": 8},
}

# Nesting a dictionary inside of a list

travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities_visited": ["Hamburg", "Berlin", "Rostock"], 
        "total_visits": 8
    },
]