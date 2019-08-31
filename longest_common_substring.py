
def longestCommSubStr(str1, str2):
    # Create the string we want to return.
    final_lcs = ''

    # Length of the first string.
    len1 = len(str1)

    # Length of the second string.
    len2 = len(str2)

    # Iterate through the positions of each character in the columns (first string characters) from left to right
    for i in range(len1):

        # We compare that position's character with each row position's character (second string characters)
        for j in range(len2):
            # Create a variable to mark the positions of each character across the first string columns and down the second string rows.
            pos = 0

            # Create a variable as a temporary longest common substring that we can add characters to if conditions are met. 
            temp_lcs = ''

            # While the first string position is less than the first string length
            # and the second string position is less than the second string length
            # and the letter at the first string position is equal to character at the second string position,
            # this means the characters match and we need to add that character to our string we want returned.
            while ((i + pos < len1) and (j + pos < len2) and str1[i + pos] == str2[j + pos]):

                # Our temporary longest common substring is equal to its current value plus the matched letter.
                temp_lcs += str2[j + pos]

                # 
                if str1[i + pos] == str2[j + pos]:
                    exit

                # We set the position to the next position 
                pos += 1
                
            # If the length of our temporary string is greater the length of the final string we want returned...
            if (len(temp_lcs) > len(final_lcs)):

                #...we set our final string equal to the temorary one.  
                # Keep in mind, we declared our final_lcs outside the loop, so only the 
                # resetting the temp_lcs for ever letter of the first string 
                # is not resetting the final_lcs to an empty string.
                final_lcs = temp_lcs
                
    return final_lcs

lcs = longestCommSubStr("nailed it", "snailed it")
print lcs
print len(lcs)