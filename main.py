import random
from datetime import datetime, timedelta

SIGNUP_LINKS = {
    "Gmail": "https://accounts.google.com/signup",
    "Instagram": "https://www.instagram.com/accounts/emailsignup/",
    "Facebook": "https://www.facebook.com/r.php",
    "X": "https://x.com/i/flow/signup",
    "TikTok": "https://www.tiktok.com/signup/phone-or-email/email"
}


def pick_random(file_path):
    """Help to open files"""
    try:
        with open(file_path, encoding='utf-8') as file:
            lines = file.readlines()
            random_line = random.choice(lines)
            return random_line.strip()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def generate_random_birthday():
    """Generate a random birthday in the format of DD-MM-YYYY"""
    start_date = datetime(1900, 1, 1)  # Earliest possible birthday
    end_date = datetime.today()  # Today's date
    # Generate a random date between start_date and end_date
    random_days = random.randint(0, (end_date - start_date).days)
    random_birthday = start_date + timedelta(days=random_days)
    return random_birthday.strftime('%d-%m-%Y')


def generate_pii():
    """Returns generated user information"""
    first_name = pick_random('first_names.txt')
    last_name = pick_random('last_names.txt')
    birthday = generate_random_birthday()
    username = last_name[0].lower() + first_name.lower() + birthday[-4:]
    password = last_name[0] + "." + first_name[0].lower() + "_" + str(random.randint(100000, 999999))
    email = username + "@gmail.com"
    return [first_name, last_name, birthday, username, password, email]


def print_credentials(credentials):
    """Prints generated user information"""
    keys = ["First Name", "Last Name", "Birthday", "Username", "Password", "Email"]
    user_info = dict(zip(keys, credentials))
    # Print out the values
    print("---User Information---")
    for info in user_info:
        print(f'{info}: {user_info[info]}')
    print("---User Information---")


def print_signup():
    """Prints out signup links for various social media sites"""
    print("\n---Links---")
    for platform, link in SIGNUP_LINKS.items():
        input(f'{platform}: {link}')


def main():
    """Main function"""
    credentials = generate_pii()
    print_credentials(credentials)
    print_signup()
    print("---Goodbye---")


if __name__ == "__main__":
    main()
