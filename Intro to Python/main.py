'''
main.py
Intro to Python
Tuesday, 4 August, 2015
Alexander Rhett Crammer
Full Sail University

This was written for Python
version 3.4.3 which was
installed on my Mac at the
beginning of this course.
I don't know how to downgrade
but I've read that it's backwards
compatible with 2.7.
'''

# print("Hello, world!")

# Some properties
first_name = "Alexander"
middle_name = "Rhett"
last_name = "Crammer"

# Let's write those out
# print(first_name)

# response = input("What's your first name?\n") # raw_input() was renamed to input() in version 3.1 or so
# print("Hello, %s!" % response)

birth_year = 1995
current_year = 2015
year_difference = current_year - birth_year
# print("You should be around " + str(year_difference) + " years of age.")

budget = 500
store = "Tiffany's"
item = "Rose Gold Necklace"

if budget > 300:
	# print("Yes Gaga! You can go to %s to get that %s!" %(store, item.lower()))
	pass
elif budget > 5000:
	# print("It looks like you can afford to take a spree up 5th!")
	pass
else:
	# print("Keep saving. Rose gold doesn't mine, smelt, and market itself.")
	pass

# print("Hello.")

characters = ["Sailor Moon",
			"Tuxedo Mask",
			"Sailor Mercury",
			"Sailor Mars",
			"Sailor Jupiter",
			"Sailor Venus",
			"Sailor Chibi Moon",
			"Sailor Pluto",
			"Sailor Uranus",
			"Sailor Neptune"]
characters.append("Sailor Saturn")
# print(characters)
# print(characters[2])

movies = dict() # Instantiate an empty dictionary
movies = {
	"Star Wars":"Darth Vader",
	"Silence of the Lambs":"Hannibal Lecter"
}
# print(movies["Star Wars"])

i = 1
while i < 11:
	# print("Iteration #%s" % i)
	i += 1

for character in characters:
	# print(character)
	pass

for number in range(1, 11):
	# print("Iteration #%s" % number)
	pass

artists = ["Tori Kelly",
			"Brandi Carlile",
			"Marina and the Diamonds",
			"Lady Gaga",
			"Mariah Carey",
			"Mary J. Blige",
			"Jennifer Hudson"]
for artist in artists:
	# print(artist)
	pass

def findArea(height, width):
	return height * width

# print("The are of 20 and 40 is %s." % findArea(20, 40))

weight = 170
height = 64
message = '''
You're {height} high and {weight} heavy.
'''
message = message.format(**locals())
page_title = "Very Hacky HTML Page"
page_content = '''
<!DOCTYPE html>
	<head>
		<title>{page_title}</title>
	</head>
	<body>
		<p>{message}</p>
	</body>
</html>
'''
print(page_content.format(**locals()))
