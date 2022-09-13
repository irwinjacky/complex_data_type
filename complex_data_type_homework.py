# %%
"""BMI 6018 Fall 2022 

Instructions: For this assignment, please return all answers as variables in your
.py file. You will quickly note that you will need to find answers outside the
class lectures. This is not an accident! You will need to become professionally
comfortable with looking things up via the python docs and google. 

Ensure that all variables are labelled according to the example. IE the answer
to problem 1 part c should be labelled one_c. While all questions are answerable
with a single line of code, you are free to use helper variables so long as they
are helpfully/informatively named. 

I should be able to open your .py file and run it without errors. I will **not** be 
debugging your code for you. If your file does not run, it will **not** be graded. 
If you are unsure if your file will run, open up a chpc terminal and test it there.

For this assignment, please only use base python files types. That is: there 
should be no import calls in your file save my use of sys at the end.

Example Problem

0.a Create a list of strings
0.b Using a str method, capitalize one of the elements in the list using a slice
0.c Coerce one character of the list to display as a hex

zero_a = ['first','second','third','fourth','fifth']
zero_b = zero_a[1].upper()
zero_c = hex(ord(zero_a[1][1]))

#Problem 1: Lists, Sets and Coersion

1.a Create a list of integers no fewer than 10 items from 0 to 9.
 .b Add 3 to the 5th indexed element
 .c Coerce all elements in the list to floats using list comprehension
 .d Coerce the list to a set
 .e Using a method, append int 10 to the set
 .f Using a method, pop an item from the set
 .g Using a length counting function, count the number of items in the set
 .h Check if the number of items in the set is the same as the 
    number of items in the list
 .i Coerce the set to a list and use the "+" operator combine the list to the list from 1.a
 .j Coerce 1.i to a set
 .k Count the number of elements in the 1.j



Problem 2: Dictionary woes

2.a Combine the three sample dictionaries (given below) into a nested dictionary (nested in programming means joined), named 
    two_a, ensure the key names are the same as the dictionary names.
 .b Using keys, retrieve the Dango's name from 2.a
 .c Using keys, update the value of Mochi's year to 2018. This should not be a variable
    and should simply update 2.a.
 .d Manually create a dictionary that has a single level and contains each patient
    as the key and the year as the value. Set Mochi's year to 2019.'
 .e Coerce the keys of 2.d into a list
 .f Coerce the values of 2.d into a list
 .g Use the zip function to combine 2.e and 2.f into a dictionary again


two_patient_dictionary_kinoko = {
  "name" : "Kinoko",
  "year" : 2021
}
two_patient_dictionary_dango = {
  "name" : "Dango",
  "year" : 2019
}
two_patient_dictionary_mochi  = {
  "name" : "Mochi",
  "year" : 2020
}



Problem 3: Set combinations

Given the predefined sets below and using set methods
3.a Is set E a subset of set A
 .b Is set E a strict subset of set A
 .c Create a set that is the intersection of set A and set B
 .d Create a set that is the union of sets C, D and E
 .e add 9 to the set
 .f Using == compare this set to the list in one_a
 .g Explain why they are not the same. What would you need to change if you
    wanted this to be True?
 

three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}



Problem 4: Changing variable types

For each step you will modify a variable, then append the type of the variable
to a list. Do not recreate the list variable, it should be a running list of 
types.

4.a Create a variable of type int with the value of 8
 .b Create an empty list 
 .c Using type(), add the type of 4.a to this list
 .d Add 0.39 to 4.c
 .e append the type of 0.39 to the list
 .f exponentiate to the -10, ie: 4.d^-10,(hint: there might be an artihmetic operator to do so) round it to no 
    decimal places, and append to list.
 .g append the type to the list
 
 
Problem 5: More variable type changes

Continue from where you left off in Problem 4.

5.a Manually create a dictionary where the values are items in the list from where we left in 
    problem 4, and the keys should be their index in the list. Print the dictionary.
 .b Add 300 and coerce it into a string
 .c append the type to the list
 .d slice the string up to the 2nd element
 .e append the type to the list
 .f use list comprehension to convert this into a new list of integers
 .g append the type to the list
 .h append the type of three_setA to the list
"""

#Start your assignment here
print("Assignment 3")



# %%
#Problem 1
print("Problem 1")
#problem 1 part a, create a list of interagers
one_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#print list
print(one_a)
#problem 1 part b, add 3 to the 5th element
one_b = one_a
#adding 3 to the list
one_b.insert(5, 3)
#print new list
print(one_b)
#problem 1 part c, making the list floats
one_c = [float(x) for x in one_b]
#print float list
print(one_c)
#problem 1 part d, make the list a set
one_d = set(one_c)
#print the new set
print(one_d)
#problem one part e, append int 10 into the set
one_e = one_d
#add 10 to the set
one_e.add(10)
#print appended set
print(one_e)
#problem 1 part f, pop an item from the set
one_f = one_e.pop()
#popped item printed
print(one_f)
#print set with popped item
print(one_e)
#problem one part g, count number of items in the set
one_g = len(one_e)
#print the number of items in the set
print(one_g)
#problem 1 part h, see if the numbers in the set are the same as the number of items in the list
one_h = one_g == len(one_c)
#print if the numbers of items are equivalent or not
print(one_h)
#problem 1 part i, add the set to the list from one_a
one_i = one_a + list(one_e)
#print the combined list
print(one_i)
#problem 1 part j, make the new list a set
one_j = set(one_i)
#printing the set
print(one_j)
#problem 1 part k, count number of elements in one_j
one_k = len(one_j)
#print the number of elements in one_j
print(one_k)

# %%
#Problem 2
print("Problem 2")
#problem 2 part a, create nested dictionary
two_a = {
    "patient_kinoko" : {
        "name" : "Kinoko",
        "year" : 2021
    },
    "patient_dango" : {
        "name" : "Dango",
        "year" : 2019
    },
    "patient_mochi" : {
        "name" : "Mochi",
        "year" : 2020
    }
}
#print dictionary
print(two_a)
#problem 2 part b, retrieve name from two_a
two_b = two_a["patient_dango"].get("name")
#print name
print(two_b)
#problem 2 part c, update "Mochi" year to 2019
two_a["patient_mochi"].update({"year" : 2019})
# print updated dictionary
print(two_a)
#problem 2 part d, create a single layer dictionary
two_d = {"Kinoko" : 2021, "Dango" : 2019, "Mochi" : 2019}
#print single layer dictionary
print(two_d)
#problem 2 part e, make a list of the keys of 2 part d
two_e = two_d.keys()
#print the keys
print(two_e)
#problem 2 part f, make a list of the values of two_d
two_f = two_d.values()
#print the values of two_d
print(two_f)
#problem 2 part g, combined keys and values back into a dictionary
two_g = dict(zip(two_e, two_f))
#print the dictionary
print(two_g)


# %%
#Problem 3
print("Problem 3")
#Given sets
three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}
#problem 1 part a
one_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#problem 3 part a, is E a sub set of A
three_a = three_setE <= three_setA
#print if E is a sub set of A
print(three_a)
#problem 3 part b, is E strict sub set of A
three_b = three_setE < three_setA
#print if E is a strict sub set of A
print(three_b)
#problem 3 part c, create a list that is an intersection of set A and set B
three_c = three_setA.intersection(three_setB)
#print intersection set
print(three_c)
#problem 3 part d, create a set that is a union of C, D, and E
three_d = three_setC.union(three_setD.union(three_setE))
#print union set
print(three_d)
#problem 3 part e, set 3 e = to 3 d
three_e = three_d.copy()
#add 9 to the set
three_e.add(9)
#print set with 9 added in
print(three_e)
#problem 3 part f, compare the set to the list from one_a
three_f = three_e == one_a
#print the comparison
print(three_f)
#problem part g,explain why they are different
print("The reason that the statement is false is because they are different types. If we want it to be true then we need to change the list to a set or the set to a list.")

# %%
#Problem 4
print("Problem 4")
#problem 4 part a, create a variable with type int with value of 8
four_a = int(8)
#print variable
print(four_a)
#problem 4 part b, create an empty list
four_b = list()
#print empty list
print(four_b)
#problem 4 part c, put 4c = to 4b
four_c = four_b
#add the type of list 4a to the list
four_c.append(type(four_a))
#print the new list
print(four_c)
#problem 4 part d, four d equal four c
four_d = four_c
#add 0.39 to the list
four_d.append(0.39)
#print updated list
print(four_d)
#problem 4 part e, appened the type of 0.39 into the list
four_e = four_d
#appeneding the type into the list
four_e.append(type(0.39))
#print updated list
print(four_e)
#problem 4 part f, expontiate -10
four_f = four_e
#raise 0.39 to the - 10
four_f.append(round(0.39 ** -10))
#print appened list
print(four_f)
#problem 4 part g, appened type into the list
four_g = four_f
#appending into the list
four_g.append(type(round(0.39 ** -10)))
#print new list
print(four_g)

#Problem 5
print("Problem 5")
#given information needed for problems
three_setA = {1,2,3,4,5}
#problem 5 part a, manually create dictionary
five_a = dict(zip(range(5), four_g))
#print the dictionary
print(five_a)
#problem 5 part b,add 300 to the list from 4
five_b = four_g
#add the string into the list
five_b.append(str(300))
#print the list
print(five_b)
#problem five part c, append the type into the list
five_c = five_b
#appending the type into the list
five_c.append(type(str(300)))
#print new list
print(five_c)
#problem 5 part d, slice string up to the 2nd element
five_d = str(300)
#slice string
five_d = five_d[:2]
#print sliced string
print(five_d)
#problem 5 part e, append type to the list
five_e = five_c
#appending type of 5d to list
five_e.append(type(five_d))
#print new list
print(five_e)
#problem 5 part f, convert 5d to a list of integers
five_f = [int(x) for x in five_d]
#print list of integers
print(five_f)
#problem 5 part g, appened type to list
five_g = five_e
#append type of five_f into list
five_g.append(type(five_f))
#print new list
print(five_g)
#problem 5 part h, append type of three_setA into the list
five_h = five_g
#append type into the list
five_h.append(type(three_setA))
#print list
print(five_h)


