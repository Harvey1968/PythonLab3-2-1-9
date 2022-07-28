# 3.2.1.9 LAB: The break statement - Stuck in a loop

while True:
    print('"Oops looks like you\'re trapped in my never ending loop!"') 
    secret = input("Enter the secret word to escape the loop: ")
    print()
    # A 'string' is used as a conditional statement.
    if secret == "chupacabra":
        # If the secret word is entered then exit the loop.
        break
# Final print statement.
print('"Damn it you\'ve escaped my loop!"\n')


