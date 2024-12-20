import instaloader

# Instantiate the Instaloader object
L = instaloader.Instaloader()

# Load the profile
profile = instaloader.Profile.from_username(L.context, "thebookishgoof")

# Print some profile details
print(f"Username: {profile.username}")
print(f"Followers: {profile.followers}")
print(f"Following: {profile.followees}")
print(f"Posts: {profile.mediacount}")
