#! python3
import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id='bojiXmJKJFIRZA', \
                     client_secret='LMPva-WqecOZ9z2hOmEdTIszxBm_sg', \
                     user_agent='YOUR_APP_NAME', \
                     username='greenirishsaint', \
                     password='4ZYfX6L0H03f')

subreddit = reddit.subreddit('UCO')
top_subreddit = subreddit.top(limit=500)

topics_dict = { "title":[], "score":[], "id":[], "url":[], "comms_num": [], "created": [], "body":[] }
for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)

def get_date(created):
    return dt.datetime.fromtimestamp(created)
_timestamp = topics_data["created"].apply(get_date)
topics_data = topics_data.assign(timestamp = _timestamp)

topics_data.info()
comms_dict = { "topic": [], "body":[], "comm_id":[], "created":[] }

iteration = 1
for topic in topics_data["id"]:
    print(str(iteration))
    iteration += 1
    submission = reddit.submission(id=topic)
    for top_level_comment in submission.comments:
        comms_dict["topic"].append(topic)
        comms_dict["body"].append(top_level_comment.body)
        comms_dict["comm_id"].append(top_level_comment)
        comms_dict["created"].append(top_level_comment.created)

print("done")
comms_data = pd.DataFrame(comms_dict)
comms_data

timestamps = comms_data["created"].apply(get_date)

comms_data = comms_data.assign(timestamp = timestamps)
topics_data.to_csv("subreddit_UCO_topics.csv")
comms_data.to_csv("subreddit_UCO_comments.csv")
