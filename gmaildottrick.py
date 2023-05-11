import itertools

def period_combinations(email):
    username, domain = email.split('@')
    combinations = []

    for i in range(len(username)):
        for combo in itertools.combinations(range(1, len(username)), i):
            new_username = list(username)
            for offset, index in enumerate(combo):
                new_username.insert(index + offset, '.')
            combinations.append(''.join(new_username) + '@' + domain)

    return combinations

def save_to_file(emails, filename):
    with open(filename, 'w') as file:
        for email in emails:
            file.write(email + '\n')

if __name__ == '__main__':
    email = input('Enter the email: ')
    emails = period_combinations(email)
    save_to_file(emails, 'output.txt')
