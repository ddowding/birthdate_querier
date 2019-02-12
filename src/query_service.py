import csv
from datetime import datetime
from timeit import default_timer as timer


class Users:
    def __init__(self, file_name):
        self.file_name = file_name
        self.user_dict, self.birthday_users = self.generate_user_list()
        self.number_of_birthdays = len(self.birthday_users)

    def generate_user_list(self):
        start = timer()
        user_dict = {}
        birthday_users = {}
        counter = 0

        with open(self.file_name) as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    user = User(row[0], row[1])
                    user_dict[row[0]] = user
                    if user.valid_row:
                        if user.birthday:
                            birthday_users[row[0]] = user
                    counter += 1
                except Exception as ex:
                    print(ex)
        end = timer()

        print("Time taken to read in user list: " +
              str(end - start) + " seconds for "
              + str(counter) + " rows.")

        return user_dict, birthday_users

    def query_age_gt_n(self, query_age):
        start = timer()
        number_gt_n = 0
        loop_counter = 0
        for user_id in self.user_dict:
            user = self.user_dict[user_id]
            if user.valid_row:
                if user.age > query_age:
                    number_gt_n += 1
            loop_counter += 1
        end = timer()

        print("Time taken to query age over n: " +
              str(end - start) +
              " seconds." +
              " for " + str(loop_counter) + " rows.")

        return number_gt_n

    def delete_user(self, uuid):
        # Delete from user and birthday dicts
        start = timer()
        if str(uuid) in self.user_dict:
            self.user_dict.pop(str(uuid))
            self.save_csv()
        if uuid in self.birthday_users:
            self.birthday_users.pop(str(uuid))
        end = timer()
        print("Time taken to delete user: " + str(end - start) + " seconds.")

    def save_csv(self):
        with open(self.file_name, 'w') as file:
            print("Writing to file: " + str(self.file_name))
            for user_id in sorted(self.user_dict):
                user = self.user_dict[user_id]
                string_to_write = str(user.uuid) + ', ' + str(user.dob_raw) + '\n'
                file.write(string_to_write)
            print("Done writing")


class User:
    def __init__(self, uuid, dob_raw):
        self.uuid = uuid
        self.dob_raw = dob_raw
        try:
            self.dob = datetime.strptime(str(dob_raw).replace(" ", ""), '%Y-%m-%d')
            self.birthday = self.calculate_birthday_today()
            self.age = self.calculate_age()
            self.valid_row = True
        except ValueError:
            self.valid_row = False

    def calculate_birthday_today(self):
        now = datetime.now()
        if self.dob.month == now.month and self.dob.day == now.day:
            return True

    def calculate_age(self):
        now = datetime.now()
        return now.year - self.dob.year - ((now.month, now.day) < (now.month, now.day))
