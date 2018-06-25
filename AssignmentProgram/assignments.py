import argparse


def set_args():
    """
    Establish the command line parameters that will be supported when executing this utility.
    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", help='Example help', action="store_true")
    parser.add_argument("-m", "--masshealth-file",
                        help='Manually define location to MassHealth Excel workbook.',
                        action="store",
                        dest='masshealthfile')
    parser.add_argument("-z", "--zipcode-file",
                        help='Manually define location to Zipcode Excel workbook.',
                        action="store",
                        dest='zipcodefile')
    parser.add_argument("-c", "--capacity-file",
                        help='Manually define location to Capacity Excel workbook.',
                        action="store",
                        dest='capacityfile')
    return parser


def main():
    parser = set_args()
    args = parser.parse_args()

    if args.test:
        # Establishing that this works on a basic level.  This will eventually become useful.
        print('test selected')

    if args.masshealthfile:
        print("MassHealth File: {}".format(args.masshealthfile))

    if args.masshealthfile:
        print("Zipcode File: {}".format(args.zipcodefile))

    if args.capacityfile:
        print("Capacity File: {}".format(args.capacityfile))


if __name__ == '__main__':
    main()
