class Text(str):
    def duplicat(self):
        return self + self 

class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


# text = Text("Python")

# # print(dir(text))
# print(text.duplicat())
tract = TrackableList()
tract.append("1")