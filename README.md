# Six degrees of Wikipedia

According to Wikipedia:
> Six degrees of separation is the idea that all people are six, or fewer, social connections away from each other. Also known as the 6 Handshakes rule. As a result, a chain of "a friend of a friend" statements can be made to connect any two people in a maximum of six steps.

This spider crawls through Wikipedia and outputs all the articles that can be reached with six links or less from a set starting point.

## Objectives
The aim of this project is to serve as an introduction to web scraping but mainly as a toy for personal amusement. It's for that purpose that I've laid down a few rules:
1. No meta articles (excluding lists of other articles e.g. "List of programming languages")
2. No sidebar (just using the "Random article" link would eventually lead you to the entirety of the wiki)
3. No main page (it adds a random element to the game as it changes everyday)

## Usage
`./scrape [ -d DEPTH_LIMIT ] START_URL OUTPUT_FILE`

* START URL: the Wikipedia article URL to start scraping from.
* OUTPUT_FILE: the file the results are stored in. CSV, JSON and XML formats are supported.
* DEPTH_LIMIT (optional): stops collecting data at a certain number of handshakes. This program has only been tested up to depth 3, because of computational limitations. Additionally, it's impolite to send so many requests to Wikipedia in such a short timeframe.
