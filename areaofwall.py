wall_height=float(input("enter the wall height:"))
wall_width=float(input("enter the wall width:"))
area_of_wall=float(wall_height*wall_width)
number_of_cans=round(area_of_wall/5)
def wall_painting(wall_heigth,wall_width,number_of_cans):
     print(f"you need {number_of_cans} cans to paint the wall")
wall_painting(wall_height,wall_width,number_of_cans)
    
