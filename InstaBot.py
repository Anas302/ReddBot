import os
from instabot import Bot
from ReddBot import ReddBot
import shutil


try:
    shutil.rmtree("config")
except OSError:
    print("no \'config\' directory has been removed")

PASSWORD = "<Instagtam account password>"
USERNAME = "<instagram account username>"
bot = Bot()
bot.login(username=USERNAME, password=PASSWORD)


def remove_files(*files):
    for i in files:
        if os.path.exists(i):
            os.remove(i)
        else:
            print(f"File {i} wasn't found")


def login_into_instagram_and_upload_images(image):
    global bot

    bot.upload_photo(image, caption=f"\n {ReddBot.links[0][23:len(ReddBot.links[0]) - 4]}\n\n Follow for more random "
                                    f"reddit content!\n \n \n \n \n \n #memes #reddit #usa #uk #jokes #funny #like "
                                    f"#follow #girl #instagram #redditmemes #photo #meme #memestagram #funnyposts "
                                    f"#explore #9gag #epicmemes #explorepage #showerthoughts #im14andthisisdeep "
                                    f"#wholesomememes #wholesome #dankmeme #like #hot #dankmemes #dankmemesdaily "
                                    f"#tiktok #likes #follow")
    remove_files("mainpost.png", "mainpost.jpg.REMOVE_ME", "mainpost.jpg")
