from src.query_service import Users
import argparse

parser = argparse.ArgumentParser(description='User query engine')

parser.add_argument('--query', '-q',
                    help='--query birthdays \n# number of birthdays today.\n'
                    '--query uuid \n# list of uuid\'s of user\'s birthdays\n')

parser.add_argument('--age_over_n', '-a', metavar='N', type=float,
                    help='--age_over_n <query age>  \n# query ages over n\n')

parser.add_argument('--delete', '-d',
                    help='--delete <uuid> \n# Deletes user based on UUID.',
                    type=str)

args, leftovers = parser.parse_known_args()

users = Users('Data/users.csv')

if args.query == 'birthdays':
    print("Number of birthdays today.")
    print(users.number_of_birthdays)

if args.query == 'uuid':
    print("UUID's with birthdays.")
    for uuid in users.birthday_users.keys():
        print(uuid)

if args.age_over_n is not None:
    print("How many users aged over N.")
    print(users.query_age_gt_n(args.age_over_n))

if args.delete is not None:
    print("Delete user id: " + args.delete)
    users.delete_user(args.delete)
