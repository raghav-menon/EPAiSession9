## Tuples
   ------
Tuple is an immutable (unchangeable) collection of elements of different data types. It is an ordered collection, 
so it preserves the order of elements in which they were defined.Tuples are defined by enclosing elements in 
parentheses () [Tuples can be defined even without a paranthesis just byy seperating the objects using a comma], 
separated by a comma. Tuples are used to store multiple items in a single variable. Tuple is one of 4 built-in 
data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different 
qualities and usage. Tuple items are ordered, unchangeable, and allow duplicate values.Tuple items are indexed, the 
first item has index [0], the second item has index [1] etc. 

### Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

### Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

### Allow Duplicates
Since tuples are indexed, they can have items with the same value

Thus every property about lists i.e. they are ordered, they can contain arbitrary objects, they can be indexed and sliced,
they can be nested—is true of tuples as well but they cannot be modified.


### Why to use a tuple instead of a list

1. Program execution is faster when manipulating a tuple than it is for the equivalent list. 
   (This is probably not going to be noticeable when the list or tuple is small.)

2. Sometimes we don’t want data to be modified. If the values in the collection are meant to 
   remain constant for the life of the program, using a tuple instead of a list guards against 
   accidental modification.

3. When compared to a dictionary, which requires as one of its components a value that is of an immutable type. 
   A tuple can be used for this purpose, whereas a list can’t be.

## NamedTuples
   -----------
Python’s collections module provides a factory function called namedtuple(), which is specially designed to make the code 
more Pythonic when working with tuples. With namedtuple(), we can create immutable sequence types that allow you to access 
their values using descriptive field names and the dot notation instead of unclear integer indices.

Python’s namedtuple() is a factory function available in collections. It allows us to create tuple subclasses with named fields. 
We can access the values in a given named tuple using the dot notation and the field names, like in obj.attr.

Python’s namedtuple was created to improve code readability by providing a way to access values using descriptive field names instead 
of integer indices, which most of the time don’t provide any context on what the values are. This feature also makes the code cleaner 
and more maintainable.

In contrast, using indices to values in a regular tuple can be annoying, difficult to read, and error-prone. This is especially true 
if the tuple has a lot of fields.

### Properties

1. Are immutable data structures
2. Have a consistent hash value
3. Can work as dictionary keys
4. Can be stored in sets
5. Have a helpful docstring based on the type and field names
6. Provide a helpful string representation that prints the tuple content in a name=value format
7. Support indexing
8. Provide additional methods and attributes, such as ._make(), _asdict(), ._fields, and so on
9. Are backward compatible with regular tuples
10. Have similar memory consumption to regular tuples


## Assignment
  -----------
1. Use the Faker (Links to an external site.)library to get 10000 random profiles. Using namedtuple, calculate the largest blood type,
   mean-current_location, oldest_person_age, and average age (add proper doc-strings). - 250 (including 5 test cases)
2. Do the same thing above using a dictionary. Prove that namedtuple is faster. - 250 (including 5 test cases)
3. Create fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). 
   Assign a random weight to all the companies. Calculate and show what value the stock market started at, what was the highest value during the day,
   and where did it end. Make sure your open, high, close are not totally random. You can only use namedtuple. - 500  (including 10 test cases)

## Using Faker Library
   --------------------
In this question we have been asked to use Faker library t generate 10000 random profiles. Initially the Faker library is installed using 'pip' command.
Once installed, the library is imported and instantiated. Assume that it has been instantiated to a variable 'fake'. Calling fake.profile() will generate 
a fake profile with differnt keys. The keys avaliable can be displayed by printing the result of fake.profile().keys(). A namedtuple called Profile can be
created with the necessary fields using

Profile = namedtuple('Profile', fake.profile().keys())

Values can be stored in using the profile created in an object by using

pr_store = Profile(**fake.profile())

For initializing 10000 random profiles, we have the following function

### init_profiles_using_namedtuple(no_profiles: int)
    This function is called with the number of profiles to be created as an input. The function returns a list of profiles where each profile is a namedtuple.

## timed
   -----
The 'timed' decorator is used here to evalaute the time taken in executing the functions for calculating the average age, mean-current location, largest
blood type and oldest persons age for both namedtuple and dictionary. This is in order to determine the time taken for executing each and check which is 
faster. 

### Question 1
    ----------
For solving Question 1, we have the following functions:

### oldest_person_nt
    This function takes in the list of namedtuples and determines the age of the oldest person. Here we use a lambda function to calculate the age. The
    min birthdate is determmined and subtracted from todays date and the difference in days is determined. This difference value divided by 365 and converted
    to an integer gives his current age which is returned.

### average_age_nt
    This function takes in the list of namedtuples and finds the age for each person. For this we use a lambda function. The individual's age is taken and 
    subtracted from the current year from today's date. If the month and date from today's date is less than the month and date from the birth year +1 is added 
    to the difference obtained above. Using a map function, we calculate the ages for all the profiles. Sum of all these divided by the number of profiles gives 
    the average age.

### average_coords_nt
    This function takes in a list of namedtuple profiles and finds the average coordinates. We use a lambda function and a map function. The coordinates are 
    taken and the sum of all the coordinates are found which is divided by the number of profiles to get the average coordinates.

### max_bloodgroup_nt
    This function returns the blood group that is occuring maximum number of times. With the help of map and lambda function, we retrieve the blood groups and find
    the mode of all the blood groups. The mode provides us with the blood group that occurs maximum number of times.

### time_nt
    This function is used to calculate the amount of average time taken to run N calls to each of the functions using a namedtuple.


## Question 2
   ----------
Here we have to perform the operations done above but with a dictionary. First all the 10000 profiles are converted into a dictionary using the following command:

fk_Profile_dict = {'Profile'+str(_):t._asdict() for _, t in enumerate(fk_Profile_nt)}

In the program, we use 'namedtup_dict' fuction to convert a namedtuple to dictionary.This is done in order to keep all the profiles same and hence check whether the 
results are the same. For Question 2 we use the following function:

### oldest_person_dc
    This function takes in a dictionary and determines the age of the oldest person. Here we use a lambda function to calculate the age. The
    min birthdate is determmined and subtracted from todays date and the difference in days is determined. This difference value divided by 365 
    and converted to an integer gives his current age which is returned.

### average_age_dc
    This function takes in a dictionary of profiles and finds the age for each person. For this we use a lambda function. The individual's age is taken and 
    subtracted from the current year from today's date. If the month and date from today's date is less than the month and date from the birth year +1 is added 
    to the difference obtained above. Using a map function, we calculate the ages for all the profiles. Sum of all these divided by the number of profiles gives 
    the average age.

### average_coords_dc
    This function takes in a dictionary of profiles and finds the average coordinates. We use a lambda function and a map function. The coordinates are 
    taken and the sum of all the coordinates are found which is divided by the number of profiles to get the average coordinates.

### max_bloodgroup_dc
    This function returns the blood group that is occuring maximum number of times. With the help of map and lambda function, we retrieve the blood groups and find
    the mode of all the blood groups. The mode provides us with the blood group that occurs maximum number of times.

### time_dc
    This function is used to calculate the amount of average time taken to run N calls to each of the functions using dictionary.

## Question 3
   ----------
Here we simulte a Fake Stock market for 100 stocks. We have 2 functions here

### symbol
    This function generates the symbol for the fake company. The function takes the company name as its input and generates 2 random integers within the length of
    the string, capitalizes the character in those positions and returns a string by joining all the capitalizd letters. This is done to keep the company symbol 
    unique.

### stock_market
    Initially we create a market capital by creating random N values. Then we create random weights which is normalized so that their sum equals 1. Once that is done,
    we start creating the stock exchange values. The open values for each Company would be the Market capital multiplied by the weights. The high value is obtained by multiplying
    the open value with a unform random number between 0.85 and 1.15. Similarly, the close value is obtained by multiplying the open value with a uniform random number between 0.75 and 1.15.
    Conditions are checked whether the open value > high and if the high < close in which case it is assigned to those values. The calculated values are stored in a named tuple and
    displayed. The start of the day value is given by multiplying each value in open with the weights and finding the sum. Similar procedure is done for obtaining the values for high and
    close. The function returns a tuple with all the N profiles, start of the day value, highest of the day value and close.

## Tests
   ------
The following are the tests written for each of the questions:

### Question 1 --> For Namedtuples
    ------------------------------
1.  test_q1_number_of_nt_profiles() --> Checks the number of profiles created is equal to the number given as input
2.  test_q1_average_age_nt() --> Tests whether the average age is properly calculated
3.  test_q1_oldest_person_nt() --> Tests whether the oldest person is being identified properly
4.  test_q1_average_coords_nt() --> Checks whether the average coordinates is being calculated properly
5.  test_q1_max_bloodgroup_nt() --> Checks whether the blood group that occurs maximum number of times is returned properly

### Question 2 --> For Dictionary
    -----------------------------
1.  test_q2_type_of_value() --> Checks whether the profiles are being converted from namedtuples to dictionary and returned in proper type
2.  test_q2_average_age_dc() --> Tests whether the average age is properly calculated using dictionary
3.  test_q2_oldest_person_dc() --> Tests whether the oldest person is being identified properly using dictionary
4.  test_q2_average_coords_dc() --> Checks whether the average coordinates is being calculated properly using dictionary
5.  test_q2_max_bloodgroup_dc() --> Checks whether the blood group that occurs maximum number of times is returned properly by the use of dictionary
6.  test_q2_fastest_nt_dc() --> Checks which is the fastest, a namedtuple or dictionary by calling the functions 1000 times and finding average

### Question3 --> Fake Stock Market
    -------------------------------
1.  test_q3_no_profiles_generated()  --> Checks whether there are N profiles generated
2.  test_q3_doc_string() --> Checks whether the stock_market function contains a doc string
3.  test_q3_annotations() --> Checks whether the stock_market function contains annotations
4.  test_q3_unique_symbol() --> Checks whether the symbols generated for companies are unique
5.  test_q3_return_namedt() --> Checks whether the returned value from stock_market is a tuple
6.  test_q3_normalized_wts() --> Checks if the weights are normalized
7.  test_q3_highd_lowd() --> Checks if the Highest value of the day is greater than or equal to the close
8.  test_q3_all_high_low() --> Checks if each of the high value generated is > = close
9.  test_q3_docstring_namedtuple() --> Checks the docstring of named tuple
10. test_q3_docstring_symbol() --> Checks if docstring is present in symbol function
11. test_q3_string_annotations() --> Checks if annotation is present in symbol function



