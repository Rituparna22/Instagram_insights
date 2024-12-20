import instaloader
import pandas as pd
import matplotlib.pyplot as plt
import os
from tabulate import tabulate

# Initialize Instaloader
L = instaloader.Instaloader()

# Define the username (for a specific user)
username = 'thebookishgoof'  # Change this to the desired username

# Load the profile of the user
profile = instaloader.Profile.from_username(L.context, username)

# List to store the user’s posts data
user_posts_data = []

# Iterate through the posts of the user
for post in profile.get_posts():
    post_data = {
        'username': post.owner_username,
        'full_name': post.owner_profile.full_name,  # Access full name from profile
        'bio': post.owner_profile.biography if hasattr(post.owner_profile, 'biography') else 'N/A',
        'location': post.location.name if post.location else 'N/A',
        'content': post.caption,
        'likes': post.likes,
        'views': post.video_view_count if post.is_video else 0,
        'date_posted': post.date_utc,
        'tags': post.caption_hashtags,
    }
    user_posts_data.append(post_data)

# Convert to DataFrame
df_user_posts = pd.DataFrame(user_posts_data)
file_name = 'excel_posts.xlsx'
df_user_posts.to_excel(file_name)
print('DataFrame is written to excel file succesfully')
# Save the table to an HTML file
html_file_path = "user_posts_table.html"
df_user_posts.to_html(html_file_path, index=False, escape=False)  # Save as an HTML file without escaping HTML characters
print(f"Current working directory: {os.getcwd()}")
print(f"HTML file has been saved at {html_file_path}")

#Use tabulate to print the DataFrame in a tabular format (optional for console display)
#print(tabulate(df_user_posts, headers='keys', tablefmt='grid', showindex=False))

# Visualizing the number of likes and views for each post
df_user_posts[['likes', 'views']].plot(kind='bar', figsize=(12, 6))
plt.title(f'Likes and Views for {username}')
plt.ylabel('Count')
plt.xlabel('Post Number')
plt.xticks(rotation=90)
plt.show()
