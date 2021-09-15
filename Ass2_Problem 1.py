class circle:
    def __init__(self,radius):
        self.radius=radius
    def Area_circle(self):
        area=float((3.14)*((self.radius)**2))
        print("Area of the circle is: ",area)
    def perimeter_circle(self):
        perimeter=float((6.28)*(self.radius))
        print("Perimeter of the Circle is: ",perimeter)
radius=int(input("Enter the radius of circle: "))
obj=circle(radius)
obj.Area_circle()
obj.perimeter_circle()
        
