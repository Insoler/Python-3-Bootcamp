def func():
    print("Hello, this is the function in one.py")

print("Top level in one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("One.py has been imported")