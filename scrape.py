
import requests
from bs4 import BeautifulSoup
import pprint


#grab html files

def grab_requests(url):
    return requests.get(url)

# convert html into an object we can parse

def parse_requests(res):
    return BeautifulSoup(res.text, "html.parser")




def sort_stories_by_vote(hnlist):
    #Pass dictionary's sort key[votes] to lambda function
    return sorted(hnlist, key = lambda k:k['votes'], reverse=True)

#combine links and votes to achieve objective

def create_cutom_hn(links, subtext):
    #New List
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points',''))
            if points > 99:
                #Using href to combine title, dictionary and points
                hn.append({'title': title, 'link': href, 'votes': points})

    return sort_stories_by_vote(hn)

def main():
    req1 = grab_requests('https://news.ycombinator.com/news')
    req2 = grab_requests('https://news.ycombinator.com/news?p=2')
    soup = parse_requests(req1)
    soup2 = parse_requests(req2)
    links = soup.select('.storylink')
    # to capture element not with 0 points
    subtext = soup.select('.subtext')
    links2 = soup2.select('.storylink')
    subtext2 = soup2.select('.subtext')
    # combine the inputs
    mega_links = links + links2
    mega_subtext = subtext + subtext2
    pprint.pprint(create_cutom_hn(mega_links, mega_subtext))

if __name__ == '__main__':
    main()
