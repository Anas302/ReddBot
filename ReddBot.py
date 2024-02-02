from selenium import webdriver


class ReddBot(object):
    chrome_options = webdriver.ChromeOptions()
    PATH = r"C:\Program Files (x86)\chromedriver.exe"
    links = []

    def __init__(self, link, postID, needsTitle):
        self.postID = postID
        self.link = link
        self.needsTitle = needsTitle
        print(f"link: {self.link}")

        if len(ReddBot.links) == 2:
            ReddBot.links.clear()

        ReddBot.links.append(self.link)
        ReddBot.chrome_options.add_argument("--disable-notifications")
        ReddBot.chrome_options.add_argument('headless')

        print("Notifications Disabled...")
        self.driver = webdriver.Chrome(ReddBot.PATH, options=ReddBot.chrome_options)
        print("Initiating ReddBOAT...")
        self.driver.get(self.link)

    def scrollpage(self, units):
        self.driver.execute_script(f"window.scrollTo(0, {units});")
        print(f"Comment at y = {units} has been located...")

    def take_scrnshot(self, img_name):
        self.sh = self.driver.get_screenshot_as_file(img_name)
        print("Taking a screenshot...")

    def click_first_post(self):
        self.body = self.driver.find_elements_by_tag_name("a")
        self.desired_post = self.body[self.postID]
        self.desired_post.click()
        print("The first post has been clicked...")
        self.postURL = self.driver.current_url

    def open_comment_section(self):
        if self.needsTitle:
            self.driver.execute_script("window.scrollTo(0, 53);")  # (0,53)-with text  (0,100)-without
        else:
            self.driver.execute_script("window.scrollTo(0, 100);")  # (0,53)-with text  (0,100)-without
        self.take_scrnshot("mainpost.png")


# NAME = "www.link.com", first_post_ID, needsTitle
IM14ANDTHISISDEEP = "https://www.reddit.com/r/im14andthisisdeep/", 14, True
WHOLESOME = "https://www.reddit.com/r/wholesome/", 14, True
MEMES = "https://www.reddit.com/r/memes/", 18, False  #
FUNNY = "https://www.reddit.com/r/funny/", 19, False  # 18
DANKMEMES = "https://www.reddit.com/r/dankmemes/", 20, False  # 19
SOFTWAREGORE = "https://www.reddit.com/r/softwaregore/", 19, True  #
CRAPPYDESIGN = "https://www.reddit.com/r/CrappyDesign/", 14, True  #
IHADASTROKE = "https://www.reddit.com/r/ihadastroke/", 16, True  #
WTF = "https://www.reddit.com/r/WTF/", 14, False
MILDLYINFURIATING = "https://www.reddit.com/r/mildlyinfuriating/", 20, True  #
PICS = "https://www.reddit.com/r/pics/", 17, True  #
MILDLYINTERESTING = "https://www.reddit.com/r/mildlyinteresting/", 25, True
TECHSUPPORTGORE = "https://www.reddit.com/r/techsupportgore/", 14, True
PEWDIEPIESUBMISSIONS = "https://www.reddit.com/r/PewdiepieSubmissions/", 18, False  #
ENGRISH = "https://www.reddit.com/r/engrish/", 14, True  #
TECHNICALLYTHETRUTH = "https://www.reddit.com/r/technicallythetruth/", 14, False  #
HOLUP = "https://www.reddit.com/r/HolUp/", 18, False  # 17
ANTIMEME = "https://www.reddit.com/r/antimeme/", 14, False
YOUNGPEOPLEYOUTUBE = "https://www.reddit.com/r/youngpeopleyoutube/", 16, True  # 18
TUMBLR = "https://www.reddit.com/r/tumblr/", 14, False  #
WHITEPEOPLETWITTER = "https://www.reddit.com/r/WhitePeopleTwitter/", 14, False
POLITICALHUMOR = "https://www.reddit.com/r/PoliticalHumor/", 14, False
PUNS = "https://www.reddit.com/r/puns/", 16, False
ODDLYSPECIFIC = "https://www.reddit.com/r/oddlyspecific/", 14, False


def scrape(subreddit):
    web = ReddBot(subreddit[0] + "top", subreddit[1], subreddit[2])
    web.click_first_post()
    web.driver.close()
    web = ReddBot(str(web.postURL), subreddit[1], subreddit[2])
    web.open_comment_section()
    web.driver.close()
