class User:
    def __init__(self, f_name,l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.followers = 0
        self.following = 0
    def follow(self, user):
        user.followers +=1
        self.following +=1

user_one = User("John", "Sam")
user_two = User("John", "Smith")

user_one.follow(user_two)
user_two.follow(user_one)
print(user_one.following)
print(user_one.followers)
print(user_two.following)
print(user_two.followers)
