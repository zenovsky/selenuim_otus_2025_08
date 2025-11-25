from faker import Faker


class UserDataGenerator:
    def __init__(self, locale='en_US'):
        self.fake = Faker(locale)

    def generate_user_data(self):
        first_name = self.fake.first_name()
        last_name = self.fake.last_name()
        email = f"{first_name.lower()}.{last_name.lower()}{self.fake.random_int(min=100, max=999)}@fakemail.com"
        password = self.fake.password(length=10, special_chars=True, digits=True, upper_case=True)
        birthday = self.fake.date_of_birth(minimum_age=18, maximum_age=65).strftime('%m/%d/%Y')

        return {
            "firstname": first_name,
            "lastname": last_name,
            "email": email,
            "password": password,
            "birthday": birthday
        }

default_generator = UserDataGenerator()
