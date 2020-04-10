phrase = input("Enter a word or phrase (without spaces or punctuation): ")

done = True
palindrome = True
start = 0

end = len(phrase)-1
while start < len(phrase):

    
    if phrase[start] != phrase[end]:
        palindrome = False

    start += 1
    end -= 1

if palindrome:
    print("That is a palindrome!")
else:
    print("That is not a palindrome.")
