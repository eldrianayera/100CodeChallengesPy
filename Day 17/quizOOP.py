class User :
    def __init__(self,user_id , name):
        self.id = user_id
        self.username = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User(771, 'Robert')
user_2 = User(323, 'Adam')

user_1.follow(user_2)
print(user_1.followers)
print(user_2.followers)
print(user_1.following)
print(user_2.following)


