"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and OMAR A. FAYOUMI.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow

redTurtle = rg.SimpleTurtle('turtle')
redTurtle.pen = rg.Pen('red', 2)
redTurtle.speed = 30

size = 20

for k in range(20):
    redTurtle.draw_regular_polygon(6,size)
    size = size + 5


cyanTurtle = rg.SimpleTurtle('circle')
cyanTurtle.pen = rg.Pen('cyan', 4)
cyanTurtle.speed = 40

cyanTurtle.backward(40)

sizeCyan = 4

for k in range(20):
    cyanTurtle.draw_regular_polygon(sizeCyan,3 * sizeCyan)
    sizeCyan = sizeCyan + 2


