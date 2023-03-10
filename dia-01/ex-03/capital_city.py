import sys

def capital_cities_of_states():

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
   
    try:
        args_sys = str(sys.argv[1])

        if len(sys.argv) != 2:
            raise IndexError

        print(cities_of_states[args_sys])

    except IndexError:
        print('')
    except KeyError:
        print('Unknown state')


if __name__ == "__main__":
    capital_cities_of_states()