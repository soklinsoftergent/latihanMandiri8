import re
import random
import string

def randomPasswd(seed: str, characters_number: int): 
	s1 = list(string.ascii_lowercase)
	s2 = list(string.ascii_uppercase)
	s3 = list(string.digits)
	s4 = list(string.punctuation)

	random.seed(seed, 10)
	random.shuffle(s1)
	random.shuffle(s2)
	random.shuffle(s3)
	random.shuffle(s4)


	part1 = round(characters_number * (30/100))
	part2 = round(characters_number * (20/100))


	result = []

	for x in range(part1):

		result.append(s1[x])
		result.append(s2[x])

	for x in range(part2):

		result.append(s3[x])
		result.append(s4[x])


	random.shuffle(result)


	password = "".join(result)
	return password


def gen_username_passwd(teks: str):
	full_emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", teks)
	usernames = []
	passwords = []
	for email in full_emails:
		email_short = re.findall(r"\w+@", email)
		username = email_short[0][:-1]
		usernames.append(username)
		password = randomPasswd(username, 8)
		passwords.append(password)
		print(email, "username:", username, "password:", password)


teks = """Berikut adalah daftar email dan nama pengguna dari mailing list:
anton@mail.com dimiliki oleh antonius
budi@gmail.co.id dimiliki oleh budi anwari
slamet@getnada.com dimiliki oleh slamet slumut
matahari@tokopedia.com dimiliki oleh toko matahari"""

gen_username_passwd(teks)