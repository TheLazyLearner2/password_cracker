import hashlib 
from urllib.request import urlopen 

print(" ########## PASSWORD CRACKER ########## ")

class PasswordCracker:
    def __init__(self):
        self.password_list = []


    def get_password_list(self, url):
        try:
            read_password_list = urlopen(url).readlines()
            for i in range(len(read_password_list)):
                read_password_list[i] = read_password_list[i].decode().strip()
        except Exception as e:
            print("An error has occured, error:", e)
            exit()

        self.password_list = read_password_list
        return read_password_list


    def read_password_list(self, filename):
        random_password_list = []
        with open(filename, errors="ignore") as f:
            for line in f:
                random_password_list.append(line.strip())

        self.password_list = random_password_list
        return random_password_list


    def hash(self, password):
        result = hashlib.sha1(str(password).encode())
        return result.hexdigest()


    def bruteforce(self, password, password_list=[]):
        if not password_list: 
            password_list = self.password_list

        print(">>> Searching", len(password_list), "possible passwords ...")
        password_hash = self.hash(password)

        for pw in password_list:
            if self.hash(pw) == password_hash:
                print(">>> Password discovered:", pw)
                exit()
        else:
            print(">>> Password not found")


pwc = PasswordCracker()
pwc.get_password_list("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt")

your_password = "password123"
pwc.bruteforce(your_password)






