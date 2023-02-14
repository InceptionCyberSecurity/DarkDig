## About darkdig
darkdig is a simple script written in Python3.11 in which it allows users to enter a search term (query) in the command line and darkdig will pull all the deep web onion sites relating to that query.

## Installation
1) ``git clone https://github.com/ArcadeusOPS/DarkDig.git``<br/>
2) ``cd darkdig``<br/>
3) ``python3 -m pip install -r requirements.txt``<br/>
4) ``python3 darkdig.py --help``<br/>
## Usage
Example 1: ``python3 darkdig.py --query programming``<br/>
Example 2: ``python3 darkdig.py --query="chat rooms"``<br/>
Example 3: ``python3 darkdig.py --query hackers --amount 12``<br/>

 - Note: The 'amount' argument filters the number of results outputted<br/>

### Usage With Increased Anonymity
darkdig Proxy: ``python3 darkdig.py --query bitcoin -p``<br/>

## Menu
```

usage: darkdig.py [-h] [-v] [-q QUERY] [-a AMOUNT] [-p]

options:
  -h, --help            show this help message and exit
  -v, --version         returns darkdig's version
  -q QUERY, --query QUERY
                        the keyword or string you want to search on the deepweb
  -a AMOUNT, --amount AMOUNT
                        the amount of results you want to retrieve (default: 10)
  -p, --proxy           use darkdig proxy to increase anonymity

```

## Ethical Notice
The original developer of this program, Josh Schiavone, nor ArcadeusOPS, are not responsible for misuse of this data gathering tool. Do not use darkdump/darkdig to navigate websites that take part in any activity that is identified as illegal under the laws and regulations of your government. STAY LEGAL !!

## License
MIT License<br/>
Copyright (c) Josh Schiavone and ArcadeusOPS
