my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
heightInMeters = 74 / 36.0
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about %r." % my_name)
print("He's %f meters tall" % heightInMeters)
print("He's %d pounds heavy" % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

#This linke is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d" %(my_age, my_height, my_weight, my_age + my_height + my_weight))