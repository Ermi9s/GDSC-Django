print("Enter a word:", end=" ")
word = input()
left = 0
right = len(word)-1

while left < right:
    if word[left] != word[right]:
        print("The word is not palindrome")
        break
    left += 1
    right -= 1
else:
    print("The word is palindrome")