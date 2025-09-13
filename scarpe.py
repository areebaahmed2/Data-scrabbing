import praw
import csv

reddit = praw.Reddit(
    client_id="p_lNKQmz_o8UCtCeOekHfQ",
    client_secret="qrRwMwD1PhmrXsEYTYqjp-AETN0bGg",
    user_agent="windows:student_scraper:1.0 (by /u/IntelligentActive843)"
)

subreddit = reddit.subreddit("InternationalStudents")

user_data = []

for post in subreddit.search("exam help", limit=50):
    text = f"{post.title} {post.selftext}"
    if "international" in text.lower():
        user_name = post.author.name if post.author else "[deleted]"
        user_link = f"https://www.reddit.com/user/{user_name}" if post.author else "[deleted]"
        post_link = f"https://www.reddit.com{post.permalink}"
        user_data.append([f'=HYPERLINK("{user_link}", "{user_name}")', f'=HYPERLINK("{post_link}", "Post Link")'])

with open("student_ids_and_posts.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["User Profile", "Post Link"])
    writer.writerows(user_data)

print(f"Extracted {len(user_data)} clickable user profile and post links to student_ids_and_posts.csv")
