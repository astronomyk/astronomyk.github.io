# Python Brackets - a basic introduction to Tuples, Lists, Arrays and Function 
---

This little introduction came out of a WhatsApp conversation I had with Sophie, 
trying to explain the nuances of python backets. It may be useful for others =)

Tuples, Lists and Arrays
------------------------

I'm gunno go full on basic here, just ignore stuff that you already know. 
In python everything is an "object": variables and function.
Its just that variables can't do anything, where as functions can.
I like to think of variables like buckets. You have to fill them with something i.e. 

    >>> my_var = 10
    
If `my_var` is a tuple, an array or a list, then it has multiple instances of the something in it:


    >>> my_tuple = (1,2,3)
    >>> my_list = [1,2,3]
    >>> my_array = np.array([1,2,3])

Tuples and lists are built into python, while arrays come from an outside source, i.e. numpy.
These examples are all 1-Dimensional. I can access any specific part of these variables using []:

    >>> my_list[1]
    2

Function calls vs Tuples
------------------------
    
Now before I go onto 2-D objects I'll just say something quickly about functions.

Tuples are called with (), lists are called with [].
However functions also use ().
Functions are code blocks which do a bunch of things and then return a value:
e.g. `np.sqrt(4)` will return 2
Here again the () are used as a way of connecting to the function.

As a side note, the insides of the function look like this:
    
    def my_func(parameter1, parameter2, etc):
        ...
        <do_a_bunch_of_calculations>
        ...
        return final_value

If you want to get `final_value` you need to call the function:
    
    >>> my_final_value = my_func(param1, param2)
    
In the "function call" I left out the `:` because I only need `:` in the "function definition".
The `:` tells python that the following lines of code should always be executed when I call the function name.
If I were to tell python:

    >>> a = my_func

this wouldn't return anything useful. I need to add () to the end of any function call.
It would have to be:

    >>> a = my_func()

Anything I put inside the () of a function call is then passed to the function for it to use.
Hence why we call the function np.array() and then put a list inside it if we want to get a numpy array object:

    >>> np.array([1,2,3])

`np.array(my_list)` would also turn `my_list` into an array.

Here we see the double usage of the ()

* () alone makes a tuple, 
* whereas () attached to a name will make a function call, i.e. my_func()

    >>> my_tuple = (...)
    >>> my_final_val = my_func(...)
        
In a similar vein, the same can be said of the []. When the [] are attached to a variable name, they "slice" the variable.
This basically means that by using [] you can pull out a certain single entry from a multi-entry variable (e.g. an array or list or tuple):

    >>> my_list = [...]
    >>> a_value = my_list[...]

How are we going? Now that we have the difference between a tuple and a function call, and a list and a slice operation, what is `a` here:

    >>> a = np.array([1,2,3])[0]
    1

What is happening in that whole line?
In short: we've taken a list and put it inside an array that we've taken from the module `numpy` (`np`). The [0] means we're taking a slice

There's a little nuance here though.
We created a list [1,2,3], and passed the list to the function `np.array()`. 
That function returns an array object with the values [1,2,3] inside. 
We then slice, or call, the 0th element and pass that to the variable `a`.

Here we need to be careful. `np.array()` is the function call, but the object that it returns is also called an array.
Actually its type is an `ndarray`. If you use the function call `type()` it will return `np.ndarray`.
A `ndarray´ is an N-dimensional array because the object can hold any number of dimensions.

Anyway, the point here is that np.array() is a function call, and not an object type:

N-dimensional stuff
-------------------

Now back to python basics, there are () and []
and they can be combined with each other:

    `([])` or `[()]`

One is a tuple which contains inside a list, the other a list which contains a tuple.
Other possibilities are 

    [(),(),()]
    ([],[],[])
    [[],[],[]]
    ((),(),())
    
As a side note, I rarely use tuples. I prefer to reserve my () for function, so I know when I'm calling a function.

This is a list of lists. More precicely 3 lists inside a list:

    [[],[],[]]

But to access any single number, you need to first extract the desired "inside-list" from within the "outside-list".
We do that with slicing:

    >>> my_dbl_list = [[1,2,3], [4,5,6]]
    >>> my_dbl_list[0]
    [1,2,3]
    >>> my_dbl_list[0][0]
    1
    
What will `my_dbl_list[2][1]` return?
Python works from 0 up, we dont have a 2 value here so it wont return anything. It throws an error because I don't have enough elements in my first dimension.
A trick question ;) But `my_dbl_list[1][2]` will return `6`.

The `len()` function is quite useful for lists. `len(my_dbl_list)` will return 2 as there are only 2 elements in the my_dbl_list.
It just happens that each of the two elements are themselves lists, each with 3 elements.
That's where the term lists of lists comes from.
Here `my_dbl_list` is "just" a single list and will act like a single list but when you slice it, what comes out is again a list:

    >>> my_sgl_list = my_dbl_list[0]
    >>> print(my_sgl_list)
    [1,2,3]
    >>> my_sgl_list[0]
    1
        
Those last couple of lines should make complete sense now =)

While a 2D list is technically correct it's better to think of them as a list of lists, **BUT** that's not the same for arrays.
For lists you notice that we always slice one layer down at a time 

    >>> fruit[][][]
    
where the [] are successively after each other.
The object that the function `np.array()` returns gives us a bit more matrix-like functionality:

    >>> my_arr = np.array([[1,2,3],[4,5,6]])

 but we can still access it like a list of lists:

    >>> my_arr[0][0]
    1

But we can also do away with the second set of [] and access elements like in a matrix.
With `my_arr[0,0]` this will give us the top left element.

One thing to note is that when you are setting the arrays the number of dimensions that you have is equal to the number of opening brackets you have.
So now `my_arr` is two lists inside a list inside an array which is 2D. The () belong to the function call and so can be ignored. The [] are what count.
Here we have [[1,2,3],[4,5,6]], so opening with [[, so it's 2D. Meaning we need two indexes to access any single number:
    
    >>> my_arr[0,0]
    1
    
How many dimensions does `np.array([[1],[2],[3]])` have?

Its 2D since it opens with [[. Technically it's a 3x1 2D array. As compared with [1,2,3] which is a 3x1 1D array. 
It doesn't matter about the numbers it matters about the brackets

To access any individual number in `[[1],[2],[3]]`, what would you do? How would you extract the 3?
You could use:

    >>> my_arr[0][2]

The 0 gets you in the first set of brackets and the index 2 gets you to the value 3. Although, here we're using the slicing technique for lists.
How would it change for an array?

    [0][2] -> [0,2]

Arrays get rid of the confusing amounts of brackets that are needed by lists of lists.
For a 5 dimensional list 

    a = [[[[[42]]]]]

you would have to access the value 42 with 

    >>> a[0][0][0][0][0]
    42

If you did a[0][0][0] what would you get? `[[42]]`. But with an array, 

    >>> a = np.array( [[[[[42]]]]] ) 
    
It's still confusing, but easier to read
    
    >>> a[0,0,0,0,0]
    42
    >>> a[0,0,0]
    [[42]]

What do the following return? 

    >>> [[42,21], [11,5]][1][0]
    11
    >>> [[42,21], [11,5]][0][1]
    21
    
Now hopefully we understand the nuance behind the different meanings of the brackets. 
That's probably one of the trickiest things to get your head around with python
All the coding should make a lot more sense now.

One last thing for arrays

    >>> my_arr = [[1,2,3],[4,5,6]]

if I call the print function 
    
    >>> print(my_arr)
    [[1, 2, 3],
     [4, 5, 6]]

How do I slice out a column or a row, not just a single number? I use the : as a place holder

    >>> my_arr[0,0]
    1
    >>> my_arr[0, : ]
    [1,2,3]
    >>> my_arr[ : , 0]
    [1,4]
    
(At least I think it's that way around)
After all these years I still get confused as to the order of array slicing with `:`