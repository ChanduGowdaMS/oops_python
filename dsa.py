class Instagram:
    def __init__(self,title, description, location, creator):  
        self.title = title
        self.description = description
        self.location=location
        self.creator=creator
        self.likes = 0
        self.comments=[]
    def display_title(self):
        print("The title of the reel is ",self.title)
    def display_description(self):
        print("The description of the reel is ",self.description)
    def display_likes(self):
        print("The likes of the reel is ",self.likes)
    def display_location(self):
        print("The location of the reel is ",self.location)
    def display_creator(self):
        print("The creator of the reel is ",self.creator)
    def display_comments(self):
        if len(self.comments)==0:
            print("there is no comment")
        else:
            print("the comments of reel")
            for comment in self.comments:
                print(comment)
   
    def liked(self):
        self.likes += 1
    def disliked(self):
        if self.likes > 0:
            self.likes-=1
    def add_comment(self, comment):
        self.comments.append(comment)
    def remove_last_comment(self):
        temp = self.comments.pop()
        print("deleted comment", temp)



reel1=Instagram("dancing","dancing with friends", "bengaluru", "chandu")
reel1.disliked() 
reel1.liked() 
reel1.add_comment("good morning")
reel1.display_title()
reel1.display_creator()
reel1.display_location()
reel1.display_description()
reel1.display_likes()
reel1.display_comments()




reel2=Instagram("finance minister conference","finance minister conference with friends", "bengaluru", "chandu")
reel2.liked() 
reel2.liked() 
reel2.disliked() 
reel2.display_likes()
reel2.add_comment("good morning")
reel2.display_title()
reel2.display_creator()
reel2.display_location()
reel2.display_description()
reel2.display_likes()
reel2.display_comments()
