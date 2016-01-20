def main():
    # VARS
    ntabs = -1 # Number of tabs to put before next level of tree (to display levels of tree, sideways)
    rfile = True # Whether or not we are still reading the file
    
    # Get the file name
    fname = input("Enter the name of the tree data file (without the extension): ")

    # Open the file
    treefile = open("{0}.treedata".format(fname), "r")

    # Read file character by character
    while rfile:
        c = treefile.read(1)

        # End of file
        if not c:
            # Break loop
            rfile = False

        # Check type of character
        else:
            # Going down to lower level in tree
            if c == "[":
                # Increase number of tabs
                ntabs += 1

                # Not at top level
                if not (ntabs == 0):
                    # Print new line, and an appropriate number of tabs for the next level of the tree to start on
                    print("\n{0}|{1} ".format("\t"*ntabs, "-"*ntabs), end="")

                # At top level, don't print pipe
                else:
                    # Print new line, and an appropriate number of tabs for the next level of the tree to start on
                    print("\n{0}{1} ".format("\t"*ntabs, "-"*ntabs), end="")

            # Going up to higher level in tree
            elif c == "]":
                # Decrease number of tabs
                ntabs -= 1

                # Print new line for upper level of tree to start/continue on
                print()

            # Indicate bar level (I don't want to just use '|')
            elif c == "|":
                print("-bar", end="")

            # BRACKETS FOR TENSE FEATURES
            elif c == "(":
                print("[", end="")

            elif c == ")":
                print("]", end="")

            # Trace
            elif c == "*":
                print("(Trace)", end="")

            # Regular characters
            else:
                # Print the character without a new line (to avoid messing up things on a single level of the tree)
                print(c, end="")

    # Close file
    treefile.close()

main()
