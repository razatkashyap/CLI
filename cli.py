import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type = int, default = 1, help = "Enter your fing age ? ")
    parser.add_argument("y", type = str, default = "", help = "Enter your name ?")
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

def calc(args):
    if args.x >= 18 :
        if args.y != None:
            return "You can enter %s " % args.y
        else:
            return "Please specify your name"
    elif args.x < 18 :
        if args.y != None:
            return "You can not enter %s " % args.y
        else:
            return "Please specify your name"
    else:
        return "Please enter something a number"

if __name__ == '__main__':
    main()
