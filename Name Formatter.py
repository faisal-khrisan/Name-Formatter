def format_name(f_name,l_name):
    """ This Function take first and last name and formating it based on your preference upper, lower and title case"""
    # Upper case :
    if choice==1:
        f_name.upper()
        l_name.upper()
        return f" Your name is { f_name.upper()} {l_name.upper()} "
    # Lower case :
    elif choice==2:
        f_name.lower()
        l_name.lower()
        return f"Your name is {f_name.lower()} {l_name.lower()}"
    # Title Case :
    elif choice == 3:
        count = 0
        count1 = 0
        f_name_first = ""
        l_name_first = ""
        for letter in f_name:

            if count == 0:
                f_name_first += letter.upper()
            else:
                f_name_first += letter
            count += 1
        for letter in l_name:
            if count1 == 0:
                l_name_first += letter.upper()
            else:
                l_name_first += letter
            count1 += 1
        return "Your name is {f_name_first} {l_name_first}"
    else:
        return "Invalid input"

stop=True
while stop:

        first=str(input("What is your first name : "))
        last=str(input("What is your last name : "))
        choice=int(input("Would you like to captlize your name or make it slower or you want to captlize each first letter (Title case) \n"
                      "Menue:\n"
                      "1- Type ( 1 ) for all captile\n"
                      "2- Type ( 2 ) for all small \n"
                      "3- Type ( 3 ) for captlize each first letter\n "
                      "   Your Choice is : "))
        output= format_name(first,last)
        print(output)
        ask=str(input("Would you like to continue yes | no  : "))
        if ask.lower()=='no':
            stop=False
