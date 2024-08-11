Analyzing Soccer Match Dynamics: A Study of Fan Sentiments and Betting Odds
Elliot Pradjonggo, Jake Reardon
May 17, 2024


Abstract

We explore the potential of using the sentiment of live Reddit comments as indicators of a soccer team’s performance throughout a match. Using an average of 320 comments per match from Reddit’s r/soccer subreddit’s live match threads across 53 matches, aiming to analyze the correlation between fan sentiment with real-time changes in betting odds at discrete time intervals to measure the match dynamics, reflecting whether a team is performing better or worse than expected. We utilize the Python Reddit API Wrapper (PRAW) to collect and process the comments, and we get the betting odds from the Betfair website. Our findings demonstrate a significant correlation between spikes in positive or negative sentiment and fluctuations in betting odds. This suggests that fan reactions on Reddit can reflect and potentially anticipate shifts in team performance as perceived by the betting market. This study underscores the value of social media sentiment analysis in enhancing real-time sports analytics.

Introduction

In recent years, the proliferation of social media platforms has opened new ways for real-time data analysis in various fields, including sports analytics. One such platform, Reddit, hosts live match threads where fans actively comment on ongoing soccer matches, providing many sources of real-time sentiment data. This study aims to explore the potential of live Reddit comments as indicators of soccer team performance dynamics during matches.

The motivation behind this research lies in the hypothesis that fan sentiment, as expressed in live match threads, correlates with and can even anticipate changes in team performance. Specifically, we seek to correlate fan sentiment with real-time changes in betting odds at discrete time intervals. Betting odds are a quantifiable measure of the perceived probability of a team's success, reflecting whether a team is performing better or worse than expected.


To investigate this hypothesis, we analyzed an average of 320 comments per match from the r/soccer live match threads across 53 matches. We utilized the Python Reddit API Wrapper (PRAW) to collect and process the comments, extracting sentiment data in real-time. Concurrently, we obtained betting odds from the Betfair website to measure the perceived performance dynamics of the teams.

Our approach involves identifying spikes in positive or negative sentiment in the Reddit comments and correlating these with fluctuations in the betting odds. The results of our study demonstrate a significant correlation between these sentiment spikes and changes in betting odds. This suggests that fan reactions on Reddit can reflect and potentially anticipate shifts in team performance as perceived by the betting market.

This research underscores the value of social media sentiment analysis in enhancing real-time sports analytics. By leveraging the immediate and unfiltered reactions of fans, we can gain insights into the dynamics of team performance that are not immediately apparent from traditional performance metrics alone. Our findings open up new possibilities for integrating social media sentiment into sports analysis frameworks, potentially improving the accuracy and responsiveness of performance assessments.

Related Work

The intersection of sports analytics, sentiment analysis, and betting strategy has been a subject of interest in recent research. Several studies have explored this area, providing valuable insights and methodologies that informed our approach.

One study titled “Predicting Soccer Results through Sentiment Analysis: A Graph Theory Approach” [1] proposed a deep-learning model that used polarity on a dataset of 3,000 tweets taken during the last game week of the English Premier League.. The researchers aimed to understand sports communities in Social Networks and identified fan’s expertise as a key indicator for soccer prediction. The model gave a probability of a winning game for either time by evaluating the network of comments. “Using Twitter to predict football outcomes” [2] used X data to predict the outcomes of soccer matches, using hashtags to collect relevant posts. They built predictive models for the outcome of soccer games of the English Premier League based on posts and found that these models can outperform predictive models which use only historical data and simple football statistics. Using data from X alone, with a random forest classifier, they achieved a mean of 58.8% accuracy. They found that combining X data and historical data together performed best, achieving a mean accuracy of 69.6%.

Although the amount of prior work relating online posts to soccer matches instill confidence, none have tried to see how posts are correlated with the state of a match throughout the match, only how posts are related to the match’s end result. Another distinction is that prior works aim to predict the outcome of a match (a future event), while this experiment aims to find a relationship between the sentiment of online posts with a match in the present.

Data

The experiment required the collection of online comments with timestamps, separated by match, and betting data for either team separated by match.

Live comments were gathered from Reddit’s r/soccer “match threads”, threads created specifically by subreddit administrators for the discussion of a specific match in real-time as it occurs. The platform’s structure made it an easy choice: discussions on a single topic are organized into individual standalone threads. Using posts from X would require identifying whether a post was addressing soccer, identifying which match the post was referring to, etc., while on Reddit that information is implied by the thread itself. The soccer subreddit was deliberately chosen in an attempt to minimize commenter bias. Obviously almost all commenters are partial to a given team, but taking comments from the main soccer subreddit has the advantage of drawing comments from fans of all teams. A commenter in the Liverpool subreddit may be likely to comment only when Liverpool is performing well. The Python Reddit API Wrapper was used to save the text contained in each top-level comment (a main comment, not a reply) from each specific thread along with the time it was posted, which were initially stored as a JSON file. Match threads contained an average of 320 comments. Comments collected with PRAW did not require any additional manipulation or cleaning. PRAW does not properly preserve emojis when downloading content, however, emojis are less common on Reddit than on other social media platforms, so this is less important than if another platform was being used, like X.

Each comment was to be given two labels, each corresponding with the sentiment towards either team. Each comment’s sentiment towards either team was to be labeled as positive, negative or neutral. Examples can be seen below:






Comment
Sentiment, Arsenal 
Sentiment, Chelsea
“Imagine conceding to Chelsea.”
Negative
Neutral
“With this win Arsenal have twice as many points as Chelsea this season”
Positive
Negative
“Find the person pointing the laser and lock them up.”
Neutral
Neutral



Defining a standard as to what constitutes a positive, negative or neutral sentiment is particularly challenging for online comments, where the frequent use of slang can make it difficult for an outsider to understand what a commenter truly means. A comment’s sentiment was said to be positive if the commenter seemed to be speaking positively about the team's performance, regardless of how the commenter seemed to feel about it. Similarly, the same definition is applied for negativity. For example, the sentiment of the comment “looks like liverpools gonna win this one, i really hate to see it” is said to be positive because although the commenter seems to not like Liverpool, the commenter is acknowledging that they're performing well, which is the metric of interest. A comment that does not address either team is said to be neutral, although it’s obvious that not addressing a team does not guarantee neutral sentiment: a comment about an unfair penalty is often really revealing how a commenter is feeling about the game. Manually looking at how the game was going at the time that the comment was left could be used to infer the sentiment, however, this was not feasible to do individually across thousands of comments.

The Betfair betting odds for a team throughout a match is used as a proxy for a team’s true performance at a given time. “Betting odds” for a given team refers to the monetary return a Betfair user would get if that team won the match. If a team is projected to win, the team’s odds decrease because there’s far less risk in betting on their victory, and if a team’s projected to lose, the team’s odds increase because there’s more risk in betting on their victory. Therefore, a decrease in betting odds indicates good performance, while an increase in betting odds indicates poor performance. It was found that the change in odds over a given time window was far more indicative of a team’s performance than the raw odds, to be discussed later.



Betfair betting odds were downloaded directly from Betfair Historical Data, which provides time-stamped betting data for past matches. Data was downloaded in the JSON file format, with each entry containing a timestamp and the betting odds for either team. Odds are stored at discrete time intervals, however, the time differences between entries are not quite regular, with odds being recorded with anywhere between 30 seconds and 2 minutes between. Still, with only hundreds of comments and thousands of betting odd entries per match, the sparsity of comment data during certain time windows became the “limiting factor” during analysis.

Data Processing

By combining these datasets, we were able to analyze the relationship between fan sentiment and betting odds in real time. This comprehensive dataset allowed us to explore how changes in fan reactions correspond to shifts in perceived team performance, providing valuable insights into the dynamics of soccer matches.

Method

To investigate the relationship between live Reddit comments and betting odds during soccer matches, we have to do sentiment analysis, and correlation analysis.

Sentiment Analysis

We performed sentiment analysis on the Reddit comments to determine whether each comment was positive, negative, or neutral. We labeled them positive, negative or neutral, represented as 1, -1 or 0, respectively. To label such a large set of comments, we used OpenAI’s GPT-4 by manually annotating the first 10 and giving the match information such as the team names and the team rosters.


Assumptions

Several assumptions were made for the design of the experiment, the most fundamental of which is related to the betting odds. Because betting odds are being used as a proxy for a team’s performance, and the odds themselves are not the measure of interest, it was assumed that the betting odds were representative of a team’s true performance throughout the match. Many factors play a role in the actual odds throughout the game, including the betting decisions of Betfair users and game information like scoring and injuries. Therefore, assuming that the odds reflect the true state of the game means assuming that fans are (collectively, at least) betting rationally and that Betfair’s analysts are utilizing game information effectively. Betters have a monetary incentive to wager rationally, and analysts have a career incentive to utilize information effectively, so this is a reasonable assumption to make. If there was a significant disconnect between betting odds and the true state of a match, they would be exploited often and Betfair would struggle to profit. The well-known difficulty of “beating the odds” in sports betting is reflective of how effectively the odds are often set and moved.

It’s also assumed that comments reflect a commenter’s feelings about the match at a time that’s reasonably close to the attached timestamp. When a game-altering event occurs, there will always be a delay between the occurrence of the event and the posting of a comment that the event caused. This means that the timestamp attached to a comment is actually later in time then the state of the match that the comment is describing. The assumption made is that this delay is small enough to be neglected. When posting online comments, users typically prioritize typing speed over correct spelling, capitalization and grammar, especially in a “live thread” where users tend to race to post their observations before others do. It’s reasonable to assume that users post their thoughts within minutes of an important event taking place, as most comments are only a sentence long.

The least certain assumption made is that comments were made in response to the match itself, and not simply in response to other comments. More formally, it was assumed that comments were independent of each other. However, social media users sometimes try to post comments that align with the feelings of others in order to get positive feedback, in the form of upvotes for Reddit. 





Correlation Analysis

To analyze the relationship between comment sentiment and betting odds, it was necessary to “align” them in some way because entries for comments and odds occur at different times, and neither are distributed uniformly over time. To accommodate this, rather than using the betting odds on their own, we looked at the change in betting odds over different time intervals. The change in odds at time ti is computed as
(odds(ti)-odds(ti-1))/(ti-ti-1).

The “overall sentiment” at time ti is computed as the sum of the sentiment values in the 5-minute window,
 j=1nsj, j=1,2,...,n,
Where sj is the sentiment of the jth comment in the time window.

These values were not normalized by count because the number of comments in a given time interval could indicate the importance of an event. For example, if a major event occurs, many users will comment on it, and if a minor event occurs, fewer users would comment on it, which should be reflected in the overall sentiment. If values were normalized by count, this information would be lost.


Results

Experimental Setup

To understand the relationship between sentiment analysis and odds changes in sports betting, we conducted an experiment focusing on a specific football match between Manchester City and Chelsea on May 21, 2023. We collected data from a Reddit live match thread, analyzing the sentiments expressed by users in real-time. Our primary objective was to determine if changes in public sentiment, as measured through Reddit comments, could predict changes in betting odds.






Baseline Method

The baseline method for our experiment involved using historical betting odds and sentiment data without any advanced feature engineering or modeling. We calculated the correlation between the sum of sentiment in one-minute intervals and the corresponding changes in betting odds. This simple correlation analysis served as a benchmark to evaluate the effectiveness of more sophisticated methods.


Figure 1: Value changes in odds for a match between Man City and Chelsea on 2023-05-21


Figure 2: Sum of Sentiment in a 1 minute interval for a match between Man City and Chelsea on 2023-05-21

Figure 1 displays the fluctuations in betting odds for the match over the course of the game. Figure 2 shows the aggregated sentiment scores in one-minute intervals throughout the match.

Our analysis revealed a notable correlation between the sentiment data from the Reddit live match thread and the odds changes. Specifically, peaks in positive or negative sentiment were often followed by corresponding adjustments in betting odds. This suggests that public sentiment, as captured through our methods, has predictive value for betting markets.

Discussion and Future Work

There’s certainly a correlation between the sentiment of online comments and the state of a soccer match. In this experiment, the sparsity of comments at certain times throughout the match posed a challenge when analyzing the relationship, because there wasn’t enough data to represent the true sentiment of fans. For some matches, even 10 minute windows would only have one or zero comments in each window. In future work, this could be remedied by collecting data from threads across more subreddits, although new problems may arise, as discussed previously in Data. 

As sports betting platforms aim to anticipate the way betters will place wagers when adjusting betting odds, the sentiment of online discussion could become another factor that sports betting platforms could use to move the odds throughout a match. 

Works Cited

[1] Miranda-Peña, Clarissa, et al. “Predicting Soccer Results through Sentiment Analysis: A Graph Theory Approach.” International Conference on Computational Science, 2021.
[2] Kampakis, Stylianos, and Andreas Adamides. “Using Twitter to Predict Football Outcomes.” arXiv preprint arXiv:1411.1243 (2014)
