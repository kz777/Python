pyg = 'ay'
original = raw_input('Enter a word:')
word = original.lower()
first = word[0]
new_word = word + first + pyg
new_word = new_word[1:len(new_word)]

if len(original) > 0 and original.isalpha():
    print new_word
else:
    print 'empty'