import sys

def main():
    try:
        args_sys = str(sys.argv[1])
        args_list = args_sys.split(",")

        if len(sys.argv) != 2:
            raise IndexError

        for item in args_list:
            item_normalized = str(item).replace(" ", "").lower()
            
            if item == " " or not item:
                raise IndexError

            try:
                city_of_state = search_city(item_normalized)
                print(f"{item} is the state of {city_of_state.capitalize()}")
            except KeyError:
                try:
                    state_of_city = search_state(item_normalized)
                    print(f"{item.strip()} is the capital of {state_of_city.capitalize()}")
                except KeyError:
                    print(f"{item.strip()} is neither a capital city nor a state")     

    except IndexError:
        print('')


def get_dict():
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
    
    return states, capital_cities

def search_state(city):
    state_of_cities={}
    states, capital_cities = get_dict()
    
    for state_name, state_acronym in states.items():    
        for city_acronym, city_name  in capital_cities.items():
            if state_acronym == city_acronym:
                city_name = city_name.lower()
                state_of_cities[city_name]=state_name
                break
    return state_of_cities[city]


def search_city(state):
    cities_of_states={}
    states, capital_cities = get_dict()
    
    for state_name, state_acronym in states.items():    
        for city_acronym, city_name  in capital_cities.items():
            if state_acronym == city_acronym:
                state_name = state_name.lower()
                cities_of_states[state_name]=city_name
                break
    return cities_of_states[state]


if __name__ == "__main__":
    main()