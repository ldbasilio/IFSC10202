# If you pass an empty sequence to range(), like range(-5) or 
# range(7, 3), the for-block won't be executed.
# Generally, you're not interested in creating empty ranges.

for i in range(-5):
    print("This won't be printed")
for k in range(8, 6):
    print('Nothing will be printed')
print("End of Loop")
