SECRET: int = 2

if SECRET == 10:
    print("Correct!")
else:
    if SECRET < 10:
        print("Your guess was too low.")
    else:
        print("You guess was too high.")

# combine else and if
if SECRET == 10:
    print("Correct!")
elif SECRET < 10:
    print("Your guess was too low.")
else:
    print("Your guess was too high.")