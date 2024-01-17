import crypt
salty = input("y/n?")
password = input(">>")
hashes = [["MD5", "$1$"], ["Blowfish", "$2a$"], ["eksblofish", "$2y$"],
          ["SHA-256", "$5$"], ["SHA-512", "$6$"]]
if salty == 'y':
    salt = input(">>")
    for i in range(0, len(hashes)):
        print(f'{hashes[i][0]}: {crypt.crypt(password, hashes[i][1] + salt)}')

else:
    for i in range(0, len(hashes)):
        print(f'{hashes[i][0]}: {crypt.crypt(password, hashes[i][1])}')
