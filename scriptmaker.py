import math

with open("script", "w") as fd:

    end = ""
    for i in range(0, 72):
        end += "clear\n"
        #Body
        end += "push\n"
        end += "move\n250 250 0\n"
        end += "box\n-60 60 40 120 120 80\n"
        #Head
        end += "push\n"
        end += "move\n0 100 0\n"
        end += "rotate\ny %d\n"%( (i%18 - 9) * 2 )
        end += "box\n-40 40 40 80 80 80\n"
        end += "pop\n"
        #Left Arm
        end += "push\n"
        end += "move\n-60 60 0\n"
        end += "rotate\nz -5\n"
        end += "rotate\ny %d\n"%( (i%18 - 9) * 5 )
        end += "box\n-40 0 20 40 100 40\n"
        
        #Pick
        end += "push\n"
        end += "move\n-20 -80 0\n"
        end += "box\n-3 3 40 6 6 80\n"
        end += "move\n0 0 40\n"
        end += "box\n-3 15 6 6 30 6\n"

        end += "push\n"
        end += "move\n0 15 0\n"
        end += "rotate\ny -30\n"
        end += "box\n-3 30 6 6 30 6\n"
        end += "pop\n"

        end += "push\n"
        end += "move\n0 -15 0\n"
        end += "rotate\nx 30\n"
        end += "box\n-3 0 6 6 30 6\n"
        end += "pop\n"
        
        end += "pop\n"
        
        end += "pop\n"
        #Right Arm
        end += "push\n"
        end += "move\n60 60 0\n"
        end += "rotate\nz 5\n"
        end += "rotate\ny %d\n"%( -(i%18 - 9) * 5 )
        end += "box\n0 0 20 40 100 40\n"
        end += "pop\n"
        #Left Leg
        end += "push\n"
        end += "move\n -30 -60 0\n"
        end += "rotate\nx %d\n"%( -(i%18 - 9) * 3 )
        end += "box\n-25 0 25 50 100 50\n"
        end += "pop\n"
        #Right Leg
        end += "push\n"
        end += "move\n 30 -60 0\n"
        end += "rotate\nx %d\n"%( (i%18 - 9) * 3 )
        end += "box\n-25 0 25 50 100 50\n"
        end += "pop\n"
        if i < 10:
            end += "save\n anim/00%d.png\n"%(i)
        else:
            end += "save\n anim/0%d.png\n"%(i)
    print end
