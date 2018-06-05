import argparse


def set_args():
    """
    Establish the command line parameters that will be supported when executing this utility.
    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", help='Example help', action="store_true")
    parser.add_argument("-c", "--set-capacity-config-file",
                        help='Manually define a capacity config file.',
                        action="store")
    return parser


def main():
    parser = set_args()
    args = parser.parse_args()

    if args.test:
        # Establishing that this works on a basic level.  This will eventually become useful.
        print('test selected')


if __name__ == '__main__':
    main()
