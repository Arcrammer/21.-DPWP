'''
Mad Lib
Tuesday, 4 August, 2015
Alexander Rhett Crammer
Full Sail University
'''

place = input("What's your favourite place to walk through?\n~> ")
things = input("What do you carry when you walk?\n~> ").lower()
giant_object = input("Largest object you can think of that stands:\n~> ").lower()
action = input("What does that object do?\n~> ").lower()
amount_of_times = int(input("Favourite number:\n~> "))
time_of_day = input("Favourite time of day:\n~> ").lower()
calling_code = int(input("What's your area code?\n~> "))
grocery_item = input("Favourite foodstuff:\n~> ").lower()
person = input("First name of your favourite person:\n~> ").lower()
street_name = input("Favourite street name:\n~> ").lower()
second_action = input("Something bad that you shouldn't do:\n~> ").lower()
age = int(input("Age:\n~> "))
os = input("'Windows', 'OS X', or 'Ubuntu'?\n~> ")

if age > 20:
	old_or_young = "old"
else:
	old_or_young = "young"

operating_systems = {
	"Windows": {
		"Creator":"Microsoft",
		"Latest Release":"Windows 10"
	},
	"Ubuntu": {
		"Creator":"Cononical",
		"Latest Release":"15.04 Vivid Vervet"
	},
	"OS X": {
		"Creator":"Apple",
		"Latest Release":"10.10 Yosemite"
	}
}

# Make the input for 'os' case insensitive
if os.lower() == "windows":
	os_creator = operating_systems["Windows"]["Creator"]
	os_version = operating_systems["Windows"]["Latest Release"]
elif os.lower() == "os x":
	os_creator = operating_systems["OS X"]["Creator"]
	os_version = operating_systems["OS X"]["Latest Release"]
else:
	os_creator = operating_systems["Ubuntu"]["Creator"]
	os_creator = operating_systems["Ubuntu"]["Latest Release"]

story = '''
I was walking through {place} with my {things} when I had suddenly noticed a giant {giant_object} directly in my path. It was seemingly inanimate and unaware of my presence so it continued to {action} without a thought. This particular {giant_object} appeared to be {old_or_young}. It was the most giant {giant_object} within the {calling_code} area code. Why would such a significant and majestic {giant_object} choose to {action} ever-so blissfully unaware of the world around itself? Later that same {time_of_day} I had decided to visit the grocery store because I had completely run out of {grocery_item} the day before -- {person} knows I can't go without my precious {grocery_item}s. However... What I had anticipated to be a lovely shop for {grocery_item}s had turned out to be a nightmare on {street_name} street. Ah! You gave me a fright, sir {person}. My life was forever changed on that day. I decide to {second_action}. I've been told {amount_of_times} times not to do that or I would be arrested. I don't see why it's illegal, but I was still forewarned not to do it again. Never again shall I {second_action}! I must now update my {os_creator} computer. It's still running OS version {os_version}!
'''
print(story.format(**locals()))
colours = ["Red","Orange","Yellow","Green","Teal","Blue","Purple","Magenta"]
print("Which colours are to be found in a rainbow? These:")
for colour in colours:
	print(colour)
