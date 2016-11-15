#last week of my udacity python class
#this code shows examples of inheritance and method overriding
#the child class inherits instances from the parent class


class Parent ():
    def__init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

        def show_info(self):
            print ("Last Name - "+self.last_name)
            print ("Eye Color- "+self.eye_color)

class Child(Parent):
    def__init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last Name = "+self.last_name)
        print("Eye Color - "+self.eye_color)
        print("Number of toys - "+str(self.number_of_toys)
              
#use string function in number of toys 
              

billy_cyrus = Parent("Cyrus", "blue")
billy_cyrus.show_info()
miley_cyrus = Child("Cyrus", "blue", 5)
miley_cyrus.show_info()
