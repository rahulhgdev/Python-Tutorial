def calculate_volume(radius):
    print("__name__:",__name__)
    return 1.33*3.14*radius*radius*radius

if __name__ == "__main__":
    print("I'm in main.py")
    v = calculate_volume(10)
    print("Volume:",v)
