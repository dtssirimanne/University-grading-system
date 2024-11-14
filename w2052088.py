# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: w2052088
#IIT ID:20220771
# Date: 12/12/2023






from graphics import *

# Initialize global variables
progress_count = 0
trailer_count = 0
retriever_count = 0
excluded_count = 0
counts_list = []
total_outcomes = 0
data_list = []
outcomes=0

def create_bar_graph(data_list):
    # Create GraphWin object 
    win = GraphWin("Histogram", 700, 600)
    win.setBackground("Mint Cream")

    #  Draw a  line bottom of the graphs
    aLine_bottom = Line(Point(0,390), Point(700 ,390))
    aLine_bottom.setWidth(1)
    aLine_bottom.draw(win)

    # Calculate the number of students in each category
    progress_count = sum(1 for i in data_list if i[0] == "Progress")
    trailer_count = sum(1 for i in data_list if i[0] == "Progress (Module Trailer)")
    retriever_count = sum(1 for i in data_list if i[0] == "Do not progress (Module retriever)")
    excluded_count = sum(1 for i in data_list if i[0] == "Excluded")

    # Draw the histogram bars
    bar_width = 80
    bar_height = 100

    progress_bar = Rectangle(Point(50, 390), Point(50 + bar_width, 390 - (progress_count * bar_height / len(data_list))))
    progress_bar.setFill(color_rgb(152,251,152))#RGB values for colors
    progress_bar.draw(win)
    
    trailer_bar = Rectangle(Point(150, 390), Point(150 + bar_width, 390 - (trailer_count * bar_height / len(data_list))))
    trailer_bar.setFill(color_rgb(103,146,103))#RGB values for colors
    trailer_bar.draw(win)
    
    retriever_bar = Rectangle(Point(250, 390), Point(250 + bar_width, 390 - (retriever_count * bar_height / len(data_list))))
    retriever_bar.setFill(color_rgb(85, 107, 47))#RGB values for colors
    retriever_bar.draw(win)
    
    excluded_bar = Rectangle(Point(350, 390), Point(350 + bar_width, 390 - (excluded_count * bar_height / len(data_list))))
    excluded_bar.setFill(color_rgb(255, 245, 238))#RGB values for colors
    excluded_bar.draw(win)

    # Display the title
    title_text = f"Histogram Results "
    title_label = Text(Point(140,50), title_text)
    title_label.setSize(16)
    title_label.setStyle("bold")
    title_label.draw(win)

    # Display the outcome counts
    outcome_text = f" Progress  "
    outcome_label = Text(Point(85, 400), outcome_text)
    outcome_label.draw(win)

    outcome_text = f" Trailing   "
    outcome_label = Text(Point(185, 400), outcome_text)
    outcome_label.draw(win)

    outcome_text = f" Retriever  "
    outcome_label =Text(Point(295, 400), outcome_text)
    outcome_label.draw(win)

    outcome_text = f" Excluded   "
    outcome_label = Text(Point(390, 400), outcome_text)
    outcome_label.draw(win)

    #Display the total outcomes
    outcome_text = f"{len(data_list)} outcomes in total  "
    outcome_label = Text(Point(140, 490), outcome_text)
    outcome_label.setSize(16)
    outcome_label.draw(win)

    # Create count Label
    count_text = f"{progress_count}"
    count_label = Text(Point(50 + bar_width/2, 390- (progress_count*bar_height/ len(data_list))-10), count_text)  # Adjust the y-coordinate as needed
    count_label.setSize(14)
    count_label.draw(win)

    count_text = f"{trailer_count}"
    count_label = Text(Point(150 + bar_width/2, 390- (trailer_count*bar_height/ len(data_list))-10), count_text)  # Adjust the y-coordinate as needed
    count_label.setSize(14)
    count_label.draw(win)

    count_text = f"{retriever_count}"
    count_label = Text(Point(250 + bar_width/2, 390- (retriever_count*bar_height/ len(data_list))-10), count_text)  # Adjust the y-coordinate as needed
    count_label.setSize(14)
    count_label.draw(win)

    count_text = f"{excluded_count}"
    count_label = Text(Point(350 + bar_width/2, 390- (excluded_count*bar_height / len(data_list))-10), count_text)  # Adjust the y-coordinate as needed
    count_label.setSize(14)
    count_label.draw(win)

    
    
    # Wait for a click before closing the window
    win.getMouse()
    win.close()

def main():
    global progress_count, trailer_count, retriever_count, excluded_count

    while True:
        # initialize variables
        c_pass = 0
        defer = 0
        fail = 0
        test_result = ""
        values = [0, 20, 40, 60, 80, 100, 120]
        data_list_var = []

        # Get credits at pass
        while True:
            try:
                c_pass = int(input("Enter your credits at pass: "))# input validation
                if c_pass in values:
                    break
                else:
                    print("Out of range")
            except ValueError:
                print("Integer required")

        # Get credits at defer
        while True:
            try:
                defer = int(input("Enter your credits at defer: "))
                if defer in values:
                    break
                else:
                    print("Out of range")
            except ValueError:
                print("Integer required")

        # Get credits at fail
        while True:
            try:
                fail = int(input("Enter your credits at fail: "))
                if fail in values:
                    break
                else:
                    print("Out of range")
            except ValueError:
                print("Integer required")

            
        #checking if total is < 120
        total = c_pass + defer + fail#check total of input credits values are 120
        if total > 120:
            print("Total Incorrect")
            main()
        else:
            pass
        
        # Check if progressed
        if fail >= 80:
            print("Excluded")
            excluded_count += 1 # add 1 to excluded_count
            test_result = "Excluded"
        elif c_pass == 100:
            print("Progress (Module Trailer)")
            trailer_count += 1   # add 1 to trailer_count
            test_result = "Progress (Module Trailer)"
        elif c_pass == 120:
            print("Progress")
            progress_count += 1 # add 1 to progress_count
            test_result = "Progress"
        else:
            print("Do not progress - Module retriever")
            retriever_count += 1  # add 1 to retriever_count
            test_result = "Do not progress (Module retriever)"
            

        # Store counts and data in a list
        counts_list = [progress_count, trailer_count, retriever_count, excluded_count]
        total_outcomes = progress_count + trailer_count + retriever_count + excluded_count
        data_list_var = [test_result, c_pass, defer, fail]
        data_list.append(data_list_var)  
        
        #New function listing data
        def listing_data():
            for i in data_list:
                print(f"{i[0]} - {i[1:]}")
            
        # create a function to store data in a file
        def file_listing():
            
            filename = f"w2052088 Part03.txt"
            with open(filename, "w") as file:#open a text file
                for i in data_list:
                    file.write(f"{i[0]} - {i[1:]}\n")

        # Ask if the user wants to enter another set of data
        again = str(input("Would you like to enter another set of data?Enter 'y' for yes, 'q' for quit): "))
        if again.lower() != 'y':
            break

    # Call the function to draw the bar graph
    listing_data()
    file_listing()
    create_bar_graph(data_list)

main()
