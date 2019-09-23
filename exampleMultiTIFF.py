from pyScanLib import pyScanLib

ls = pyScanLib() # load scanner library
devices = ls.getScanners()
print(devices)
ls.setScanner(devices[0])

ls.setDPI(300)
    
# A4 Example
#ls.setScanArea(width=8.26,height=11.693) # (left,top,width,height) in inches

ls.setPixelType("color") # bw/gray/color

pils = ls.multiScan()
if len(pils) > 0:
    pils[0].save("multiimage.tif", compression="tiff_deflate", save_all=True, append_images=pils[1:])
else:
    print("Error: "+ ls.lastError)
    
ls.closeScanner() # unselect selected scanner, set in setScanners()
ls.close() # Destory whole class
