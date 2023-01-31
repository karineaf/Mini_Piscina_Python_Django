import sys

def capital_cities_of_states():
    args_sys = sys.argv[0]
    print(args_sys)
    
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    cities_of_states={}
    for state_name, state_acronym in states.items():    
        for city_acronym, city_name  in capital_cities.items():
            if state_acronym == city_acronym:
                cities_of_states[state_name]=city_name
    #print(cities_of_states[args_sys])



if __name__ == "__main__":
    capital_cities_of_states()