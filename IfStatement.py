# ----- If statement -----

hasMoney = False
isSmoker = False
hasGirlfriend = False

print("\nReply with Y or N.\n")
if input("Do you have much money? ") == "Y":
    hasMoney = True
if input("Do you drink/smoke? ") == "Y":
    isSmoker = True
if input("Do you have a girlfriend? ") == "Y":
    hasGirlfriend = True

if (isSmoker or hasGirlfriend) and not hasMoney:
    print("\nProblems will be generating eventually.")
else:
    print("\nNo problems!")
