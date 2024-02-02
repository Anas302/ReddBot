from ReddBot import scrape
from ReddBot import IM14ANDTHISISDEEP, WHOLESOME, MEMES, FUNNY, DANKMEMES, \
    SOFTWAREGORE, CRAPPYDESIGN, IHADASTROKE, MILDLYINFURIATING, MILDLYINTERESTING, PICS, WTF, TECHSUPPORTGORE, \
    PEWDIEPIESUBMISSIONS, ENGRISH, TECHNICALLYTHETRUTH, HOLUP, ANTIMEME, YOUNGPEOPLEYOUTUBE, TUMBLR, \
    WHITEPEOPLETWITTER, POLITICALHUMOR, PUNS, ODDLYSPECIFIC
from cropper import crop
from interface import initate_interface


subreddits = [WTF, ODDLYSPECIFIC, POLITICALHUMOR, TECHNICALLYTHETRUTH, PEWDIEPIESUBMISSIONS, WHITEPEOPLETWITTER,
              CRAPPYDESIGN, FUNNY, IM14ANDTHISISDEEP, MEMES, MILDLYINTERESTING, TUMBLR, SOFTWAREGORE, IHADASTROKE,
              WHOLESOME, ANTIMEME, PICS, PUNS, MILDLYINFURIATING, DANKMEMES, ENGRISH, TECHSUPPORTGORE, HOLUP]


def start(counter):
    scrape(subreddits[counter])
    crop("mainpost.png")
    initate_interface()


if __name__ == "__main__":
    while True:
        for i in range(len(subreddits)):
            print(f"scraping: {subreddits[i][0][23:len(subreddits[i][0]) - 1]}")
            start(i)


'''
To Add a new Subreddit, the following must be done:

1) Add a new variable at ReddBOAt.py with the name of the subreddit, the link, PostID and whether it contains images
2) The postID can be any number for now, just put a number between 10 and 30
3) Go to ReddBOAT.click_first_post() and un-comment the grey lines of code
3) Run the code and observe the scraping of the subreddit
4) Each number would indicate the ID of the text, determine the number of the first post
5) Change the postID number from what you previously added to the new number you observed
6) Congrats you added a new subreddit!
'''
