import requests
import pyshorteners
import random


def generate_hex_string():

    hex_digits = ["0", "1", "2", "3", "4", "5", "6",
                  "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    hex_string = ""
    for i in range(64):
        hex_string += random.choice(hex_digits)

    return hex_string


url = 'https://api.discord.gx.games/v1/direct-fulfillment'

headers = {
    'authority': 'api.discord.gx.games',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.opera.com',
    'referer': 'https://www.opera.com/',
    'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0',
}

data = {
    'partnerUserId': generate_hex_string()
}

response = requests.post(url, headers=headers, json=data)

# Check if the response starts with '<' (HTML response)
if not response.text.startswith('<'):
    # Extract the token from the response
    token_start = response.text.find('"token":"') + len('"token":"')
    token_end = response.text.find('"}', token_start)
    token = response.text[token_start:token_end]

    # Print the URL and token
    url_with_token = f'https://discord.com/billing/partner-promotions/1180231712274387115/{token}'
    print(url_with_token)

    # Shorten the URL using TinyURL
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url_with_token)
    print(f'Short URL: {short_url}')

   # Export the result to "../codes.txt" in append mode
    with open('codes.txt', 'a') as file:
        file.write(short_url + '\n')

    with open('codes.txt', 'r') as file:
        lines = file.readlines()
    # Remove empty line at the end of the file
    if lines and lines[-1].strip() == '':
        lines.pop()

    with open('../codes.txt', 'w') as file:
        file.writelines(lines)
else:
    print('Error: HTML response received. Not adding to the text file.')
