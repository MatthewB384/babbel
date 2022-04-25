# babbel
Inspired by https://libraryofbabel.info/, this aims to find the shortest 
possible string that contains every possible arrangement of characters of 
a given length and from a given character set

For example the string "aabacbbcca" contains every different 2 letter string
you could make from the letters a, b, & c.

For strings of length (len) and (num) different characters, the shortest string
you could possibly make that includes every possible string is num^len + len - 1
characters long. Such a string is called a minimum length string.

All minimum length strings are cyclic - the last (len-1) characters are the 
same as the first (len-1) characters. This means you could take any number of 
characters from the end of any minimum length string and move it to the start, 
and it would still be a valid minimum length string.

Let f(len, num) be the number of unique minimum length strings that contain
all possible substrings of length len using num different characters.

f(len, num) = num! ^ (num ^ (len - 1))
