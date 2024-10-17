# hey guys, so today we're going to do a madlibs project. In this project, we have a story where some words are given by the user.
# those words are in between <> and we need to collect them, ask to the user which word they want to use and then replace it. soo lets go

with open("story.txt", "r") as f:
    story = f.read()

print(story)