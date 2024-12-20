class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")
    def display_timeline(self):
        g=0
        print(self.username)
        for i in self.posts:
            g+=1
            print(g, end=' ')
            print(i)

def main():
    person=SocialMediaProfile('johndoe')
    SocialMediaProfile.add_post(person, 'Hello, world')
    SocialMediaProfile.add_post(person, 'Had a great time')
    SocialMediaProfile.add_post(person, 'what is up')
    SocialMediaProfile.display_timeline(person)

if __name__=='__main__':
    main()


