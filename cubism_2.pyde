 ## Assignment: Cubism
 ## Student: Daniel Wooden
 ## Pasadena City College, Spring 2026
 ## Course Name: DMA60 Creative Coding
 ## Prof. George McKinney
 ## Project Description: Cubism
 ## Last Modified: 3/29/26
 ## Notes: I feel like I need more time to work on this, but I will still be submitting this.

def setup():
    size(500, 500)

def draw():
    background(0)
    stroke(0)         
    strokeWeight(0.5)   
    
## disco grid
    for i in range(0, 500, 20):
        for x in range(0, 500, 20):
            r = int(random(0, 255))
            g = int(random(0, 255))
            b = int(random(0, 255))
            fill(r, g, b)
            rect(x, i, 20, 20)
            
## triangle head
    fill(255, 220, 0)
    triangle(280, 50, 380, 290, 200, 290)
    
## split triangle face
    fill(255, 180, 0)
    triangle(280, 50, 300, 290, 200, 290)
    
## animation pupils
    moveX = sin(frameCount * 0.15) * 5
    moveY = cos(frameCount * 0.15) * 5
    
## uneven eyes
    fill(255, 0 , 255)
    rect(235, 125, 25, 25)
    rect(305, 115, 25, 25)
    
## pupils
    fill(255, 255, 0)
    rect(245 + moveX, 135 + moveY, 5, 5)
    rect(315 + moveX, 125 + moveY, 5, 5)
    
## circle body
    fill(255, 220, 0)
    ellipse(290, 350, 120, 120)
    
## rectangle under circle
    fill(255, 180, 0)
    rect(150, 410, 280, 60)
