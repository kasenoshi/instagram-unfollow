# instagram-unfollow
unfollow all automatically through selenium
* note that Instagram has a limit for unfollowing (15 in 15 minutes, no more than 1000 per day)

* Tested on python 3.7.3
* Tested on Mac 10.15.7 with Selenium 3.141.0, ChromeDriver 86.0.4240.22
* Tested on Instagram on Nov 13th, 2020

## Dependency
* virtualenv
* selenium
* [ChromeDriver](https://chromedriver.storage.googleapis.com/index.html)
  * Download the ChromeDriver meet your chrome's version
  * Include ChromeDriver on the path
  * $ export PATH="$PATH:/path/to/chromedriver"

## Usage
* $ python3 -m venv ENV
* $ source ENV/bin/active
* $ pip install selenium
* edit config.json
* $ python unfollow.py
* enter your username and password
