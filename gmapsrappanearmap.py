
#from gmapsrappa import *

headerText = """<!DOCTYPE html "-//W3C//DTD XHTML 1.0 Strict//EN" 
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
    <title>#1: Basic Map - NearMap JavaScript API Examples</title>
    <script src="http://www.nearmap.com/api0.3/api.js" type="text/javascript"></script>
    <script type="text/javascript">
      function init() {"""

tailerText = """}
    </script>
  </head>
  <body onload="init()" onunload="nearmap.event.unload()">
    <div id="map_element" style="width: 640px; height: 480px"></div>
  </body>
</html>
"""



fileName = 'blah.html'

from nearmapsrappa import *

if __name__ == '__main__':
   try:
      fpo = open(fileName, mode = 'w')
   except IOError:
      sys.stderr.write("IOError on filename: %s\n" % fileName)
      sys.exit(1)

   fpo.write(headerText)

   nmap = NearMap("map", "map_element")
   nmap.center = NearMapCenter(LatLng(-33.89578, 151.2141), 15)
   nmap.setUIToDefault()
   polyLine = NearmapOverlayPolyline([LatLng(-33.89548, 151.2131), LatLng(-33.89588, 151.2121)])
   nmap.addOverlay(polyLine);	
   fpo.write(str(nmap))
   fpo.write(tailerText)
   print "ALL Done"
