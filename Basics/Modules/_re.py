import re 
# re module

str = "Python course : Your Python pathway | 40 Hours(saat)"

# re.findall()
# Finds all the patterns of 1st parameter in the 2nd paramater 
# result = re.findall("Python",str)
# result = len(result)
#---------------------------------------------------------------------------------------------------------------------
# re.split()
# splits the string from the character in 1st parameter 
# result = re.split(" ",str)
# result = re.split("w",str)
#----------------------------------------------------------------------------------------------------------------------
# re.sub()
# replaces the first parameter with the second parameter in the str (which is parameter 3)
# result = re.sub(" ","-",str)
#-----------------------------------------------------------------------------------------------------------------------
# re.search()
# searchs where the first paramater (or element) on the string 
result = re.search("Python",str)
# now result is the match object (which is Python)
# result = result.span()
# result = result.start()
# result = result.end()
# result = result.group()
result = result.string
#-----------------------------------------------------------------------------------------------------------------------
# Regular Expression 

"""
[] All expressions written in square brackets will be searched
   [abc] => a = 1 Match
            ac = 2 Match
            Python = No Matches 
    [a-e] => [abcde]
    [1-5] => [12345]
    [0-39] => [1239]  ( 0 1 2 3 9 only these numbers )

    [^abc] => character other than abc
    [^0-9] => characters other than numbers 



"""
result = re.findall("[abc]",str)
result = re.findall("[hour]",str)
result = re.findall("[a-e]",str)  #returns a b c d e 
result = re.findall("[0-9]",str) #returns numbers
result = re.findall("[^abc]",str) #returns non abc characters
result = re.findall("...",str)  #returns every 3 characters
result = re.findall("Py..on",str)
#------------------------------------------------------------------------------------------------------------------------
"""
  ^ - Does the pattern (string) start with the specified character?
  ^a  = > 0 Mathces
  ^P = > 2 Matches
"""

result = re.findall("[^a]",str)
result = re.findall("[^P]",str)
#------------------------------------------------------------------------------------------------------------------------
"""
  a$ - Does the pattern (string) ens with the specified character ? 

"""

result = re.findall("s$",str)
result = re.findall("Hours$",str)
#------------------------------------------------------------------------------------------------------------------------
"""
  * - checks whether the string contins specified parameter more than once  
   ma*n => mn = 1 Match 
           man = 1 Match
           maaaan = 1 Match 
           main = No Match (n doesn't come after a that'S why there is no match)
"""
result = re.findall("sa*t",str)
#------------------------------------------------------------------------------------------------------------------------
"""
   + - checks whether the string contains specified parameter for once or more 
"""
result = re.findall("sa+t",str)
#------------------------------------------------------------------------------------------------------------------------
"""
  ? - checks whether the string contains the specified parameter just for once or doesn't contain
"""
result = re.findall("sa?t",str)
#------------------------------------------------------------------------------------------------------------------------
"""
  {} -Checks the character number
     al{2} -- l character comes after the a for 2 times
     al{2,3} -- l comes after a at least for 2 times , at most 3 times  
     [0-9]{2,4} -- Numbers with at least 2 and at most 4 digits
"""
result = re.findall("a{2}",str)
result = re.findall("[0-9]{2}",str)
#---------------------------------------------------------------------------------------------------------------------------
"""
   | - One of the alternative options must be realized
      a|b = a or b

      cde = > no match
      ade = > 1 Match 
      acdbea = > 3 Match 
#---------------------------------------------------------------------------------------------------------------------------
"""
   

"""
   ()  - uses for grouping 
   (a|b|c)xz => x and z must be placed between the abc characters
"""
# What we have covered so far has been about alphanumeric characters, now we will look at special characters.

#--------------------------------------------------------------------------------------------------------------------
"""
  \  - > uses for searching special characters 
     \$a => search for a after $ . Means that $ doesn't comment by regular expression engine 

     
   \A -> Is the specified character placed at the beginning of the string ? 
     \Athe -> is 'the' at the beginning of the string ? 

    
    \Z -> Is the specified character placed at the end of the string ? 
      the\Z -> is 'the' at the end of the string ?  

    \b -> checks whether the specified character placed at the beginning of the sentence or at the end of the sentence 
       \bthe => is 'the' placed at the beginning of the sentence ?
       the\b => is 'the' placed at the end of the sentence ?

    \d -> same as [0-9] , searchs for numbers
      \d => 12abc34

    \D same as [^0-9] , searchs for non-numbers
      \D => 1ab44_50

    \s -> serachs for whitespaces 
    \S -> inverse of \s , search for non-whitespace
    \w -> alphabetical characters , numbers , underscore characters 
    \W -> inverse of \w  
"""


print(result)