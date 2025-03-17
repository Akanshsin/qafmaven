# Define the string to check
import sys

if len(sys.argv) > 2 and sys.argv[1] == sys.argv[2]:
    print("Both the keys are same ", sys.argv[2])
else:
    print("Both the keys are different")
