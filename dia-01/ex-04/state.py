import sys

def states_of_capital_cities():

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
    state_of_cities={}
    for state_name, state_acronym in states.items():    
        for city_acronym, city_name  in capital_cities.items():
            if state_acronym == city_acronym:
                state_of_cities[city_name]=state_name
   
    try:
        args_sys = str(sys.argv[1])

        if len(sys.argv) != 2:
            raise IndexError

        print(state_of_cities[args_sys])

    except IndexError:
        print('')
    except KeyError:
        print('Unknown capital city')


if __name__ == "__main__":
    states_of_capital_cities()