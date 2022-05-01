"""Creating a dictionary"""
class TagCloud:
    def __init__(self):
        self.__tags = {
            "Name": "Kojibello",
            'Build_Name': "Python"
        }

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1   

    """get item magic method"""
    def __getitem__(self, tag):
        return self.tag.get(tag.lower(), 0)

    """set item magic method"""
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count 

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)   


cloud = TagCloud()

# print(cloud.__dict__)
print(cloud._TagCloud__tags)
"""what to read a tag like cloud[""]"""
#print(cloud.__tags["Python"])