
while True:
    print("=" * 40)
    print("\033[1m" + "     * FUNDAMENTALS OF PROGRAMMING *" + "\033[0m")
    print("=" * 40)


    print("\n[0] INTRODUCTION")
    print("[1] PRELIMINARY LESSON")
    print("[2] MIDTERM LESSON")
    print("[3] FINAL LESSON")
    print("[E] EXIT")


    choice = input("\n Enter your lesson: ").upper()


    if choice == "0":
        print("\nYou selected: 0. INTRODUCTION")
        print("\n")
        print("=" * 100)
        print("\033[1m" + "                                       INTRODUCTION TO PROGRAMMING " + "\033[0m")
        print("=" * 100)
        print("\n\033[1m" + "                                       WHAT IS PROGRAMMING LANGUAGE " + "\033[0m")
        print("                               A programming language is a special language")
        print("                            that computers understand and use to perform tasks.")
        print("\n\033[1m" + "                                   COMMON PROGRAMMING LANGUAGES INCLUDE" + "\033[0m")

        print("\n\033[1m" + "     [ PYTHON ]" + "\033[0m""\033[1m" + "                           [ C / C++ ]" + "\033[0m""\033[1m" + "                            [ PHP ]" + "\033[0m")
        print("     Easy to learn and read.""              High performance""                       Used for web development.")
        print("     Great for beginners,""                 and efficient""                          Work well with")
        print("     data science, and ""                   Used in system programming,""            databases and")
        print("     automation.""                          games, and applications.""               server-side scripting.")

        print("\n\033[1m" + "     [ JAVA ]" + "\033[0m""\033[1m" + "                             [ JAVASCRIPT ]" + "\033[0m""\033[1m" + "                         [ RUBY ]" + "\033[0m")
        print("     Platform-Independent""                 The language of""                        Known for simplicity")
        print("     and widely used.""                     the web.""                               and productivity.")
        print("     great for apps and ""                  Adds interactivity ""                    Used in web")
        print("     systems.""                             to websites.""                           development.")

        print("\n 💡  Each language has its own strengths. Choose the right tool for the right job!   </>")

        while True:
            back = input("\n Select [X] to return to the main list: ").upper()
            if back == "X":
                print("\n" * 2)
                break
            else:
                print(" Invalid input. Please enter 'X' to return.")


    elif choice == "1":

        while True:
            print("=" * 40)
            print("\033[1m" + "           PRELIM LESSON LIST" + "\033[0m")
            print("=" * 40)

            print("\n [1] PYTHON INTRO")
            print(" [2] PYTHON SYNTAX")
            print(" [3] PYTHON OUTPUT")
            print(" [4] PYTHON COMMENTS")
            print(" [5] PYTHON VARIABLES")
            print(" [6] PYTHON DATA TYPES")
            print(" [7] ARITHMETIC OPERATORS AND EXPRESSIONS")
            print(" [8] BASIC INPUT AND OUTPUT IN PYTHON")
            print(" [X] BACK TO MAIN MENU")

            prelim_choice = input("\nEnter your sub-lesson: ").upper()
            print("\n" * 2)

            if prelim_choice == "1":
                print("=" * 100)
                print("\033[1m" + "                                          PYTHON INTRO" + "\033[0m")
                print("=" * 100)
                print("\033[1m" + " What is Python Programming" + "\033[0m")
                print(" Python is a widely-used programming language that was created by\033[1m" + " Guido van Rossum in 1991." + "\033[0m")
                print("\n A\033[1m" + " dutch software engineer" + "\033[0m"" best known for creating the Python programming language in 1991.")
                print(" he designed Python with the goal of making programming simple, readable, and easy")
                print(" to learn while remaining powerful enough for professional software development.")

                print("\n Example:")
                print(" print('Hello World')")
                print(" The print() function displays text on the screen")

                while True:
                    back = input("\n Select [X] to return to the prelim list: ").upper()
                    if back == "X":
                        print("\n" * 2)
                        break
                    else:
                        print(" Invalid input. Please enter 'X' to return.")


            elif prelim_choice == "2":
                print("=" * 100)
                print("\033[1m" + "                                          PYTHON SYNTAX" + "\033[0m")
                print("=" * 100)
                print("- Syntax refers to the set of rules that tell us how to correctly")
                print("  write a program in Python.")
                print("  There are two major rule sets to know:")
                print("\n\033[1m" + "A. Python is Case-Sensitive:" + "\033[0m")
                print(" Python treats uppercase and lowercase letters differently.")
                print("\n Example: ✔")
                print(" name = 'John' ⟶ Create variable name")
                print(" print(name)   ⟶ Print the value of name")
                print("\nExample: ✘")
                print(" name = 'John'")
                print(" print(Name)   ⟶ Error! Name is not the same as name.")
                print(" ⚠️ Python is case-sensitive.")
                print("\n\033[1m" + "B. INDENTATION:" + "\033[0m")
                print("- Unlike other programming languages, Python uses indentation")
                print("  (spaces) to define blocks of code.")
                print("\n Example: ✔")
                print(" age = 18         ←  Assign value to variable")
                print(" if age >= 18:    ←  Check condition")
                print("    print('Adult') ←  Indented (inside the block)")

                while True:
                    back = input("\n Select [X] to return to the prelim list: ").upper()
                    if back == "X":
                        print("\n" * 2)
                        break
                    else:
                        print(" Invalid input. Please enter 'X' to return.")

            elif prelim_choice == "3":
                print("=" * 40)
                print("\033[1m " + "                                          PYTHON PRINTING OUTPUT""\033[0m")
                print("=" * 40)

                print(" The\033[1m " + "print ():""\033[0m ""function displays information""function displays information")
                print(" one the screen")
                print("\n\033[1m " + "Print Statement""\033[0m")
                print("\033[1m " + "Syntax:""\033[0m")
                print(" print('value')")

                print("\n\033[1m " + "print -""\033[0m ""the function that displays output.")
                print("\n\033[1m " + "() -""\033[0m ""parentheses that contain the information to be displayed.")
                print("\n\033[1m " + "value -""\033[0m ""the text, number, variable, or expression you want to show.")


                print("\n\033[1m " + "Print Text""\033[0m")
                print("\033[1m " + "Text -""\033[0m""(also called a string) must be enclosed in""\033[1m " + "quotation marks.""\033[0m")
                print("\n Example: ✔")
                print("                              👍")
                print(" print('Hello World!') ⟶\033[1m " + "Correct syntax ""\033[0m")
                print("                        Used double quotes")
                print("                        inside the parentheses.")

                print("\n Example: ✘")
                print("                              ⚠️")
                print(" print(Hello World!)   ⟶\033[1m " + "Incorrect syntax ""\033[0m")
                print("                        Missing quotes around")
                print("                        the text")

                print("\n\033[1m " + "Print Numbers""\033[0m")
                print(" You can""\033[1m " + "print numbers""\033[0m"" directly without quotation marks.")

                print("\n Example: ✔")
                print("                             OUTPUT    ""\033[1m " + "Numbers(int, float)""\033[0m")
                print(" print(100)            ⟶      100       numbers are used       ")
                print(" print(25.5)                  25.5      without quotes. ")

                print("\n Example: ✔ ALSO CORRECT  (DIFFERENT DATA TYPE )")
                print("\n                             OUTPUT    ""\033[1m " + "Strings(str)""\033[0m")
                print(" print('100')          ⟶      100       Values inside quotes are       ")
                print(" print('25.5')                25.5      text (strings). ")

                while True:
                    back = input("\n Select [X] to return to the prelim list: ").upper()
                    if back == "X":
                        print("\n" * 2)
                        break
                    else:
                        print(" Invalid input. Please enter 'X' to return.")

            elif prelim_choice == "4":
                print("=" * 100)
                print("\033[1m " + "                                          PYTHON COMMENTS""\033[0m")
                print("=" * 100)

                print(" Comments\033[1m " + "are ignored:""\033[0m ""by Python.")
                print(" They are\033[1m " + "used to explained the code.""\033[0m")

                print("\n Example: ✔ \033[1m " + "SINGLE LINE COMMENT:""\033[0m\n")
                print(" # This is a comment        ⟶        Uses the hash symbol #")
                print("                                     Comment continues until")
                print("                                     the end of the line.")
                print("\n print ('Hello')  \033[1m " + "                  Used for:""\033[0m")
                print("                                     • Short explanations")
                print("                                     • Disabling a line of code")
                print("                                     • Quick notes")

                print("\n Example: ✔ \033[1m " + "MULTI-LINE COMMENT:""\033[0m\n")
                print(" '''                                 Uses triple quotes''' ")
                print(" This is                             Comment continue")
                print(" a multi-line                        until closing'''.")
                print(" comment.")
                print(" '''")
                print(" print ('Hello')  \033[1m " + "                   Used for:""\033[0m")
                print("                                     • Long explanations")
                print("                                     • Describing functions")
                print("                                     • Adding documentation")

                while True:
                    back = input("\n Select [X] to return to the prelim list: ").upper()
                    if back == "X":
                        print("\n" * 2)
                        break
                    else:
                        print(" Invalid input. Please enter 'X' to return.")

            elif prelim_choice == "5":
                print("=" * 100)
                print("\033[1m " + "                                          VARIABLES""\033[0m")
                print("=" * 100)

                print(
                    "\n A\033[1m " + "variable:""\033[0m ""is a named.""\033[1m " + "storage used to keep data in a program.""\033[0m")
                print(" The value of a variable can change while the program is running.")

                print("\n Example: \033[1m " + "a, b, c, age, name""\033[0m")
                print("\n Variable name ⟶ \033[1m " + "age ""\033[1m " + " name""\033[0m"" ← Variable name")
                print(" Stored value  ⟶ \033[1m " + "20 ""\033[1m " + " 'John'""\033[0m"" ← Stored value")

                print("\n\033[1m " + "VARIABLE NAMING RULES:""\033[0m")
                print(" A variable can have a\033[1m " + "short name""\033[0m"" (like x and y) or")
                print(" a more \033[1m " + "descriptive name""\033[0m"" (age, carname, total_value).")

                print("\n • A variable name\033[1m " + "must start a letter""\033[0m""or the")
                print("\033[1m " + "  underscore character.""\033[0m")
                print("\n Example: ✔")
                print(
                    "\n\033[1m " + "       age     ""\033[0m""\033[1m " + "       _value     ""\033[0m""\033[1m " + "       total     ""\033[0m")
                print("      age = 20       _value = 100        total = 50")
                print("         ↑                 ↑                   ↑")
                print("     start with        start with         start with")
                print("      a letter         underscore          a letter")

                print("\n • A variable name\033[1m " + "cannot start with a number.""\033[0m")
                print("\n Example: ✘")
                print(
                    "\n\033[1m " + "     1stValue     ""\033[0m""\033[1m " + "     2total     ""\033[0m""\033[1m " + "      123name     ""\033[0m")
                print("    1stValue = 10      2total = 30    123name = 'john'")
                print("         ↑                  ↑                 ↑")
                print("     start with         start with        start with")
                print("      a number           a number          a number")

                print("\n Variable names are case-sensitive")
                print(" (\033[1m " + "age""\033[0m"" and""\033[1m " + "AGE""\033[0m"" are two different variables)")
                print("\n           variable 1                    variable 2")
                print("            \033[1m " + " age" + "                            AGE""\033[0m")
                print("              18               ≠             25")
                print("   This is a variable named        This is a variable named")
                print("            \033[1m " + " age" + "                            AGE""\033[0m")

                print("\n\033[1m " + "ASSIGN VALUE TO VARIABLE""\033[0m")
                print(" in programming, we store data in variables. We assign a value")
                print(" to a variable using the\033[1m " + "= (assignment operator)""\033[0m")
                print("                         ↓")
                print(
                    "\033[1m " + "             first_name""\033[0m""\033[1m " + "=""\033[0m""\033[1m " + "'John'""\033[0m")
                print("                   ↑         ↑ ")
                print("\033[1m " + "      ↱   📦VARIABLE NAME""\033[0m""\033[1m " + "📦VALUE   ↰""\033[0m")
                print(" The name we choose           The data we store      ")
                print(" to represent the data        in the variable")
                print(" (follows naming rules.)      (can be text, numbers, etc.)")

                print("\n\033[1m " + "OUTPUT VARIABLES""\033[0m")
                print(" The Python\033[1m " + "print () function" "\033[0m""is often used to output variables.")

                print("\n\033[1m " + "EXAMPLE CODE""\033[0m")
                print(
                    " school =\033[1m " + "'Clark College'""\033[0m"" ----⟶     We store the text""\033[1m " + "'Clark College'""\033[0m")
                print("                                    in variable named\033[1m " + "school.""\033[0m")

                print(
                    "\n\033[1m " + "print""\033[0m""(school) ---------------⟶     We use""\033[1m " + "'print()'""\033[0m""to display value of")
                print("                                    the variable \033[1m " + "school.""\033[0m")

                print("\n\033[1m " + "OUTPUT""\033[0m")
                print(" Clark  College""               ✔    The value stored")
                print("                                    in\033[1m " + "school""\033[0m""is displayed")
                print("                                    on the screen.")

                print(
                    "\n In the print() function, your output\033[1m " + "multiple variables separated by a comma and + sign.""\033[0m")
                print("\n\033[1m " + "EXAMPLE CODE""\033[0m")
                print(" a = 'I'""------------------ Store 'I' in a variable a")
                print(" b = 'Love'""--------------- Store 'Love' in a variable b")
                print(" c = 'CCST'""--------------- Store 'CCST' in a variable c")
                print("\n # print multiple variables")
                print("\n print(a, b, c)"" or print(a + b + c)""---------- print() display the values")
                print("                                              of a, b, and c, separated")
                print("                                              by space.")

                while True:
                    back = input("\n Select [X] to return to the prelim list: ").upper()
                    if back == "X":
                        print("\n" * 2)
                        break
                    else:
                        print(" Invalid input. Please enter 'X' to return.")

            elif prelim_choice == "6":
                print("=" * 100)
                print("\033[1m " + "                                          DATA TYPES""\033[0m")
                print("=" * 100)

                print("\n\033[1m " + "Data types :""\033[0m""\033[1m " + "                                 int""\033[0m" "              Whole number (no decimal part).")
                print(" Are categories that tell Python""               Integer numbers""\033[1m " + " Example 10, 25, -7, 100""\033[0m")
                print(" what kind of data a variable stores.""\033[1m " + "         float""\033[0m" "            Numbers with a decimal point.")
                print(" They determined the type of value""             Decimal numbers""\033[1m " + " Example 12.5, 3.14, -0.001, 2.0""\033[0m")
                print(" a variable can hold and what operations.""\033[1m " + "     str""\033[0m" "              Text or characters inside quotes.")
                print(" can be performed on that value.""               String or text""\033[1m " + "  Example 'Hello', 'Juan', 'CCST'""\033[0m")
                print("\033[1m " + "                                              bool""\033[0m""             Represents one of two values: True or False")
                print("                                               Boolean values ""\033[1m " + " Example True or False""\033[0m")

                print("\n\033[1m " + "Declaration of Variables""\033[0m")
                print("\n\033[1m " + "                             VARIABLE""\033[0m""\033[1m " + "    VALUE""\033[0m""\033[1m " + "    DATA TYPE""\033[0m""\033[1m " + "    DESCRIPTION""\033[0m")
                print(" name =\033[1m " + "'Maria'""\033[0m""                 name""      'maria'""    str""           Stores text")
                print("                                                     (string)      inside quotes.")
                print(" age =\033[1m " + "20""\033[0m""                       age""         20""       int""           Stores whole")
                print("                                                     (integer)     numbers.")
                print(" grade =\033[1m " + "89.5""\033[0m""                   grade""      89.5""      float""         Stores numbers with")
                print("                                                     (decimal)     decimals points.")
                print(" is_enrolled =\033[1m " + "True""\033[0m""         is_enrolled""    True""      bool""          Stores True or ")
                print("                                                     (boolean)     False values.")

                while True:
                    back = input("\n Select [X] to return to the prelim list: ").upper()
                    if back == "X":
                        print("\n" * 2)
                        break
                    else:
                        print(" Invalid input. Please enter 'X' to return.")

            elif prelim_choice == "7":
                print("=" * 100)
                print("\033[1m " + "                                   ARITHMETIC OPERATORS AND EXPRESSIONS""\033[0m")
                print("=" * 100)

                print("\n WHAT ARE ARITHMETIC OPERATORS?")
                print("\033[1m " + "Arithmetic operators""\033[0m""are symbols used to perform mathematical calculations")
                print(" on numbers. They work the same way as the operators used in everyday mathematics.")

                print("\n\033[1m " + "                 PYTHON ARITHMETIC OPERATORS""\033[0m")
                print("\n\033[1m " + "OPERATOR""\033[0m""\033[1m " + "          DESCRIPTION""\033[0m""\033[1m " + "          EXAMPLE""\033[0m""\033[1m " + "     RESULT""\033[0m")
                print("    +""               Addition""              5 + 3""          8")
                print("    -""               Subtraction""           10 - 4""         6")
                print("    *""               Multiplication""        7 * 2""         14")
                print("    /""               Division (float)""      15 / 3""        5.0")
                print("    //""              Floor Division""        17 // 3""        5")
                print("    %""               Modulus""               10 % 3""         1")
                print("    **""              Exponentiation""        2**3""           8")

                print("\n\033[1m " + "EXPRESSIONS IN PYTHON""\033[0m")
                print(" An expression is a combination of values, variable, and operators")
                print(" that evaluates to a result.")

                print("\n\033[1m " + "                 EXAMPLE: ADD TWO NUMBERS""\033[0m")
                print("\n\033[1m " + "   🔴🟡🟢           Python code""\033[0m""\033[1m " + "                                        Output""\033[0m")
                print("        a = 10                          # first number")
                print("        b = 5                           # Second number""                10 + 5 = 15")
                print("        result =  a + B                 # Add the number""                    ↓ ")
                print("        print('The result is:,result')  # Display the result         The result is: 15")

                print("\n Python follows the order of operations""\033[1m " + "(PEMDAS):""\033[0m")
                print("\033[1m " + "PEMDAS (Order of operations)""\033[0m")
                print("______________________________________")
                print("| P Parentheses              | First |")
                print("| E Exponent                 |   │   |")
                print("| M Multiplication           |   │   |")
                print("| D Division                 |   │   |")
                print("| A Addition                 |   ↓   |")
                print("| S Subtraction              | Last  |")
                print("______________________________________")

                while True:
                    back = input("\n Select [X] to return to the prelim list: ").upper()
                    if back == "X":
                        print("\n" * 2)
                        break
                    else:
                        print(" Invalid input. Please enter 'X' to return.")

            elif prelim_choice == "8":
                print("=" * 100)
                print("\033[1m " + "                                          BASIC INPUT AND OUTPUT""\033[0m")
                print("=" * 100)

                print("\n\033[1m " + "ACCEPTING USER INPUT""\033[0m")
                print(" Purpose of input in programming")
                print(" Real-life analogies (e.g., asking for a user's name and responding)")

                print("\n\033[1m " + "Example:""\033[0m")
                print("\033[1m " + "PYTHON INPUT - GETTING USER INPUT""\033[0m")
                print("\033[1m " + "name = input ('Enter your name:')""\033[0m")
                print("\033[1m " + "name = input ('Enter you age:')""\033[0m")
                print("\n• Using""\033[1m " + "input () function""\033[0m")
                print("• Syntax :""\033[1m " + "variable = input('Prompt message:')""\033[0m")
                print("• All input is""\033[1m " + "string""\033[0m"" type by""\033[1m " + "default""\033[0m")

                print("\n\033[1m " + "FORMATTING OUTPUT""\033[0m")
                print(" Using comma , in ""\033[1m " + "print()""\033[0m")

                print("\n\033[1m " + "GETTING USER INPUT AND DISPLAYING OUTPUT""\033[0m")
                print("\n name = input ('Enter your name:')")
                print(" age = input ('Enter your age:')")
                print(" print('Name: ', name)")
                print(" print('Age: ', age)")

                print("\n\033[1m " + "CONVERTING INPUT TO OTHER DATA TYPES""\033[0m")

                print("\033[1m " + "B. Float Input (for decimal numbers)""\033[0m")
                print("\n\033[1m " + "PYTHON CODE""\033[0m")
                print(" grade = float(input('Enter your grade:')")
                print(" print(f'Your grade is {grade}')")

                print("\n\033[1m " + "C. Boolean Input (True or False using conditions)""\033[0m")
                print("\n\033[1m " + "PYTHON CODE""\033[0m")
                print(" answer = input('Are you student? (yes/no):')")
                print(" is_student = answer.lower() === 'yes'")
                print(" print('Student status:', is_student)")

                print("\n\033[1m " + "Example Program (Combining All)""\033[0m")
                print("\n name = input ('Enter your name:')")
                print(" age = int(input('Enter your age:')")
                print(" grade = float(input('Enter your final grade:')")
                print(" print(f'Student: {name}, Age: {age}, Final Grade: {grade}')")

                while True:
                    back = input("\n Select [X] to return to the prelim list: ").upper()
                    if back == "X":
                        print("\n" * 2)
                        break
                    else:
                        print(" Invalid input. Please enter 'X' to return.")

            elif prelim_choice == "X":
                break

            else:
                print("\nInvalid choice! Please select 0, 1, 2, 3, 4, 5, 6, 7, 8, or X.\n")

    elif choice == "2":
              while True:
                  print("=" * 40)
                  print("\033[1m " + "         MIDTERM LESSON LIST""\033[0m")
                  print("=" * 40)

                  print("\n [1] CONDITIONAL STATEMENTS IN PYTHON")
                  print(" [2] LOGICAL OPERATOR")
                  print(" [X] BACK TO MAIN MENU")

                  midterm_choice = input("\n Enter your sub-lesson: ").upper()
                  print("\n" * 2)

                  if midterm_choice == "1":
                      while True:
                          print("=" * 40)
                          print("\033[1m " + "CONDITIONAL STATEMENTS CHAPTER LESSON""\033[0m")
                          print("=" * 40)

                          print("\n [0] INTRODUCTION TO CONDITIONAL STATEMENTS")
                          print(" [1] RELATIONAL OPERATORS")
                          print(" [2] IF STATEMENT")
                          print(" [3] IF-ELSE STATEMENT")
                          print(" [4] IF-ELIF-ELSE STATEMENT" )
                          print(" [5] NESTED CONDITION" )
                          print(" [X] BACK TO MIDTERM LESSON LIST " )

                          chap_choice = input("\n Enter your chapter-lesson: ").upper()
                          print("\n" * 2)

                          if chap_choice == "0":
                              print("=" * 100)
                              print("\033[1m " + "                                    Introduction to Conditional Statements""\033[0m")
                              print("=" * 100)
                              print("\n\033[1m " + "A condition statement""\033[0m"" allows a program to make decision")
                              print(" based on whether a condition ""\033[1m " + "True or False.""\033[0m")
                              print("\n Basic Structure""                                     How it works""                          Example")
                              print("  if condition""                                          Start""                              🔴🟡🟢")
                              print("    ∟  statement""                                          |""                                age = 18")
                              print( "                                                          ↓ ""                               if age >= 18:")
                              print("\033[1m " + "if""\033[0m"" The if keyword start the""                      Is the Condition""                         print('You are an adult')")
                              print(" conditional statement.""                                 True?   _____________")
                              print("                                                          |""                  |""             Output when run")
                              print("\033[1m " + "condition""\033[0m"" The condition is evaluated If it ""              |""                  ↓""\033[1m " + "            Your are an adult.""\033[0m")
                              print(" is True, the indented statement is executed.""             ↓""              Skip the")
                              print( "                                                     Execute the ""        statement")
                              print( "\033[1m " + "statement""\033[0m"" The statement is the code that""             statement""              |")
                              print(" runs when the condition is True.""                         |""                  |")
                              print("                                                          |""                  |")
                              print("                                                          |""__________________|")
                              print("                                                          ↓")
                              print("                                                         End")

                              while True:
                                  back1 = input("\n Select [X] to return to the midterm chapter list: ").upper()
                                  if back1 == "X":
                                      print("\n" * 2)
                                      break
                                  else:
                                      print(" Invalid input. Please enter 'X' to return.")

                          elif chap_choice == "1":
                              print("=" * 100)
                              print("\033[1m " + "                                          RELATIONAL OPERATORS ""\033[0m")
                              print("=" * 100)
                              print("\n Relational operators,also called \033[1m " + "comparison operators,""\033[0m"" are used")
                              print(" to compare two values. The result is always either""\033[1m " + "True or False.""\033[0m")

                              print("\n\033[1m " + "Operator""\033[0m""\033[1m " + "          Meaning""\033[0m""\033[1m " + "                      Example""\033[0m""\033[1m " + "     Result""\033[0m")
                              print(" ==""                 Equal to""                      10 == 10""       True")
                              print(" !=""                 Not equal to""                  10 != 5""        True")
                              print(" >""                  Greater than""                  10 > 5""         True")
                              print(" <""                  Less than""                     5 < 10""         True")
                              print(" >=""                 Greater than or equal to""      10 >= 10""       True")
                              print(" <=""                 Less than or equal to""         5 <= 10""        True")

                              print("\n\033[1m " + "💡 Remember:""\033[0m")
                              print(" Relational operators compare values and always return either ""\033[1m " + "True or False.""\033[0m\n")

                              while True:
                                  back1 = input("\n Select [X] to return to the midterm chapter list: ").upper()
                                  if back1 == "X":
                                      print("\n" * 2)
                                      break
                                  else:
                                      print(" Invalid input. Please enter 'X' to return.")

                          elif chap_choice == "2":
                              print("=" * 100)
                              print("\033[1m " + "                                          THE IF STATEMENT ""\033[0m")
                              print("=" * 100)
                              print("\n The\033[1m " + "if""\033[0m"" statement executes a block of code only")
                              print(" when condition is""\033[1m " + "True.""\033[0m")

                              print("\n Syntax""                                              How it works""                          Example")
                              print("  if condition""                                          Start""                              🔴🟡🟢")
                              print("    ∟  statement (s)""                                      |""                                age = 20")
                              print("                                                          ↓ ""                               if age >= 20:")
                              print("\033[1m " + "if""\033[0m"" The if keyword start the""                      Is the Condition""                         print('You are an adult')")
                              print(" statement.""                                             True?   _____________")
                              print("                                                          |""                  |""            \033[1m " + "What happens?""\033[0m")
                              print("\033[1m " + "condition""\033[0m"" The condition is evaluated If it ""              |""                  ↓""             • if age is 18 or more (True)")
                              print(" is True, the indented block is executed.""                 ↓""              Skip the""          the message is printed.")
                              print("                                                     Execute the ""          block""           • if age is less than 18 (False)")
                              print("\033[1m " + "statement""\033[0m"" One or more statement that""               indented block""           |""             nothing happens.")
                              print(" runs when the condition is True.""                         |""                  |")
                              print("                                                          |""                  |")
                              print("                                                          |""__________________|")
                              print("                                                          ↓")
                              print("                                                         End")
                              print("\n 💡 If the condition is\033[1m " + "False,""\033[0m")
                              print(" the indented block is skipped.\n")

                              while True:
                                  back1 = input("\n Select [X] to return to the midterm chapter list: ").upper()
                                  if back1 == "X":
                                      print("\n" * 2)
                                      break
                                  else:
                                      print(" Invalid input. Please enter 'X' to return.")

                          elif chap_choice == "3":
                              print("=" * 100)
                              print("\033[1m " + "                                          THE IF-ELSE STATEMENT ""\033[0m")
                              print("=" * 100)
                              print("\n The\033[1m " + "else""\033[0m"" statement provides an alternative")
                              print(" when the""\033[1m " + "if""\033[0m"" condition is""\033[1m " + "false.""\033[0m")

                              print("\n Syntax""                                              Example")
                              print(" if condition""                                        🔴🟡🟢")
                              print("    ∟  statement ""                                    score = 65")
                              print(" else:""                                               if score >= 75:")
                              print("    ∟  statement ""                                       print('Passed')")
                              print("                                                     else:")
                              print("                                                        print(''Failed)")

                              print("\n\033[1m " + "💡 Key Points:""\033[0m")
                              print(" • Use""\033[1m " + "else""\033[0m"" when you want an alternative action""\033[1m " + "     Explanation: ""\033[0m")
                              print("   if the""\033[1m " + "if""\033[0m"" condition is""\033[1m " + "False. ""\033[0m""                    In the example, score is 65, which is lesss than 75,")
                              print(" • Only one of the ""\033[1m " + "if  ""\033[0m""or""\033[1m " + "else ""\033[0m""block""                so the""\033[1m " + "else ""\033[0m""block runs an the program prints""\033[1m " + "Failed. ""\033[0m")
                              print("   will be executed.\n")

                              while True:
                                  back1 = input("\n Select [X] to return to the midterm chapter list: ").upper()
                                  if back1 == "X":
                                      print("\n" * 2)
                                      break
                                  else:
                                      print(" Invalid input. Please enter 'X' to return.")

                          elif chap_choice == "4":
                              print("=" * 100)
                              print("\033[1m " + "                                          THE IF-ELIF-ELSE STATEMENT  ""\033[0m")
                              print("=" * 100)
                              print("\n The""\033[1m " + "elif""\033[0m"" statement is used when there are multiple")
                              print(" condition to evaluate. Python checks each condition")
                              print(" from top to bottom and executes the first condition")
                              print(" that is\033[1m " + "True.""\033[0m")

                              print("\n Syntax""                                   Example""                          Explanation")
                              print(" if condition1:""                          score = 85""                        • score is 85 ")
                              print("  ∟  statement ""                          if score >= 90:""                   • 85 >= 90 → False")
                              print(" elif condition2""                            print('Excellent')""             • 85 >= 80 → True ✔")
                              print("  ∟  statement""                           elif score >= 80:""                 • Therefore, print('Very Good')")
                              print("  |""                                         print('Very Good')""               is executed.")
                              print(" else:" "                                  elif score >= 75:""                  • The remaining elif and else")
                              print("  ∟  statement ""                             print('Passed')""                  blocks are skipped.")

                              print("\n\033[1m " + "⭐ Key Points:""\033[0m")
                              print(" • Python checks condition from top to bottom")
                              print(" • If a condition is true, its block is executed")
                              print("   and the rest are skipped.")
                              print(" • If none of the condition are True,")
                              print("   the else block is executed.")

                              while True:
                                  back1 = input("\n Select [X] to return to the midterm chapter list: ").upper()
                                  if back1 == "X":
                                      print("\n" * 2)
                                      break
                                  else:
                                      print(" Invalid input. Please enter 'X' to return.")

                          elif chap_choice == "5":
                              print("=" * 100)
                              print("\033[1m " + "                                          NESTED CONDITION  ""\033[0m")
                              print("=" * 100)

                              print("\n A nested condition is a condition inside another condition.")
                              print("\n\033[1m " + "SYNTAX""\033[0m")
                              print(" if condition1:""                     ←------- First condition")
                              print("      if condition2:" "                          is checked.")
                              print("            # block of code""                  Second condition")
                              print("      else:                         -------⟶  is checked only if")
                              print("            # block of code""                   the first condition")
                              print("                                              is True.")
                              print(" else:")
                              print("            # block of code""         ←------- This runs if the")
                              print("                                              first condition is False")

                              print("\n\033[1m " + "CODE""\033[0m")
                              print(" gender = input('Enter gender (M/F):')")
                              print(" age = int(input('Enter age:'))")
                              print("\n if gender == 'M':")
                              print("     if age >= 21:")
                              print("         print('You are a MALE DEBUTANT')")
                              print("     else:")
                              print("         print('You are a male, but not a debutant yet.')")
                              print(" else:")
                              print("     if age <= 18:")
                              print("         print('You are a FEMALE DEBUTANT')")
                              print("     else:")
                              print("         print('You are a female, but not a debutant yet.')")

                              while True:
                                  back1 = input("\n Select [X] to return to the midterm chapter list: ").upper()
                                  if back1 == "X":
                                      print("\n" * 2)
                                      break
                                  else:
                                      print(" Invalid input. Please enter 'X' to return.")

                          elif chap_choice == "X":
                              break

                  elif midterm_choice == "2":

                      while True:
                          print("=" * 40)
                          print("\033[1m " + "          LOGICAL OPERATOR""\033[0m")
                          print("=" * 40)

                          print("\n [0] INTRODUCTION TO LOGICAL OPERATOR")
                          print(" [1] THE AND OPERATOR")
                          print(" [2] THE OR OPERATOR")
                          print(" [3] THE NOT OPERATOR")
                          print(" [X] BACK TO MIDTERM LESSON " )


                          chap2_choice = input("\n Enter your chapter-lesson: ").upper()
                          print("\n" * 2)

                          if chap2_choice == "0":
                              print("=" * 100)
                              print("\033[1m " + "                                          LOGICAL OPERATOR  ""\033[0m")
                              print("=" * 100)

                              print("\n\033[1m " + "Logical operators are used to combine or reverse condition in a Python program.""\033[0m")
                              print(" They are commonly used with if, elif, and else.\n")

                              print("\033[1m " + "Python has three logical operators:""\033[0m""\033[1m " + "                           Example:""\033[0m")
                              print("\033[1m " + "    Operator""\033[0m""\033[1m " + "               Meaning""\033[0m""                            🔴🟡🟢")
                              print("       and""            Both condition must be True""               age = 20")
                              print("       or""             At least one condition must be True""       if age >= 18 and age <= 60:")
                              print("       not""            Reverses the result""                       print('Allowed')\n")

                              while True:
                                  back1 = input("\n Select [X] to return to the midterm chapter list: ").upper()
                                  if back1 == "X":
                                      print("\n" * 2)
                                      break
                                  else:
                                      print(" Invalid input. Please enter 'X' to return.")

                          elif chap2_choice == "1":
                              print("=" * 100)
                              print("                                          The\033[1m " + "AND ""\033[0m""Operator")
                              print("=" * 100)
                              print("\n The and operator returns True only when ALL conditions are True.")

                              print("\n\033[1m " + "  Example:""\033[0m""\033[1m " + "                                💡  Explanation:""\033[0m")
                              print(" age = 20""                                   The program checks:")
                              print(" has_id = True""                              age >= 18 ⟶ True")
                              print(" if age >= 18 and has_id:""                   has_id    ⟶ True")
                              print(" print('You are allowed to enter.')")
                              print(" else:""                                      since\033[1m " + "both are True:""\033[0m")
                              print(" print('You are not allowed to enter.')""\033[1m " + "    True and True = True""\033[0m")

                              print("\n\033[1m " + "               Truth Table - AND""\033[0m")
                              print("=" * 47)
                              print("│  Condition A  │  Condition B  │   A and B   |")
                              print("=" * 47)
                              print("│     True      │     True      │    True     │")
                              print("│     True      │     False     │    False    │")
                              print("│     False     │     True      │    False    │")
                              print("│     False     │     False     │    False    │")
                              print("‾" * 47)

                              print("\n\033[1m " + "💡 Easy way to remember:""\033[0m")
                              print(" AND = KAILANGAN LAHAT TRUE\n")

                              while True:
                                  back1 = input("\n Select [X] to return to the midterm chapter list: ").upper()
                                  if back1 == "X":
                                      print("\n" * 2)
                                      break
                                  else:
                                      print("Invalid input. Please enter 'X' to return.")

                          elif chap2_choice == "2":

                              print("=" * 100)
                              print("                                          The\033[1m " + "OR ""\033[0m""Operator")
                              print("=" * 100)
                              print("\n The or operator returns True when at least ONE condition is True.")

                              print(
                                  "\n\033[1m " + "Example Code""\033[0m""\033[1m " + "                                  💡 The program checks:""\033[0m")
                              print(" day = 'Saturday'""                               day == 'Saturday' ⟶ True")
                              print(" if day == 'Saturday' or day == 'Sunday':""       day == 'Sunday' ⟶ False")
                              print("     print('It's the weekend!')""\033[1m " + "                Therefore:""\033[0m")
                              print(" else:""                                           True or False = False")
                              print("     print('It's a regular school day.')""\033[1m " + "       Output:""\033[0m")
                              print("                                                 it's the weekend!")

                              print("\n\033[1m " + "               Truth Table - OR""\033[0m")
                              print("=" * 47)
                              print("│  Condition A  │  Condition B  │   A and B   |")
                              print("=" * 47)
                              print("│     True      │     True      │    True     │")
                              print("│     True      │     False     │    True     │")
                              print("│     False     │     True      │    True     │")
                              print("│     False     │     False     │    False    │")
                              print("‾" * 47)

                              while True:
                                  back1 = input("\n Select [X] to return to the midterm chapter list: ").upper()
                                  if back1 == "X":
                                      print("\n" * 2)
                                      break
                                  else:
                                      print(" Invalid input. Please enter 'X' to return.")

                          elif chap2_choice == "3":

                              print("\n\033[1m " + "💡 Easy way to remember:""\033[0m")
                              print(" OR = KAILANGAN ISA LANG TRUE\n")

                              print("=" * 100)
                              print("                                          The\033[1m " + "NOT ""\033[0m""Operator")
                              print("=" * 100)
                              print("\n The not operator reverse the result of a condition.")
                              print("\033[1m " + "                  True ⟶ False""\033[0m")
                              print("\033[1m " + "                  False ⟶ True""\033[0m")

                              print(
                                  "\n\033[1m " + "Example:""\033[0m""\033[1m " + "                                  Explanation:""\033[0m")
                              print(" is_raining = False""                         is_raining = False")
                              print(" if not is_raining:""                         not is_raining")
                              print("     print('You can go outside.')""           not False = True")
                              print(
                                  " else:""\033[1m " + "                                     Output:""\033[0m"" You can go outside.")
                              print("     print('Bring an umbrella.')")

                              print("\n\033[1m " + "          Truth Table - OR""\033[0m")
                              print("=" * 38)
                              print("│  Condition A  │  not  Condition B  │")
                              print("=" * 38)
                              print("│     True      │        False       │")
                              print("│     False     │        True        │")
                              print("‾" * 38)

                              print("\n\033[1m " + "💡 Easy way to remember:""\033[0m")
                              print(" NOT = BALIKTARIN ANG RESULT\n")

                              while True:
                                  back1 = input("\n Select [X] to return to the midterm chapter list: ").upper()
                                  if back1 == "X":
                                      print("\n" * 2)
                                      break
                                  else:
                                      print(" Invalid input. Please enter 'X' to return.")

                          elif chap2_choice == "X":
                           break

                          else:
                              print("\n Invalid choice! Please select 0, 1, 2, 3, or X.\n")

                  elif midterm_choice == "X":
                      break

                  else:
                      print("\n Invalid choice! Please select 0, 1, 2, 3, or X.\n")


    elif choice == "3":

        while True:
            print("=" * 40)
            print("\033[1m " + "          FINAL LESSON LIST""\033[0m")
            print("=" * 40)

            print("\n [0] INTRODUCTION TO ITERATION AND LOOPS")
            print(" [1] PYTHON FOR LOOP")
            print(" [2] PYTHON WHILE LOOP")
            print(" [X] BACK TO MAIN MENU")

            final_choice = input("\n Enter your sub-lesson: ").upper()
            print("\n" * 2)

            if final_choice == "0":
                print("=" * 100)
                print("                       \033[1m " + "INTRODUCTION TO ITERATION AND LOOPS""\033[0m")
                print("=" * 100)

                print("                        Iteration means repeating a process.")
                print("      In programming, it means repeatedly executing  a set of instructions.")
                print("                       Each repetition is called in iteration.")

                print("\n 🔴🟡🟢""                                              1")
                print(" for number in range(3):""                              Welcome to Python")
                print("    print('Welcome to Python')""      -------⟶         2")
                print("                                                      Welcome to Python")
                print("                                                     3")
                print("                                                      Welcome to Python")
                print("\n The print() instruction executes once during each iteration\n")

                print(" Iteration allows a program to perform the same task multiple times.")
                print(" Without a loop, instructions must be written repeatedly\n")

                print("=" * 55)
                print("\033[1m" + "│     Without a loop:      │""\033[0m""\033[1m " + "     Using a loop:      │""\033[0m")
                print("=" * 55)
                print("│  print('Study Python')   │""  for number in range(4):│")
                print("│  print('Study Python')   │ " "    print(Study Python) │")
                print("│  print('Study Python')   │ " "                        │")
                print("‾" * 55)
                print("\n\033[1m " + "Both programs produce the same output, but the loop makes the""\033[0m")
                print("\033[1m " + "program shorter and easier to modify. To repeat the message 100 times,""\033[0m")
                print("\033[1m " + "change 4 to 100.""\033[0m\n")

                print("=" * 100)
                print("                       \033[1m " + "             Types of loops in Python""\033[0m")
                print("=" * 100)

                print("\n Python has two main types of loops:for and while.")
                print(
                    "\n\033[1m " + "                   For Loop""\033[0m""\033[1m " + "                                                 While Loop""\033[0m")
                print(
                    "\n Repeats instruction for ech item in a sequence.""             Repeats instructions while a condition is true")
                print(
                    " Useful when the number of repetitions is known.""             Useful when repetition depends on a condition.")
                print("\n          for number in range(3):""                                          count = 1")
                print("                print('Hello!')""                                            while count <= 3: ")
                print("                                                                               print('Hello!')")
                print("       1                2                3""                                     count += 1")
                print("     Hello!    ---⟶   Hello!    ---⟶  Hello!")
                print(
                    "                                                                        Check condition ---⟶ Repeat")
                print(
                    "\n                                    \033[1m " + "Both example print Hello! three times.""\033[0m")

                while True:
                    back1 = input("\n Select [X] to return to the main list: ").upper()
                    if back1 == "X":
                        print("\n" * 2)
                        break
                    else:
                        print(" Invalid input. Please enter 'X' to return.")


            elif final_choice == "1":
                print("=" * 100)
                print("                                            \033[1m " + "PYTHON FOR LOOPS""\033[0m")
                print("=" * 100)

                print("\n A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).")
                print(" This is less like the for keyword in other programming languages, and works more like an iterator ")
                print(" method as found in other object-orientated programming languages.")
                print("\n With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.")

                print("\n\033[1m " + "       Syntax""\033[0m""\033[1m " + "                                      Example Code""\033[0m")
                print("   for variable in sequence:""                   for number in range(4):")
                print("   statement(s)""                                    print('Study Python')")
                print("\n variable: receives each item")
                print(" sequence: items to loop through"" This loop prints Study Python four times.")
                print(" Indented statements: the loop body")
                print("\n\033[1m " + "Use a colon (:) after the loop header and indent the loop body.""\033[0m")

                print("\n\033[1m " + "for loop: Print Numbers 1 to 5""\033[0m\n")
                print("=" * 50)
                print("│  Example Code""                         Output   │")
                print("=" * 50)
                print("│  for number in range(1, 6):""           1        │")
                print("│      print(number)""                    2        │")
                print("│                                       3        │")
                print("│                                       4        │")
                print("│                                       5        │")
                print("‾" * 50)

                print("\n\033[1m " + "How It Works ""\033[0m")
                print(" 1. range(1, 6) produce 1, 2, 3, 4, and 5. ")
                print(" 2. The start value 1 is included; the stop value 6 is excluded.")
                print(" 3. Each iteration assigns the next value to number.")
                print(" 4. print(number) displays that value. After 5, the loop ends.\n")
                print("                 1 -⟶ 2 -⟶ 3 -⟶ 4 -⟶ 5")
                print("                 |___________________|")
                print("                     5 iterations")

                while True:
                    back1 = input("\n Select [X] to return to the final lesson list: ").upper()
                    if back1 == "X":
                        print("\n" * 2)
                        break
                    else:
                        print(" Invalid input. Please enter 'X' to return.")


            elif final_choice == "2":

                print("=" * 100)
                print("                                            \033[1m " + "PYTHON WHILE LOOP""\033[0m")
                print("=" * 100)

                print("\nWith the while loop we can execute a set of statements as long as a condition is true.")

                print("\n\033[1m " + "       Syntax""\033[0m""\033[1m " + "                                      Example Code""\033[0m")
                print("   while condition:""                                count = 1")
                print("   statement(s)""                                    while count <= 5:")
                print("                                                        print(count)")
                print(" condition: checked before each iteration""               count += 1")
                print(" Indented statements: run while the")
                print(" condition is True.""                               This loop prints the numbers 1 to 5.")
                print("\n\033[1m " + "count += 1 increase count by 1 each iteration.""\033[0m")
                print("\033[1m " + "When count becomes 6, the condition is false and the loops stops.""\033[0m")

                print("\n\033[1m " + "Counting Downward with a while loop: 5 to 1" + "\033[0m")
                print("=" * 50)
                print("│  Example Code""                         Output   │")
                print("=" * 50)
                print("│  number = 5""                           5        │")
                print("│  while number >= 1:""                   4        │")
                print("│      print(number)""                    3        │")
                print("│      number -= 1                      2        │")
                print("│                                       1        │")
                print("‾" * 50)

                print("\n\033[1m " + "How It Works ""\033[0m")
                print(" 1. Start with number = 5.")
                print(" 2. Repeat while number >= 1.")
                print(" 3. Print number, then decrease it by 1 using number -= 1.")
                print(" 4. Stop when number becomes 0 and the condition is False.\n")
                print("                 5 -⟶ 4 -⟶ 3 -⟶ 2 -⟶ 1")
                print("                 |___________________|")
                print("                     5 iterations")

                while True:
                    back1 = input("\n Select [X] to return to the final lesson list: ").upper()
                    if back1 == "X":
                        print("\n" * 2)
                        break
                    else:
                        print(" Invalid input. Please enter 'X' to return.")


            elif final_choice == "X":
                break

            else:
                print("\n Invalid choice! Please select 0, 1, 2, or X.\n")


    elif choice == "E":
        print("\n Exiting the Python Tutorial . Goodbye!")
        break
    else:
        print("\n Invalid choice! Please select 0, 1, 2, 3, or X.\n")
