#  Solutions to this problem: http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
def list_function(a):
    new_list = [i for i in a if i < 5]  # One liner to print the new list.
    print("New list is: %s" % new_list)

    extra_list = []

    for j in a:
            if j < num:
                extra_list.append(j)
    print("Extra list is: %s" % extra_list)


num = int(input("Give me a number: "))


list_function([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
