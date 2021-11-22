class Anush:
    t= 4.5
    f = False
    def hell():
        print("Hell")
    def hello():
        print("Hello")
print(10+5)
ffff = True
for i in range(5):
    print(i)

def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1);
def calculate_fact(n):
    return fact(n)
def calculate_fact_2(n):
    return calculate_fact(n)
print(calculate_fact_2(7))
list = [1,2,True, "Hello", 4.5]
list2 = [3,3,3,3]

for i in range(2):
    j=0
    while(j<1):
        print(j)
        j=j+1
i=0
def hello():
    t="Hi"
    print("Hello")
hello()
while(i<2):
    j=0
    while(j<2):
        hello()
        j=j+2
    i=i+1

class Anush1:
    def hello():
        print("Hello")

nn=4
if(nn==1):
    print(nn)
elif(nn==2):
    print(nn)
elif(nn==4):
    print(nn)     


class Color:
    
  # constructor method
  def __init__(self):
    # object attributes
    self.name = 'Green'
    self.lg = self.Lightgreen()
    
#   def show(self):
#     print("Name:", self.name)
    
  # create Lightgreen class
  class Lightgreen:
     def __init__(self):
        self.name = 'Light Green'
        self.code = '024avc'
    
    #  def display(self):
    #     print("Name:", self.name)
    #     print("Code:", self.code)
  
# create Color class object
outer = Color()
  
# method calling
# outer.show()
  
# create a Lightgreen 
# inner class object
g = outer.lg
  
# inner class method calling
# g.display()