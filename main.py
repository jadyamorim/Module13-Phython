from user import User
from post import Post

app_user_one = User("jady@yam.com", "Jady Amorim", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()

app_user_two = User("aa@aa.com", "John Doe", "supersecret", "Developer")
app_user_two.get_user_info()

new_post = Post("learning today", app_user_one.name)
new_post.get_post_info()

new_post = Post("writing code today", app_user_two.name)
new_post.get_post_info()
