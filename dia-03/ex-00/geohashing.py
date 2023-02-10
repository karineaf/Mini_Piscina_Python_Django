# import sys 
from antigravity import geohash
from sys import argv


def main():
    latitude, longitude, date = get_args()
    try:    
        geohash(float(latitude), float(longitude), date.encode('utf-8'))
    except Exception:
        print("An error ocurred.")

def get_args():
    try:
        if len(argv) != 4:
            raise Exception() 
        return argv[1], argv[2], argv[3]
    except Exception:
        print("Wrong arguments!") 


if __name__ == "__main__":
    main()