import requests

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
    'partnerUserId': '2d34db3885501fe20c4489171ade370fdeceeb52bf7ff474764762e0491b42aa'
}

response = requests.post(url, headers=headers, json=data)

# Extract the token from the response
token_start = response.text.find('"token":"') + len('"token":"')
token_end = response.text.find('"}', token_start)
token = response.text[token_start:token_end]

# Print the URL and token
url_with_token = f'https://discord.com/billing/partner-promotions/1180231712274387115/{token}'
print(url_with_token)
