# hey guys, so today we're going to do a madlibs project. In this project, we have a story where some words are given by the user.
# those words are in between <> and we need to collect them, ask to the user which word they want to use and then replace it. soo lets go

# function to open the text file
with open("projects/madlibs/story.txt", "r") as f:
    story = f.read()

words = set() # basically create an array of unique elements

flag = -1
start_target = "<"
end_target = ">"

for i, char in enumerate(story):  # this runs through the story getting the index (i) and char in which position
    if char == start_target:
        flag = i

    if char == end_target and flag != -1:
        word = story[flag : i + 1] # this goes from flag (<) up to end_target (>) and gets everything that's inside. 
        words.add(word)
        flag = -1

# asking the replacement words for the user

answers = {} # creates an dictionary

for word in words:
    answer = input(f"Type an word for {word}: ")
    answers[word] = answer

# replacing the words in the story

for word in words:
    story = story.replace(word, answers[word])

print(story)