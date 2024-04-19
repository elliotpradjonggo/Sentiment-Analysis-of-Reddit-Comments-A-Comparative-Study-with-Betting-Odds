import praw
from praw.models import MoreComments

reddit = praw.Reddit(
        client_id='z-mqMKI-8P2VI_WAI3iQnw',
        client_secret='zaEJv8zThrJd1fOJOLIoquYjNKXQMQ',
        password='rxVBY6e4#u2\'n9A',
        user_agent='test script',
        username='Amazing_Sir8976')

url = 'https://www.reddit.com/r/soccer/comments/1bscv3u/match_thread_manchester_city_vs_arsenal_english/'

submission = reddit.submission(url=url)

for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    print(top_level_comment.body, top_level_comment.created_utc)
