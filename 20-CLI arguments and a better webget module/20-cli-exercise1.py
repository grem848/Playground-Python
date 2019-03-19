# Exercise 1 - 20-CLI arguments and a better webget module
# 1. Create a file with a `if __name__ == '__main__':` clause
# 2. Use the `argparse` library to create an `ArgumentParser`
# 3. Add the *positional* argument `URL` that gives you a string
# 4. Save that url into a string
import argparse


# bash commands: 
# python 20-cli-exercise1.py -h
# python 20-cli-exercise1.py https://dr.dk

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that downloads a URL and stores it locally')
    parser.add_argument('URL', help='an integer for the accumulator')
    parser.add_argument('-d', '--destination', default='default_file.exe', help='The name of the file to store the url in')
    args = parser.parse_args()

    print("URL: " + args.URL)
    print("Destination: " + args.destination)
    if args.destination == "default_file.exe":
        print("Saved to default file!")
    print("Nothing happened here since we just print :D")

