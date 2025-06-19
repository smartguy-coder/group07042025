import requests
import library

# url = 'https://www.ukr.net'
url = 'https://moemisto.ua/img/cache/blog_show_photo/blog/0004/75/fe2a5835d6d62a84d64cc357061c8186a244a1a8.jpeg'
print('main')

response = requests.get(url)
print(response)
# print(response.content)
# print(response.text)

# with open('spring.jpeg', mode='bw') as file:
#     bynary_string = b'hello there'
#     file.write(response.content + bynary_string)

# with open('spring.jpeg', mode='br') as file:
#     print(file.read())