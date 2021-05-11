# def cache1d(func):
#     def inner(*args, **kwargs):
#         with open("last.json", r) as file:
#             last = json.load(file)
#         if last["name"]["date"] == date.today():
#             return last["name"]["answer"]
#         else:
#             function

def test():
    def inner(func):
        print("ENTER inner")
        func()
        print("EXIT inner")
    return inner
