__author__ = 'nemzer'


import easygui as eg
import random
import math


def welcomeWindow(proteinsList, vegeList, carbsList, foodOptionsList, foodList):
    image = "resources/eatList.gif"
    choices = ["View List","What do I want to eat?", "What's in your fridge?"]
    reply = eg.buttonbox(image=image, choices=choices)
    respondToReply(reply, proteinsList, vegeList, carbsList, foodOptionsList, foodList)

def respondToReply(reply, proteinsList, vegeList, carbsList, foodOptionsList, foodList):
    if reply == "View List":
        # image = "has;kh;"
        msg = ""
        for item in foodList:
        	msg += item[0] + " wants to eat:" +"\n" + "	"
        	for i in range(1, len(item) - 1):
        		msg += item[i] + ", "
        	msg = msg[:-2]
        	msg += "        Score: " + item[len(item) - 1] + "\n"
        scores = []
        best = ""
        highest = 0
        for item in foodList:
        	if item[len(item) - 1] > highest:
        		highest = item[len(item) - 1]
        		best = item[0]
        msg += "\n\n TODAYS HEALTHIEST EATER IS:\n" + "		" + best
        choices = ["Back","Family is fed, delete list"]
        reply = eg.buttonbox(msg, choices=choices)
        if reply == "Back":
        	welcomeWindow(proteinsList, vegeList, carbsList, foodOptionsList, foodList)
        else:
        	foodList = ""
        	welcomeWindow(proteinsList, vegeList, carbsList, foodOptionsList, foodList)
    if reply == "What do I want to eat?":
        newItem = []
        nameReply = eg.enterbox(msg="My name is...")
        if nameReply:
        	newItem.append(nameReply)
        	chooseItems(foodOptionsList, newItem, carbsList, proteinsList, vegeList, foodList)
        else:
        	welcomeWindow(proteinsList, vegeList, carbsList, foodOptionsList, foodList)
    if reply == "What's in your fridge?":
        foodOptionsList = sorted(vegeList + proteinsList + carbsList)
        if foodOptionsList[0] == "":
        	foodOptionsList = foodOptionsList[1:]
        foodOptionsList = eg.multchoicebox(msg = "What's in your fridge?", title = "Choose Food", choices = foodOptionsList)
        welcomeWindow(proteinsList, vegeList, carbsList, foodOptionsList, foodList)


# function to read file and insert the items into a List
def readfile(file):
   f = open(file, 'r')
   myList = []
   for line in f:
        myList += line.rstrip().split(",")
   f.close()
   # print myList
   return myList

# function to search an element in a list

def search_element(lst, elem):
   flag = False
   if elem in lst:
       flag = True
   return flag

def chooseItems(foodOptionsList, newItem, carbsList, proteinsList, vegeList, foodList):
	if len(newItem) > 1:
		newItem = newItem[0:1]
	foodOptionsList = sorted(foodOptionsList)
	if foodOptionsList[0] == "":
        	foodOptionsList = foodOptionsList[1:]
	choices = eg.multchoicebox(msg = "What do you want to eat?", title = "Choose Food", choices = foodOptionsList)
	newItem += choices
	msg = "Are you sure you want:" + "\n"
	for i in range(1, len(newItem)):
		msg += "".join(newItem[i]) + ", "
	msg = msg[:-2]
	if eg.ccbox(msg):
		score = calculate_grade(choices, carbsList, proteinsList, vegeList)
		newItem.append(str(score))
		# print newItem
		if score == 1:
			image = "resources/1fullapple.gif"	
		elif score == 2:
			image = "resources/2fullapples.gif"
		elif score == 3:
			image = "resources/3fullapples.gif"
		elif score == 4:
			image = "resources/4fullapples.gif"
		else:
			image = "resources/5fullapples.gif"
		reply = eg.buttonbox(image=image, choices=["Oy Vey! I want to change that!", "Great! I'll stick with that!"])
		if reply == "Oy Vey! I want to change that!":
			chooseItems(foodOptionsList, newItem, carbsList, proteinsList, vegeList, foodList)
		else:
			foodList.append(newItem)
			welcomeWindow(proteinsList, vegeList, carbsList, foodOptionsList, foodList)
	else:
	    chooseItems(foodOptionsList, newItem, carbsList, proteinsList, vegeList, foodList)

# Calculate the user score - recives lst of items choosen by the user.
def calculate_grade(lst, carbsList, proteinsList, vegeList):
	NumCarbs = 0
	NumProtain = 0
	NumVeges = 0
	for elem in lst:
		if (search_element(carbsList,elem)):
			NumCarbs += 1
		elif (search_element(proteinsList,elem)):
			NumProtain += 1
		elif (search_element(vegeList,elem)):
			NumVeges += 1
	# print str(NumVeges) + " " + str(NumProtain) + " " + str(NumCarbs)
	Num_of_items = len(lst)
	# score = (abs(1-0.5*NumCarbs/Num_of_items) + abs(1-0.33333*NumProtain/Num_of_items) + abs(1-0.166666*NumVeges/Num_of_items))/3
	# score = (abs(1 - (NumCarbs/(2*Num_of_items) + NumProtain/(3*Num_of_items) + NumVeges/(6*Num_of_items))))/3
	# score = (abs(NumCarbs/(2*Num_of_items) + NumProtain/(3*Num_of_items) + NumVeges/(6*Num_of_items)))/3
	# score = (abs(2*NumCarbs/Num_of_items + 3*NumProtain/Num_of_items + 6*NumVeges/Num_of_items))/3
	score = 2*(NumCarbs/float(3) + NumProtain/float(2) + NumVeges/float(1))/float(Num_of_items)
	print score
	final_score = math.ceil(score*5)
	if final_score == 0:
		final_score = 1
	# print final_score
	# return random.randint(1, 5);
	return final_score


carbsList = readfile('resources/carbs.txt')
vegeList = readfile("resources/vegetables.txt")
proteinsList = readfile("resources/proteins.txt")
foodOptionsList = proteinsList + vegeList + carbsList
foodList = []


welcomeWindow(proteinsList, vegeList, carbsList, foodOptionsList, foodList)

