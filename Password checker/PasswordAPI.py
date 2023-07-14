import requests
import hashlib


password= input('Enter the password: ')
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res


# def read_res(response):
#     print(response.text) #by this command it returns all type of hashes that matches the beginning of the hash password

def get_password_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

    # it is the tail of the hash password which is never shared
    #print(h, count)


def pwned_api_check(password):
    # check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
   # print(first5_char, tail)
    #print(response)
    # return read_res(response)
    return get_password_leak_count(response, tail)

pwned_api_check(password)
count = pwned_api_check(password)
if count:
    print(f'{password} was found {count} times.. you should probably change your password')
else:
    print(f'{password} was not found. Carry on!')




