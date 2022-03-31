#each test file must be called test_something.py or something_test.py
#each directory must be called test/tests/something with test 
#this is the "tests/util_test.py" file

# def test_answer():
#     assert inc(3) == 5 

from app.utils import to_usd #from foldername.filename import function 

def test_to_usd(): #test function should be called test_something
    #it rounds to 2 decimal places and have a $

    assert to_usd(0.455555) == "$0.46"


    #if large number, should use thousands separator:
    assert to_usd(123454645.98) == "$123,454,645.98"
    

#run pytest from command line
#for tests to find the code properly, create new file in root directory - helps pytest find tests