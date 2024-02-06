class User:
    # Init function is called the constructor - this data (the attributes) must now be provided as below...
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Henry Jones")
user_2 = User("002", "Angela Gallagher")

# user_1.id = "001"
# user_1.username = "Henry Jones"

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
