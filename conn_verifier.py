import urllib.request


def is_connected(given_address):
    try: 
        urllib.request.urlopen(given_address)
        return True
    except:
        return False    


if __name__ == "__main__":
    given_input = input('Insert a valid internet address, e.g: "https://www.google.com": ')
    converted_input = str(given_input) 
    print('Your connection is on!' if is_connected(converted_input) else 'No internet available!')



