 # Ask the user to list a starting number, ending number, and increment to use. Display an answer based on the users' answers (use the input command.)

# starting number
start=int(input("Start at: "))

# ending number
end=int(input("End before: "))

# increment
inc=int(input("Increment between values: "))

for i in range(start, end, inc):
  print(i)