import requests

webhook = input("Enter your webhook link here > ")
nickname = input("Enter the nickname you want to use > ")
message = input("Enter your message > ")

data = {
    "content" : message,
    "username" : nickname
}

post_req = requests.post(webhook, json = data)
print("Your message has been successfully sent!")