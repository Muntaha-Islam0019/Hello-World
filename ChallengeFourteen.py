# Make a basic emote converter what converts some basic emotes like
# :) to 🙂.

emotes = {
    ":)": "🙂",
    ":(": "🙁",
    ":'(": "😥",
    ":3": "😅",
    ":p": "😛"
}

message = input("Enter with message: ")
message_Split = message.split(" ")

output_Message = ""

for word in message_Split:
    output_Message += (emotes.get(word, word + " ")) + " "

print(output_Message)
