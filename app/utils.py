from json.tool import main


def to_usd(my_price):
    """
    This is a docstring. This tells us what the function is about
    What its responsibilities are
    What the parameters are about
    What datatypes the parameters are
    What this function will return
    Example of invoking the function

    Invoke like this: to_use(9.9999)
    Example return value "$9.99"
    """
    return '${:,.2f}'.format(my_price)



#if this code is in the global scope
#of a file we're trying to import from
#it will throw errors when we try to run those 
#price = input("Please choose a price like 4.9999: ")
#print(to_usd(float(price)))

if __name__ == "__main__":
    #nesting the code in the main conditional will
    #allow other scripts to cleanly import functions from this file
    #without running this code
    # 
    # this code still gets run when we invoke the script from the command line  
    price = input("Please choose a price like 4.9999: ")
    print(to_usd(float(price)))

