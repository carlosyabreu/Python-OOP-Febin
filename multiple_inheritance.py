
class OperatingSystem:
    multitasking = True
    name = "Mac OS"
class Apple:
    website = "www.apple.com"
    name = "Apple"
class MacBook(OperatingSystem, Apple):
    def __init__(self):
        if self.multitasking is True:
            print(f"This is a multi tasking system. Visit {self.website} for more details")
            print("This is a second multi tasking system. Visit {} for more details".format(self.website))
            print("Name: ", self.name)

macBook = MacBook()
