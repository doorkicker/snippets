from math import *
from PIL import Image
import copy

'''
n: the number to destructure
target: the value we are dividing by
tac: target-as-constant. Very helpfully named /s. If true, the target itself is subtracted at each round
  of iteration
indexonly: return only whether or not a division by the target occured, and not the number of divisions total
basis: what value to end a division on.
adjust: how much to adjust the initial results to start the process
constant: a value to add to the count.

EXAMPLE
In the simply case, an n of 15.

(15-1) = 14
14/2 = 7
Can we add divide by the target again (2)?
No? So we add a 1 at index 0, and move on to the next index.
(7-1)=6
6/2 = 3
Can we add divide by the target again (2)?
No. So we add a 1 at index 1, and move on to the next index.

3-1 = 2
2/2 = 1

We mark the last index, and subtract 1 from the running total.
Our result now equals the basis, 0, and so we return the vector of results.
'''
def findAb(n, target=2, tac=False, indexonly = False, basis=0, adjust=1, constant=1, suppress=True):
  count = 0
  elm = [] #ab elements
  c = constant
  result = floor(n)-adjust
  #t = floor(target)
  t = target
  if tac == True:
    c = target
  
  while result > basis:
    #print("result: " + str(result))
    if (result/t)%1 < Dec('0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001'):
      #print("prior: " + str(result))
      result = result/t
      #print("post: " + str(result))
      #_  = input("press [enter] to continue.")
      count = count + c
    else:
      if indexonly == True and count > 0:
        elm.append(1)
      else:
        elm.append(count)
      count = 0
      result = result - c
  
  #print("done calculating structure - result: " + str(result) + ",  elm: " + str(elm))
  if suppress == False:
    print("done calculating structure - result: " + str(result) + ",  elm len: " + str(len(elm)))
  #with HiddenPrints():
  #  return elm
  return elm
   
#ab is a shell structure, like returned from ab. It should be
#in ab111111 format or in list format
def nhot(ab):
   results = []
   i = 0
   while i < len(ab):
     if ab[i] > 0:
       results.append({"val": ab[i], "index": i})
     i = i + 1
   
   return results
   
   
   
def fingerprint(z, lsmax=len(first_primes_list)):
  i = 0
  struct = []
  while i < lsmax and primes[i] < z:
    elm = []
    elm = findAb(z, primes[i], False, True)
    i = i + 1
    struct.append(elm)
  #print("ab structure computation over range complete!")
  return struct

  
  
  
'''
Instead of padding the list, why not loop through it as, is
Setting pixels as needed, on a much larger image thats been
padded for you by initializing its rightmost dimension to
the list element with the largest length?
'''

#takes an fingerprint and produces image output
def fpOut(fp, savewhendone=False, showOnDone=False):
  #print("new image...")
  img = Image.new("RGB", (fplen(fp), len(fp)), "black")
  #print("loading pixels...")
  pixels = img.load()
  i = 0
  #print("iterating pixels...")
  while i < len(fp):
    j = 0
    while j < len(fp[i]):
      #print("setting pixel x:" + str(j) + ",  y: " + str(i))
      pixels[j, i] = ((fp[i][j])*255, (fp[i][j])*255, (fp[i][j])*255)
      #pixels[j, i] = (255, 255, 255)
      j = j + 1
    i = i + 1
  
  #img.show()
  if showOnDone == True:
    img.show()
  
  if savewhendone == True:
    name = pType + "-" + "a" + str(int(a)) + "b" + str(int(b)) + ".bmp"
    img.save(os.getcwd() + "\\" + "fingerprints\\" + name)
    img.close()
  else:
    #img.close()
    return img
    
    
def fpOutSave():
  fp = fingerprint(p)
  fpOut(fp, True)

  
''' 
For the comparisons, we can set 
(case a) yellow dots on a copy of the smaller image, 
(case b) on a copy of the larger image, or 
(case c) on a new image we could also set ONLY yellow dots, copying only that which matches.

'''
def fpGetFileCompare(case="small", suppress=True):
  #print("be sure to use appropriate extensions, and leave no extra spaces or other chars not in the name")
  imgx = input("image 1 filename: ")
  imgy = input("image 2 filename: ")
  
  imgx = Image.open(imgx)
  imgy = Image.open(imgy)
  
  xpix = imgx.load()
  ypix = imgy.load()
  
  if (imgx.height * imgx.width) < (imgy.height * imgy.width):
    sz = "x"
  elif (imgx.height * imgx.width) < (imgy.height * imgy.width):
    sz = "y"
  elif imgx.width > imgy.width:
    #if they're both the same area or something goes wrong
    sz = "x"
  else:
    sz = "y"
  
  #new image for storing comparison
  if case == "small":
    if sz == "x":
      imgz = imgx.copy()
    elif sz == "y":
      imgz = imgy.copy()
  elif case == "large":      
    if sz == "x":
      imgz = imgy.copy()
    elif sz == "y":
      imgz = imgx.copy()
  elif case == "new":
    if sz == "x":
      imgz = Image.new("RGB", imgx.width, imgx.height, "black")
    elif sz == "y":
      imgz = Image.new("RGB", imgy.width, imgy.height, "black")
    else:
      #just choose x by default
      imgz = Image.new("RGB", imgx.width, imgx.height, "black")

  zpix = imgz.load()
  
  if imgx.height < imgy.height:
    imax = imgx.height
  else:
    imax = imgy.height
    
  if imgx.width < imgy.width:
    jmax = imgx.width
  else:
    jmax = imgy.width
  
  total = 0
  ytotal = 0
  xtotal = 0
  match = 0
  i = 0
  while i < imax:
    j = 0
    while j < jmax:
      if ypix[j, i] == (255, 255, 255):
        ytotal = ytotal + 1
      if xpix[j, i] == (255, 255, 255):
        xtotal = xtotal + 1
      
      if xpix[j, i] == ypix[j, i] and xpix[j, i] == (255, 255, 255):
        zpix[j, i] = (255, 255, 0)
        match = match + 1
      
      total = total + 1
      j = j + 1
    
    i = i + 1
    
  #done
  if suppress == False:
    print("done. matching: " + str((match/(ytotal+1))*100)[0:7] + "%  (" + str(match) + "/" + str(ytotal) + ")")
  imgz.show()
  
  
  
  
#blends two images
def composite(img1, img2):
  #first determine which is largest, so we can copy from it, assuming all images are the same height
  if img1.width > img2.width:
    imgz = img1.copy()
  else:
    imgz = img2.copy()
  
  #then determine bounds, so we're copying from the smallest to the largest
  if img1.width < img2.width:
    jmax = img1.width
  else:
    jmax = img2.width
  
  if img1.height < img2.height:
    imax = img1.height
  else:
    imax = img2.height
    
  xpix = img1.load()
  ypix = img2.load()
  zpix = imgz.load()
  print(f"imax: {imax}, j:{jmax}")
  #_ = input("press [enter] to continue.")
  i = 0
  while i < imax:
    j = 0
    while j < jmax:
      #print(f"i: {i}, j: {j}")
      if xpix[j, i] == (255, 255, 255) or ypix[j, i] == (255, 255, 255):
        zpix[j, i] == (255, 255, 255)
      j = j + 1
    i = i + 1
  
  #imgz.show()
  return imgz.copy()
  
# example usage:
# composite(fpOut(fingerprint(floor(p)), False, False), fpOut(fingerprint(floor(a)), False, False))
  
  
#takes 2 variables, and fingerprints them if they are not of type Image.Image
def fpVarCompare(z0, z1, case="small", copyBase=False, suppress=False, xshift=0, yshift=0):
  #print("be sure to use appropriate extensions, and leave no extra spaces or other chars not in the name")
  #print("z0: " + str(z0)  + ",  z1: " + str(z1))
  #_ = input("press [enter] to continue.")
  if type(z0) != Image.Image:
    imgx = fpOut(fingerprint(floor(z0)), False, False)
  else:
    imgx = z0.copy()
    
  if type(z1) != Image.Image:
    imgy = fpOut(fingerprint(floor(z1)), False, False)
  else:
    imgy = z1.copy()
  
  if xshift != 0 or yshift != 0:
    imgx = imgx.transform(imgx.size, Image.AFFINE, (1, 0, xshift, 0, 1, yshift))
  
  xpix = imgx.load()
  ypix = imgy.load()
  
  
  
  if (imgx.height * imgx.width) < (imgy.height * imgy.width):
    sz = "x"
  elif (imgx.height * imgx.width) < (imgy.height * imgy.width):
    sz = "y"
  elif imgx.width > imgy.width:
    #if they're both the same area or something goes wrong
    sz = "x"
  else:
    sz = "y"
  
  #new image for storing comparison
  if case == "small":
    if sz == "x":
      imgz = imgx.copy()
    elif sz == "y":
      imgz = imgy.copy()
  elif case == "large":      
    if sz == "x":
      imgz = imgy.copy()
    elif sz == "y":
      imgz = imgx.copy()
  elif case == "new":
    if sz == "x":
      if copyBase == True:
        imgz = imgx.copy()
      else:
        imgz = Image.new("RGB", (imgx.width, imgx.height), "black")
    elif sz == "y":
      if copyBase == True:
        imgz = imgy.copy()
      else:
        imgz = Image.new("RGB", (imgy.width, imgy.height), "black")
    else:
      #just choose x by default
      if copyBase == True:
        imgz == imgx.copy()
      else:
        imgz = Image.new("RGB", imgx.width, imgx.height, "black")
  
  #if copyBase == True:
  #  if imgx.width >= imgx.height:
  #    imgz = imgx.copy()
  #  else:
  #    imgz = imgy.copy()
  
  zpix = imgz.load()
  
  if imgx.height < imgy.height:
    imax = imgx.height
  else:
    imax = imgy.height
    
  if imgx.width < imgy.width:
    jmax = imgx.width
  else:
    jmax = imgy.width
  
  total = 0
  ytotal = 0
  xtotal = 0
  match = 0
  i = 0
  while i < imax:
    j = 0
    while j < jmax:
      if ypix[j, i] == (255, 255, 255):
        ytotal = ytotal + 1
      if xpix[j, i] == (255, 255, 255):
        xtotal = xtotal + 1
      
      if xpix[j, i] == ypix[j, i] and xpix[j, i] == (255, 255, 255):
        zpix[j, i] = (255, 255, 0)
        match = match + 1
      
      total = total + 1
      j = j + 1
    
    i = i + 1
  
  #done
  #if suppress == False:
  print("done. matching: " + str((match/(ytotal+1))*100)[0:7] + "%  (" + str(match) + "/" + str(ytotal) + ")")
  if suppress != True:
    imgz.show()
  
  return match/(ytotal+1)






  

  
  
def loadFingerprints():
  results = []
  path = os.getcwd() + "\\" + "fingerprints"
  for file in os.listdir(path):
    #print(str(file))
    results.append(file)
  
  fingerprints = []
  for name in results:
    filname = path + "\\" + name
    fingerprints.append(Image.open(filename))
  
  return fingerprints
 




 
#
# SCORECARD
# 
# fpScoreCard takes a fingerprint image and compares them to a base image.
# It starts with an all white image, and for each blackpixel in the test image, sets 
# that pixel to black in the scorecard. The result is, if run against a large collection of
# sample, returning only those points that remain constant, in a set, or say, between types.
# test case should return a copy of the img passed into it.

def fpScorecard(img, scorecard=None, width=0):
  imgx = img.copy()
  if scorecard != None:
    sc = scorecard.copy()
  else:
    sc = Image.new("RGB", (imgx.width, width), "white")
  
  xpix = imgx.load()
  ypix = sc.load()
  
  if imgx.width < sc.width:
    jmax = imgx.width
  else:
    jmax = sc.width
  
  
  if imgx.height > sc.height:
    imax = sc.height
  else:
    imax = imgx.height
  
  #print("imgx.height: " + str(imgx.height) + ", width: " + str(imgx.width))
  #print("sc.height: " + str(sc.height) + ", width: " + str(sc.width))
  
  
  total = 0
  ytotal = 0
  xtotal = 0
  match = 0
  i = 0
  while i < imax:
    j = 0
    while j < jmax:
      if ypix[j, i] == (255, 255, 255):
        ytotal = ytotal + 1
      if xpix[j, i] == (255, 255, 255):
        xtotal = xtotal + 1
      
      if xpix[j, i] == (0, 0, 0):
        ypix[j, i] = (0, 0, 0)
        match = match + 1
      
      total = total + 1
      j = j + 1
    
    i = i + 1
    
  #done
  #print("done. matching: " + str((match/ytotal)*100)[0:7] + "%  (" + str(match) + "/" + str(ytotal) + ")")
  #img.show()
  return sc.copy()





#  
#loads a list of fingerprints from a directory
#
#
def loadFingerprints():
  results = []
  path = os.getcwd() + "\\" + "fingerprints"
  for file in os.listdir(path):
    #print(str(file))
    results.append(file)
  
  fingerprints = []
  for name in results:
    filename = path + "\\" + name
    fingerprints.append(Image.open(filename))
  
  return fingerprints
  

  
  
#  
#loads a list of fingerprints from a directory
#loads fingerprints by type
#
def loadFingerprintsByType(pType):
  results = []
  path = os.getcwd() + "\\" + "fingerprints"
  fn = ""
  for file in os.listdir(path):
    #print(str(file))
    fn = file
    ptype = fn.split('-')[0]
    if ptype == pType:
      results.append(file)
  
  fingerprints = []
  for name in results:
    filename = path + "\\" + name
    fingerprints.append(Image.open(filename))
  
  return fingerprints

  
  
#
#finds the widest image in a set of PIL images, and returns the width of it  
#
#
def widestImg(ls):
  i = 0
  width = 0
  while i < len(ls):
    if ls[i].width > width:
      width = ls[i].width
    i = i + 1
  
  return width

  

#
# FPSCORELIST
#
# runs fpScoreCard against a list of fingerprints and shows the result (optional save to directory)
#
def fpScoreList(imgls=None):
  fplist = []
  if imgls == None:
    fplist = loadFingerprints()
  else:
    fplist = imgls
  width = widestImg(fplist)
  i = 0
  scorecard  = Image.new("RGB", (width, 70), "white")
  print("calculating scorecard...")
  while i < len(fplist):
    scorecard = fpScorecard(fplist[i], scorecard, width)
    i = i + 1
  
  scorecard.show()
  


if len(sys.argv) > 1:
  if sys.argv[1] == "fpOutSave":
    #print("fpout")
    fpOutSave()
  if sys.argv[1] == "loadFingerprints":
    fplist = []
    fplist = loadFingerprints()
  if sys.argv[1] == "fpScoreCard":
    fplist = []
    fplist = loadFingerprints()
    widest = widestImg(fplist)
    fpScorecard(fplist)
  if sys.arfv[1] == "fpScoreList":
    fpScoreList()
    
#fpGetFileCompare()




def findAdd(n, d):
  i = Dec(0)
  while True:
    if ((n+i)/d)%1 <= Dec(0):
      print(str(i))
      return i
    i = i + 1
  

def buildDiv(n):
  current = n+1 #our 
  results = []
  i = 0
  co = 0 #the coefficient we want to add to our current value to get an even result
  while True:
    print("calculating result...")
    co = findAdd(current, primes[i])
    #print(f"co: {co}")
    results.append([co, primes[i]])
    current = (current+co)/primes[i]
    if current <= 1:
      print(f"finished building division list, current: {current}")
      return results
    #else
    i = i + 1

    
#builds a string from an ab structure to show how it was arrived at
def divStr(base, ls):
  i = 0
  result = base+"+1" #name of variable used to build the string
  while i < len(ls):
    result = f"(({result}+{ls[i][0]})/{ls[i][1]}" 
    i = i + 1
  
  print(f"i: {i}")
  #finish by padding our output with closing parenthesis
  m = 0
  while m < i:
    result = f"{result})"
    m = m + 1
  
  return result
 
 
#test the result 
#s = divStr("b", buildDiv(b))
#print(s)

 