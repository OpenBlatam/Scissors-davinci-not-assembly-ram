import pyperclip

# suppose we have a text that we want to "cut"
text = "This is a text to be cut"

# "cut" operation is basically copy + delete, so let's do the copy part first
pyperclip.copy(text)

# now you can paste it anywhere with pyperclip.paste(), once the data is copied it can be considered as "cut" from its original place
# to simulate deletion you can replace the original text with an empty string

text = ""
