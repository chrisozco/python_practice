from operator import truediv


class User:
    def __init__ (self, first_name, last_name, email, age, points):
        self.name = first_name
        self.last = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = points
    def display_info(self):
        print("////////////")
        print(f"First Name: {self.name}")
        print(f"Last name: {self.last}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")
    def enroll(self):
        if self.is_rewards_member == False:
            print("User already a member")
        else: self.is_rewards_member = True
    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount


Chris = User('Chris', 'Orozco', 'chris@bank.com', 25, 280)
Harper = User('Harper', 'Hahn', 'harper@bank.com', 24, 440)
Todd = User('Todd', 'Parker', 'tod@bank.com', 18, 360)
Chris.display_info()
Harper.display_info()
Todd.display_info()
Todd.spend_points(50)
Harper.enroll()
Harper.spend_points(80)
Harper.display_info()
Todd.display_info()
