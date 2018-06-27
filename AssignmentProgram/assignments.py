import argparse
import os
import toml
from AssignmentProgram.AssignmentProcessing import generate_zipcodes_manager, generate_capacities_manager, \
    generate_members, process_rules, generate_stats, update_masshealth_assignments


def set_args():
    """
    Establish the command line parameters that will be supported when executing this utility.
    :return: None
    """
    description = 'Assignment Program utility used to apply rules to the MassHeath Spreadsheet.'
    parser = argparse.ArgumentParser(description,
                                     epilog='--config-file is mutually exclusive from specifying each file.')
    parser.add_argument("-t", "--test", help='Example help', action="store_true")
    maingroup = parser.add_argument_group(title='required')
    maingroup.add_argument("-m", "--masshealth-file",
                           help='Manually define location to MassHealth Excel workbook.',
                           action="store",
                           dest='masshealthfile',
                           metavar="masshealth.xlsx",
                           nargs=1)
    maingroup.add_argument("-z", "--zipcode-file",
                           help='Manually define location to Zipcode Excel workbook.',
                           action="store",
                           dest='zipcodefile',
                           metavar="zipcode.xlsx",
                           nargs=1)
    maingroup.add_argument("-c", "--capacity-file",
                           help='Manually define location to Capacity Excel workbook.',
                           action="store",
                           dest='capacityfile',
                           metavar="zipcode.xlsx",
                           nargs=1)
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("-C", "--config-file",
                       help='Path to the configuration file used to define the source files.',
                       action="store",
                       dest='configfile',
                       metavar="config.toml",
                       nargs=1)
    group.add_argument("-N", "--no-capacity",
                       help='Disable the use of capacity when making assignments.',
                       action="store_true",
                       dest='nocapacity')
    group.add_argument("-D", "--mark-duplicate-members",
                       help='Add a text indicator in the Excel workbook rows for duplicate members.',
                       action="store_true",
                       dest='markduplicates')
    return parser


def load_toml(toml_file_location):
    return toml.load(toml_file_location)


def main():
    parser = set_args()
    args = parser.parse_args()
    masshealth_file_location = None
    capacity_file_location = None
    zipcode_file_location = None
    apply_capacities = True
    mark_member_duplicates = False

    if args.test:
        # Establishing that this works on a basic level.  This will eventually become useful.
        print('test selected')

    if args.masshealthfile:
        print("MassHealth File: {}".format(args.masshealthfile))

    if args.masshealthfile:
        print("Zipcode File: {}".format(args.zipcodefile))

    if args.capacityfile:
        print("Capacity File: {}".format(args.capacityfile))

    if args.configfile:
        print("Config File: {}".format(args.configfile))
        file_path = str(args.configfile[0])
        full_path = '{0}\{1}'.format(os.path.dirname(os.path.realpath(__file__)), file_path)
        if os.path.exists(full_path):
            config = load_toml(full_path)
            print(config)
            if config:
                masshealth_file_location = config['files_config']['masshealth_location']
                capacity_file_location = config['files_config']['capacity_location']
                zipcode_file_location = config['files_config']['zipcode_location']
                apply_capacities = config['assignment_options']['apply_capacities']
                mark_member_duplicates = config['assignment_options']['mark_member_duplicates']

                print("found these: "
                      "\nMassHealth: {0}\n"
                      "Capacity: {1}\n"
                      "Zipcode: {2}\n"
                      "Apply capacities: {3}".format(masshealth_file_location, capacity_file_location,
                                                     zipcode_file_location, apply_capacities))
        else:
            print('Error: File {0} not found!'.format(full_path))
            exit(1)

    if args.markduplicates:
        print("Marking up duplicate member rows with the text string DUPLICATE")

    # TODO - check if all config parsing is good, run the program...
    process_all(zipcode_file_location, capacity_file_location,
                masshealth_file_location, apply_capacities, mark_member_duplicates)


def process_all(zipcode_excel_location, capacity_excel_location, masshealth_excel_location,
                apply_capacities=True, mark_duplicates=False):
    # TODO - add in code to control capacity management flag: apply_capacities
    zipcode_manager = generate_zipcodes_manager(zipcode_excel_location)
    capacities_manager = generate_capacities_manager(capacity_excel_location)
    all_members = generate_members(masshealth_excel_location)

    process_rules(all_members, capacities_manager, zipcode_manager)
    generate_stats(all_members)
    update_masshealth_assignments(all_members, masshealth_excel_location, mark_duplicates)


if __name__ == '__main__':
    main()
