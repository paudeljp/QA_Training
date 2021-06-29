# def assert_function(x,y):
#     assert x == y
#
# if __name__ == "__main__":
#     x = "Jeevan"
#     y = "Jeevan"
#     assert_function(x,y)

# def assert_function(x,y):
#     assert x in y
#
# if __name__ == "__main__":
#     x = "Jeevan"
#     y = "Jeevans"
#     assert_function(x,y)


# def assert_function(x,y):
#     assert x not in y
#
# if __name__ == "__main__":
#     x = "Jeevan"
#     y = "Jeevans"
#     assert_function(x,y)


# def try_catch():
#     Y = "Hi"
#     try:
#         print(Y)
#     except:
#         print("Y is not defined")
#
# if __name__ == "__main__":
#     try_catch()


def try_catch():
    try:
        assert Y == Y
    except AssertionError:
        print("Unmatched")
    except:
        print("Other Exception has occured")
    else:
        print("Matched")

if __name__ == "__main__":
    try_catch()




