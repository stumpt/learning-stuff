import interpolate as int

def run_tests():

    int.load("../data/textbook_values.csv")
    print(int.interpolate(568.2))

def main():
    run_tests()

if __name__ == "__main__":
    main()

