# I declare that my_project contains no examples of misconduct, such as plagiarism, or collusion.
# All the websites of python contents and key codes that i have refered is included within my code solution.
# https://learnpython.com/blog/python-if-in-one-line/#:~:text=Conditional%20expressions%20in%20Python%20(also,block%20in%20a%20single%20line. -checked if i can write one line if statments
# https://matplotlib.org/2.1.1/gallery/color/named_colors.html - colors for Histogram
# https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/-Took a base idea how the histogram need to be programmed
# https://www.w3schools.com/python/python_file_handling.asp- Took an idea how the text file handling is done and more deep researched about them
# https://stackoverflow.com/questions/20309456/how-do-i-call-a-function-from-another-py-file - how python import files from one to another file
# Date-30/11/2023
from graphics import *    #import the graphics.py module
from w2053501_part3 import save_data,read_data        # import the textdef.py which i has user define functions of 'save_data' and 'read_data'
progress_count,Trailer_count,exclude_count,modile_retriever_count=0,0,0,0   # single line variable assigning ( for each variable, the values are assigned in the order i have wriiten separated by',' ex;progress_count=0
data=[]   #A null list which i created to append these values (pass_marks,defer_marks,fail_marks) and the return of output()
'''This is a user define function which is to check the user inputs belongs to the following catoregies(progress,progress(module trailer,exclude,do not progress(module retriver)'''                                                                                      
def output(pass_marks,defer_marks,fail_marks):                                                                                                                       
    total_marks=pass_marks+defer_marks+fail_marks  #Adding the user input values to a variable name:total                                                            
    if total_marks != 120:  # validating whether the user input values add up to (120)!!!                                                                            
            return("total incorrect")                                                                                                                                      
    else:                                                                                                                                                            
         if pass_marks ==120: # condition to check whether the user input meet the following requierments                                                            
               return("progress")                                                                                                                                                                                                                                                                                                         #
         elif pass_marks ==100: # condition to check whether the user input meet the following requierments                                                          
                  return("progress(module trailer)")                                                                                                                 
         elif fail_marks==120 or fail_marks== 100 or fail_marks== 80: # condition to check whether the user input meet the following requierments                    
                  return("exclude")                                                                                                                                  
         else:                                                                                                                                                       
                   return("do not progress(module retriever)")                                                                                                         
def Histogram(): #                                           <====Histogram====> 
    # OPEN THE WINDOW
    win = GraphWin("<=HISTOGRAM=>", 600, 600)  # open a window object called "win" with size and title
    win.setBackground("mintcream")  # Setting the background color of the window
    my_heading = Text(Point(200, 30), 'Histogram Results')  # Heading of my Histogram
    my_heading.draw(win)
    my_heading.setTextColor("deepskyblue4")
    my_heading.setSize(24)
    my_heading.setStyle("bold")
    my_heading.setFace("helvetica")
    # The base line of the histogram
    xLine = Line(Point(50, 500), Point(550, 500))  # points of the 'x' axis
    xLine.setWidth(2)
    xLine.move(0, 30)
    xLine.draw(win)
    #A list created to draw the histogram by calling the list items by the help of for loop
    Data = [("Progress", "lightgreen", progress_count),("Trailer", "darkseagreen", Trailer_count),("Retriever", "yellowgreen", modile_retriever_count),("Exclude", "rosybrown", exclude_count)]
    fixed_point, max_height, bar_space, space, Base, number_count_point = 45, 450, 10, 100, 529, 520 # single line variable assigning (for each variable, the values are assigned in the order i have wriiten separated by',' ex; fixed_point -45, max_height-450........)
    max_count = max(progress_count, Trailer_count, modile_retriever_count, exclude_count)
    for i, (bar_name, color, count) in enumerate(Data):
        Starting_Point = 80 + i * (space + bar_space)
        Ending_Point = Starting_Point + space       
        height = height = (count / max_count) * 450
        # The bars of the histogram          
        aRectangle = Rectangle(Point(Starting_Point, Base), Point(Ending_Point, Base - height))
        aRectangle.setFill(color)
        aRectangle.draw(win)
        # Number of counts which appear on the top of each bar 
        atext = Text(Point(Starting_Point + space / 2, number_count_point - height), count)
        atext.setStyle("bold")
        atext.setTextColor("deepskyblue4")
        atext.setFace("helvetica")
        atext.draw(win)
        #The name of the bar'''
        atext1 = Text(Point(Starting_Point + space / 2, 550), bar_name)
        atext1.setTextColor("deepskyblue4")
        atext1.setFace("helvetica")
        atext1.setStyle("bold")
        atext1.draw(win)
    # Display the total number of counts in the histogram'''
    total_count = (progress_count+Trailer_count+modile_retriever_count+exclude_count)
    text1 = Text(Point(150, 580), total_count)
    text2 = Text(Point(260, 580), "outcomes in total")
    for text in [text1, text2]:
        text.setTextColor("deepskyblue4")
        text.setSize(15)
        text.setStyle("bold")
        text.draw(win)
#                           ---------------------------End of user define functions--------------------------
print('--------welcome to progression predictor--------')
print('Authorized program users  \n Student-[S] \n Staff-[T]')
while True:
    user_type=str(input('select user type: ')).upper()
    if user_type in ('S','T'):
        break
    else:
        print('Acsses dinied!! please use an Authorized user type to continue') 
        continue 
'''Main code section which i ask for three marks from the user and then to validate (for out of range),using a user difine function i have validate if total=120,and the outcome conditions'''
while True:
     try:#A try except to stop program crashing into a error if the user enter a string instade of a integer
         pass_marks=int(input("\nenter pass_marks: "))# geting the user input  
         if pass_marks not in (0,20,40,60,80,100,120):#condition checking for pass marks whether its out of range or not
             print("out of range!")
             continue #if pass marks is out of range the it will restart within its loop   
         else:
              while True:
                     try:
                         defer_marks=int(input("enter defer_marks: "))# geting the user input
                         if defer_marks not in (0,20,40,60,80,100,120):#condition checking for defer marks whether its out of range or not
                                  print("out of range!")
                                  continue #if pass marks is out of range the it will restart within its loop 
                         else:
                              break
                     except ValueError: # exception for value error 
                                 print("integer is required")       
              while True:
                     try:
                          fail_marks=int(input("enter fail_marks: "))# geting the user input
                          if fail_marks not in (0,20,40,60,80,100,120):#condition checking for fail marks whether its out of range or not
                               print("out of range!")
                               continue #if pass marks is out of range the it will restart within its loop 
                          else:
                              break
                     except ValueError: # exception for value error 
                                 print("integer is required")       
              output(pass_marks,defer_marks,fail_marks)  #calling user define output function 
              value= output(pass_marks,defer_marks,fail_marks)
              print(value)# printing the returned value of output
              if value =='total incorrect':# The loop will restart if total is !=120..
                  continue
              elif value =='progress':# condition to get count which is used to represent in the histogram graph
                progress_count+=1
              elif value =='progress(module trailer)' :# condition to get count which is used to represent in the histogram graph
                    Trailer_count+=1
              elif value =='exclude':# condition to get count which is used to represent in the histogram graph
                    exclude_count+=1
              else: 
                    modile_retriever_count+=1
              data.append([pass_marks,defer_marks,fail_marks,value]) # adding the following values into a list "data" 
              save_data(data,filename='CWTEXTFILE.txt')# user define function created to write the following data into a text file
              if user_type != 'T': # user type checking before entering into multiple input loop                     
                      break
              while True:# loop to check wether user enters the correct option to continue with the program
                new_input=str(input("\n whould you like to continue entering more sets of marks? \n Enter [y] to continue , Enter [q] to quit: ")).lower()
                if new_input  in('y','q'):# new_input should be 'y' or 'q' 
                    break
                else: #else it will continue loop
                    print("please double check the option!!! Invalid user decision")
                    continue                                
              if new_input != 'y': # if new_input not equal to 'y' the loop will break 
                  Histogram()    #calling user define Histogram function             
                  break
     except ValueError: # exception for value error 
        print("integer is required")
if user_type== 'T': # user type checking before displaying the list and text document
      print('\nPart2:\n--------Lists--------')
      for i in data:
            print(f"{i[3]}-{i[0]},{i[1]},{i[2]}")       
      print('\nPart3:\n ----TEXT DOCUMENT DATA----')
      text_output=read_data(filename='CWTEXTFILE.txt')
      print(text_output)  #printing user define function after assinging it to another variable
        
        

        
            
          


               
 
