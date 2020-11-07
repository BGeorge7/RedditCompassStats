import praw
import sys
import json
import os

#sys.stdout = open('.\\comments.txt', 'w')
sys.path.append(".")

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
j = open(os.path.join(__location__, 'config.json'))
config = json.load(j)

from commentInfo import SubmissionCommentInfo
from ideology import Ideology
from threadstats import ThreadStats

reddit = praw.Reddit(
                    client_id="7R4qFh50EcFCUg",
                    client_secret=str(config['secret']),
                    user_agent="Mr0reo User Agent") #Creates the reddit instance with a particular app

# for submission in reddit.subreddit("conservative").hot(limit=20):
#     print(submission.link_flair_text)
#     print("---------------")

# sub = reddit.submission(url = "https://www.reddit.com/r/PoliticalCompassMemes/comments/jj9yjg/wait_authleft_actually_likes_china_and_stalin_i/")
# print (vars(sub.comments[0]))
# print(sub.comments[0].author_flair_text)

# listx = sub.comments.list()

# count = 1
# for comment in sub.comments:
#     print(f"Comment {count} Flair: {comment.author_flair_text}")
#     count += 1

def populate_thread(listx): #Compiles a comment thread into a list of easy to proccess information about each comment
    myThread = []

    idy = Ideology.NONE

    for comment in listx:

        if(str(comment.author_flair_text) == ":centrist: - Centrist"): #Centrist
            idy = Ideology.CENTRIST
        elif(str(comment.author_flair_text) == ":authright: - AuthRight"): #Auth Right
            idy = Ideology.AUTHRIGHT
        elif(str(comment.author_flair_text) == ":authleft: - AuthLeft"): #Auth Left
            idy = Ideology.AUTHLEFT
        elif(str(comment.author_flair_text) == ":libleft: - LibLeft"): #Lib Left
            idy = Ideology.LIBLEFT
        elif(str(comment.author_flair_text) == ":libright: - LibRight"): #Lib Right
            idy = Ideology.LIBRIGHT
        elif(str(comment.author_flair_text) == ":auth: - AuthCenter"): #Auth Center
            idy = Ideology.AUTHCENTER
        elif(str(comment.author_flair_text) == ":left: - Left"): #Left
            idy = Ideology.LEFT
        elif(str(comment.author_flair_text) == ":lib: - LibCenter"): #Lib Center
            idy = Ideology.LIBCENTER
        elif(str(comment.author_flair_text) == ":right: - Right"): #Right
            idy = Ideology.RIGHT
        elif(str(comment.author_flair_text) == ":libright2: - LibRight"): #Lib Right 2 (I know I made them the same shut the fuck up)
            idy = Ideology.LIBRIGHT
        elif(str(comment.author_flair_text) == ":CENTG: - Centrist"): #Centrist 2 (I know I made them the same to shut the fuck up)
            idy = Ideology.CENTRIST
        
        myThread.append(SubmissionCommentInfo(
            idy, 
            comment.score,
            comment.author,
            comment.permalink,
            comment.controversiality,
            comment.total_awards_received))
    return myThread

def main():
    topThreads = []
    stats = ThreadStats()

    for submission in reddit.subreddit("PoliticalCompassMemes").top("month",limit=2):
        print("Fetching thread.....")
        submission.comments.replace_more(0)
        topThreads.append(populate_thread(submission.comments.list()))

    for thread in topThreads:
        print("Compilling Data...")
        for comment in thread:
            stats.count_increment(comment, accountSameUserComments=True)
            #print(f"Ideology: {str(comment.get_ideology())}, Score {str(comment.get_score())}, Author Username: {str(comment.get_authorUserName())},\nPermalink: {str(comment.get_permalink())},\nControversiality: {str(comment.get_controversiality())}, Awards: {str(comment.get_totalAwards())}")
            #print("")

    stats.ideology_breakdown()

if __name__ == "__main__":
    main()