import praw
from praw.models import MoreComments
import datetime
import json
import time


reddit = praw.Reddit(
        client_id='z-mqMKI-8P2VI_WAI3iQnw',
        client_secret='zaEJv8zThrJd1fOJOLIoquYjNKXQMQ',
        password='rxVBY6e4#u2\'n9A',
        user_agent='test script',
        username='Amazing_Sir8976')

subreddit = reddit.subreddit('soccer')

with open('output.json', 'r') as json_file:
    # Load the JSON data
    """
    match_det = data[x]
    match_det[match_date]
    match_det[start_time]
    match_det[team1_name]
    match_det[team2_name]

    odds = match_det[match_odds]
    odds[date]
    odds[time]
    odds[team1]
    odds[team2]
    odds[draw]
    """
    data = json.load(json_file)

jsonData = []

for match in data:
    match_date = match['match_date']
    start_time = match['start_time']
    title = 'Match Thread: ' + match['team1_name'] + ' vs ' + match['team2_name'] + " English"
    for submission in subreddit.search(title, sort='relevance', time_filter='all'):

        match_date_time = datetime.datetime.strptime(f"{match_date} {start_time}", "%Y-%m-%d %H:%M:%S")
        post_date_time = datetime.datetime.fromtimestamp(submission.created_utc)
        time_difference = match_date_time - post_date_time

        if time_difference <= datetime.timedelta(hours=12) and time_difference >= datetime.timedelta(hours=0):
            url = (submission.url)
            submission = reddit.submission(url=url)
            comments = []
            for top_level_comment in submission.comments:
                if isinstance(top_level_comment, MoreComments):
                    continue
                date_time = datetime.datetime.fromtimestamp(top_level_comment.created_utc)
                comments.append({
                    'time': str(date_time),
                    'comment': top_level_comment.body
                })
            jsonData.append({
                'title': title,
                'match_date': match_date,
                'comments': comments
            })

with open('comments.json', 'w') as json_file:
    # for item in jsonData:
    #     item['match_odds'] = json.dumps(item['match_odds'])
    json.dump(jsonData, json_file, indent=4)

# url = 'https://www.reddit.com/r/soccer/comments/wc3ddk/post_match_thread_liverpool_31_manchester_city_fa/'



# submission = reddit.submission(url=url)
# date = datetime.datetime.fromtimestamp(submission.created_utc)
# print(date)
# for top_level_comment in submission.comments:
#     if isinstance(top_level_comment, MoreComments):
#         continue
#     time = datetime.datetime.fromtimestamp(top_level_comment.created_utc)
#     print(top_level_comment.body, time)


