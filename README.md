# instagram-unfollow
unfollow all automatically through selenium
* note that Instagram has a limit for unfollowing (15 in 15 minutes, no more than 1000 per day)

* Tested on Mac 10.13.2 with Selenium 3.8.1, ChromeDriver 2.35
* Tested on Instagram on Jan 20th, 2018

## Dependency
* virtualenv
* selenium
* [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

## Usage
* virtualenv ENV
* source ENV/bin/active
* pip install selenium
* python unfollow.py
* enter your username and password
