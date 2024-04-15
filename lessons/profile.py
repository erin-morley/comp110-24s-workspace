"""Practice writing a twitter profile class."""
# definition
class Profile:

    username: str
    private: bool

    def __init__(self, username_input: str):
        """Create new profile."""
        self.username = username_input
        self.private = True
        # return self
    
    def tweet(self, msg: str) -> None:
        """If profile is not private, print msg."""
        if self.private is False:
            print(f"{self.username}: {msg}")

user1: Profile = Profile("110_rulez") #__init__
user1.private = False
user1.tweet("OOP is cool!")=-