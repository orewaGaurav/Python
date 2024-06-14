class Distance:
    def __init__(self,km=0,m=0):
        self.km=km + m//1000
        self.m=m%1000

    def __add__(self,other):
        total_km = self.km + other.km
        total_m = self.m + other.m

        if total_m >= 1000:
            total_km += total_m//1000
            total_m %= total_m%1000

        return Distance(total_km,total_m)
    def __repr__(self):
        return f"Total distance: {self.km} km and {self.m} m"

distance1 = Distance(3,500)
distance2 = Distance(2,800)
distance3 = distance1+distance2
print(distance3)

#total_distance = distance1.add_distances(distance2)
#print("Total distances:",total_distance.km,"km",total_distance)

        
