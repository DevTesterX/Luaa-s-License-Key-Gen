import random

num_keys = 100 # How many keys do you want generated?

def main(self, count):
    seq = "ABCDFGHJIKLMNOPQRSTUVWXYZ1234567890"
    robloxID = "YourRobloxIDHere"
    command = "a!update" # You can change to a!update or a!redeem
    for i in range(count):
        key = ('-'.join(''.join(random.choice(seq) for _ in range(5)) for _ in range(4)))
        print(command, key, robloxID)
    print("\nGenerated {} serial keys!".format(count))
main(0, num_keys)
