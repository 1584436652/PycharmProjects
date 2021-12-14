import requests

url = 'https://search.51job.com/list/040000,000000,0000,00,9,99,Python%2B%25E7%2588%25AC%25E8%2599%25AB,2,1.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
}
respones = requests.get(url=url, headers = headers)
