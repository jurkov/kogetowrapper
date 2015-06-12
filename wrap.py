from PIL import Image, ImageDraw
from math import sin, cos, pi

def avgcolor(colarray):
    c = [0,0,0]
    div = len(colarray)
    #print len(colarray)
    #print colarray
    
    for f in range(div):
        
        c[0] += colarray[f][0]
        c[1] += colarray[f][1]
        c[2] += colarray[f][2]
        #c[3] += colarray[f][3]
        #print c, colarray
        
    
    for i in range(3):
        c[i] = c[i]/div
    
    #print c
    return (c[0],c[1],c[2])

def calccolor(im, pos):
    """
    *---*---*---*
    I   I   I   I
    *---*---*---*
    I   I   I   I
    *---*---*---*
    I   I   I   I
    *---*---*---*
    """
    if (pos[0] - int(pos[0])<0.333): #x
        if (pos[1] - int(pos[1])<0.333): #y
            p = (int(pos[0]-1),int(pos[1]-1))
            c1 = im.getpixel(p)
            p = (int(pos[0]-1),int(pos[1]))
            c2 = im.getpixel(p)
            p = (int(pos[0]),int(pos[1]-1))
            c3 = im.getpixel(p)
            p = (int(pos[0]),int(pos[1]))
            c4 = im.getpixel(p)
            return avgcolor((c1,c2,c3,c4))
        
        elif (pos[1] - int(pos[1])<0.666):
            p = (int(pos[0]-1),int(pos[1]))
            c1 = im.getpixel(p)
            p = (int(pos[0]),int(pos[1]))
            c2 = im.getpixel(p)
            return avgcolor((c1,c2))
            
        else:
            p = (int(pos[0]-1),int(pos[1]))
            c1 = im.getpixel(p)
            p = (int(pos[0]-1),int(pos[1]+1))
            c2 = im.getpixel(p)
            p = (int(pos[0]),int(pos[1]+1))
            c3 = im.getpixel(p)
            p = (int(pos[0]),int(pos[1]))
            c4 = im.getpixel(p)
            return avgcolor((c1,c2,c3,c4))
        
    elif(pos[0] - int(pos[0])<0.666):
        if (pos[1] - int(pos[1])<0.333):
            p = (int(pos[0]),int(pos[1]-1))
            c1 = im.getpixel(p)
            p = (int(pos[0]),int(pos[1]))
            c2 = im.getpixel(p)
            return avgcolor((c1,c2))           
            
        elif (pos[1] - int(pos[1])<0.666):
            p = (int(pos[0]),int(pos[1]))
            c = im.getpixel(p)
            #return (0,0,0,0)
            return c
        
        else:
            p = (int(pos[0]),int(pos[1]+1))
            c1 = im.getpixel(p)
            p = (int(pos[0]),int(pos[1]))
            c2 = im.getpixel(p)
            return avgcolor((c1,c2))
    else:
        if (pos[1] - int(pos[1])<0.333):
            p = (int(pos[0]),int(pos[1]-1))
            c1 = im.getpixel(p)
            p = (int(pos[0]-1),int(pos[1]+1))
            c2 = im.getpixel(p)
            p = (int(pos[0]),int(pos[1]+1))
            c3 = im.getpixel(p)
            p = (int(pos[0]),int(pos[1]))
            c4 = im.getpixel(p)
            return avgcolor((c1,c2,c3,c4))
        
        elif (pos[1] - int(pos[1])<0.666):
            p = (int(pos[0]),int(pos[1]+1))
            c1 = im.getpixel(p)
            p = (int(pos[0]),int(pos[1]))
            c2 = im.getpixel(p)
            return avgcolor((c1,c2))
            
        else:
            p = (int(pos[0]),int(pos[1]+1))
            c1 = im.getpixel(p)
            p = (int(pos[0]+1),int(pos[1]+1))
            c2 = im.getpixel(p)
            p = (int(pos[0]+1),int(pos[1]))
            c3 = im.getpixel(p)
            p = (int(pos[0]),int(pos[1]))
            c4 = im.getpixel(p)
            return avgcolor((c1,c2,c3,c4))
    
def intpos(pos):
    return (int(pos[0]),int(pos[1]))

def wrapimage(imgin, imgout):
    im = Image.open(imgin)
    
    innercircle = (im.size[0]/2+11,im.size[1]/2+50)
    innerradius = 322
    outerradius = 640
    
    #############################
    #debug
    #############################
    
    #draw = ImageDraw.Draw(im)
    #draw.ellipse((innercircle[0]-innerradius, innercircle[1]-innerradius, innercircle[0]+innerradius, innercircle[1]+innerradius), outline=128)
    #draw.ellipse((innercircle[0]-outerradius, innercircle[1]-outerradius, innercircle[0]+outerradius, innercircle[1]+outerradius), outline=128)
    #del draw
    
    size = (1800.0,outerradius - innerradius)
    
    out = Image.new('RGBA', (int(size[0]),int(size[1])), (255,255,255,0))
    
    for x in range(int(size[0])):
        q = (pi*2/size[0]) *x
        for y in range(size[1]):
            pos = (
                      
                      (innerradius+y)* cos(q) + innercircle[0], 
                      (innerradius+y)* sin(q) + innercircle[1]
                  )
            #color = calccolor(im,pos)
    
            color = im.getpixel(intpos(pos))
            out.putpixel((x,y),color)
            
            #im.putpixel(pos,(255,255,255,0))
    
    # write to stdout
    #im.save("wrap.jpg")
    #im.show()
    out.save(imgout)
    #out.show()

wrapimage("IMG_20150611_200757.jpg","IMG_20150611_200757_wrap.jpg")

