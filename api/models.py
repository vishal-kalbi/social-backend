from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User model with additional fields for email, profile picture, bio, and website
class User(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.FileField(upload_to='profile_pictures/', default='default.jpg', blank=True)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.username


# Model representing a user profile, which includes followers and additional info
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"


# Model representing a post made by a user, including an image, caption, and timestamp
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = models.FileField(upload_to='posts/')
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s post"


# Model representing comments on a post, with a reference to the post, the user who commented, and the comment text
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.id}"


# Model representing likes on a post, with a reference to the post and the user who liked it
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like by {self.user.username} on {self.post.id}"


# Model representing the follow relationship between users
class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"


# Model representing a story posted by a user, including an image or video and timestamp
class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories')
    content = models.FileField(upload_to='stories/')  # Can be an image or video
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  # To handle story expiration

    def __str__(self):
        return f"{self.user.username}'s story"


# Model representing comments on a story, with a reference to the story and the user who commented
class StoryComment(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.story.id}"


# Model representing likes on a story, with a reference to the story and the user who liked it
class StoryLike(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like by {self.user.username} on {self.story.id}"
