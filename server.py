import os
import time
from flask import Flask, Response, request, redirect

app = Flask(__name__)

red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
reset = "\033[0;0m"
bold = "\033[;1m"
reverse = "\033[;7m"
underline = "\033[4m"

style_json  = {
    "red": "\033[0;31m",
    "green": "\033[0;32m",
    "yellow": "\033[0;33m",
    "blue": "\033[0;34m",
    "purple": "\033[0;35m",
    "cyan": "\033[0;36m",
    "white": "\033[0;37m",
    "reset": "\033[0;0m",
    "bold": "\033[;1m",
    "reverse": "\033[;7m",
    "underline": "\033[4m",
    "blink": "\033[6;30;42m"
}
    
portfolio = f'{open("portfolio.txt", "r").read()}'

for key, value in style_json.items():
    portfolio = portfolio.replace("{%s}" % key, value)

print(portfolio)



def generate_text_letter_by_letter():
    characters = ""
    
    for character in portfolio:
        characters += character
        yield f"\033[2J\033[3J\033[H{characters}\n"
        time.sleep(0.025)  # Add a delay to control the speed of streaming

@app.route('/')
def hello_world():
    if 'curl' not in request.headers.get('User-Agent', ''):
        return redirect('https://github.com/Ankit404butfound', code=302)

    return Response(generate_text_letter_by_letter(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2222, debug=True)