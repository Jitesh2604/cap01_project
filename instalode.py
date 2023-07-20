# With the the help of this code you can download anything from instagram profile

# Imprort prfile from instagram with the help of instaloader
import instaloader
insta = instaloader.Instaloader()

user = input("Enter the Instagram profile Username")

insta.download_profile(user,profile_pic_only=True)