# Write a function called "show_excitement" where the string
# "I am super excited for this course!" is returned exactly
# 5 times, where each sentence is separated by a single space.
# Return the string with "return".
# You can only have the string once in your code.
# Don't just copy/paste it 5 times into a single variable!


def show_excitement():
    phrase = "I am super excited for this course!"
    newPhrase = ""
    for time in range(0,5):
        newPhrase += phrase
        if(time != 4):
            newPhrase += " "
    return newPhrase

print show_excitement()