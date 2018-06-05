import argparse


def set_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", help='Example help', action="store_true")
    return parser


def main():
    parser = set_args()
    args = parser.parse_args()

    if args.test:
        print('test selected')


if __name__ == '__main__':
    main()
