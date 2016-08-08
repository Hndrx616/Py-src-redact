'''
author Stephen Hilliard (c) 2015.
developer Stephen Hilliard (c) 2015.
'''
from turtle import Turtle, Screen
import random
from math import cos, radians


class Schooler(Turtle):
    swarm = []

    def __init__(self):
        Turtle.__init__(self)
        self.up()
        self.setheading(random.randrange(360))
        self.setpos(random.randrange(-200,200),random.randrange(-200,200))
        self.down()
        self.newHead = None
        Schooler.swarm.append(self)

    def getNewHeading(self):
        minangle = 999
        for other in Schooler.swarm:
            if self != other:
                head = self.towards(other) - self.heading()
                if cos(radians(head)) > 0:
                    if head < minangle:
                        minangle = head
        if minangle == 999:
            self.newHead = self.heading()
        else:
            self.newHead = minangle+self.heading()

    def inFrontOf(self,other):
        head = self.towards(other) - self.heading()
        if cos(radians(head)) > 0:
            return True
        return False

    def setHeadingAndMove(self):
        self.setheading(self.newHead)
        self.newHead = None
        self.forward(10)
		
class Obstacle(Turtle):
	obstacles = []
	def __init__(self):
		Turtle.__init__(self)
		self.up()
		self.setpos(random.randrange(-200,200),random.randrange(-200,200))
		self.shape('circle')
		Obstacles.obstacle.append(self)

class FocalFish(Schooler):
    repulse = 10
    align = 50
    attract = 600

    def getNewHeading(self):
        repulsion = []
        alignment = []
        attraction = []

        for other in Schooler.swarm:
            if self != other:
                dist = self.distance(other)
                if dist <= self.repulse:
                    repulsion.append(other)
                elif dist <= self.align:
                    alignment.append(other)
                elif dist <= self.attract:
                    attraction.append(other)

        self.newHead = self.heading()
        if repulsion:
            x = 0
            y = 0
            for o in repulsion:
                x = x + o.xcor()
                y = y + o.ycor()

            self.newHead = self.towards(x/len(repulsion),y/len(repulsion)) + 180

        elif alignment:
            hs = self.heading()
            for other in alignment:
                hs = hs + other.heading()
            self.newHead = hs // (len(alignment)+1)

        elif attraction:
            x = 0
            y = 0
            for o in attraction:
                x = x + o.xcor()
                y = y + o.ycor()
            self.newHead = self.towards(x/len(attraction),y/len(attraction))

class ObstacleFish(FocalFish):
	def __init__(self):
		FocalFish.__init__(self)
		if random.randrange(100) == 0:
			self.amLeader = Trueself.color('red','red')
			print "I'm a leader!!!"
		else:
			self.amLeader = False
			
	def getNewHeading(self):
		if self.amLeader:
			if random.randrange(100) == 0:
				print "whimsically changing direction"
				self.newHead = random.randrange(360)
			else:
				self.newHead = self.heading()
			return
		else:
			def getNewHeading(self):
				avoiding = False
				for o in Obstacle.obstacles:
					if self.inFrontOf(o) and self.distance(o) < 40:
						angleTo = (self.towards(o) - self.heading())%360
						if angleTo < 45:
							print "taking leftward evasive ", angleTo
							self.newHead = self.heading() - 25
							avoiding = True
						elif angleTo > 315:
							self.newHead = self.heading() + 25
							print "taking rightward evasive ", angleTo
							avoiding = True
				if not avoiding:
					FocalFish.getNewHeading(self)
					
class LeaderFish(ObstacleFish):
	def __init__(self):
		ObstacleFish.__init__(self)
		self.color('red','red')
		
	def getNewHeading(self):
		if random.randrange(100) == 0:
			print "whimsically changing direction"
			self.newHead = random.randrange(360)
		else:
			self.newHead = self.heading()
		return

class ObstacleFish(Schooler):
    def getNewHeading(self):
        avoiding = False
        for o in Obstacle.obstacles:
            if self.inFrontOf(o) and self.distance(o) < 40:
                angleTo = (self.towards(o) - self.heading())%360
                if angleTo < 45:
                    print ("taking leftward evasive ", angleTo)
                    self.newHead = self.heading() - 25
                    avoiding = True
                elif angleTo > 315:
                    self.newHead = self.heading() + 25
                    print ("taking rightward evasive ", angleTo)
                    avoiding = True
        return avoiding

def main():
    swarmSize = 50
    t = Turtle()
    win = Screen()
    win.setworldcoordinates(-600,-600,600,600)
    t.speed(10)
    t.hideturtle()
    t.tracer(15)

    for i in range(swarmSize):
        FocalFish()

    for turn in range(300):
        for schooler in Schooler.swarm:
            schooler.getNewHeading()

        for schooler in Schooler.swarm:
            schooler.setHeadingAndMove()

    win.exitonclick()


main()
