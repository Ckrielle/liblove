![liblove logo](/docs/images/liblove.png)

# liblove
Give your python libraries some love <3

## Table of Contents
* [General Info](#general-info)
* [Installation](#installation)
* [Demonstration](#demonstration)
* [To-Do](#to-do)
* [Donations](#donations)
* [Contact Me](#contact-me)
* [License](#license)

## Gerenal Info
**Purpose**: This project goes to all the python libraries that carries our projects, the silver linings of endless google searches. After we download them
we forget them and never care about them. This is what liblove fixes. It gives them some love <3

**How**: You need a username to access a repo with the github API. So I had to find a way to get the username to make the request. Luckily I was on pypi at that time,
and observed that their url is of the for pypi.org/project/*project*. The script gets every library you have in tour system, sends a request to pypi, takes the 
text of the response, parses it into BeautifulSoup, which in turns finds the link to the github repo, remove the necessary characters so that only the name and project
remain, adds them to the appropriate request for the API, and then sends it. Though you need to create a token for this to work. You can learn how to generate one
[here](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token), and then add it in the appropriate variable in the script.

## Installation
All you have to do is copy paste the commands below into your terminal.
```
git clone https://github.com/Ckrielle/liblove.git
cd liblove
pip install -r requirements.txt
```

## Demonstration
![Demo](./docs/examples/demo.svg)

## To-Do
As you can see it is a simple script. I mainly want to see how I can implement oauth. If anyone would want to do it feel free to do so.

## Donations
If for some reason you think I deserve money for having written this or any of my other projects, firstly thank you very much I'm humbled. Secondly you can buy me a penguin!

<a href="https://www.buymeacoffee.com/Machina" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

## Contact Me
You can find me on [Twitter](https://twitter.com/3xM4ch1n4).

## License
See LICENSE for more info.
