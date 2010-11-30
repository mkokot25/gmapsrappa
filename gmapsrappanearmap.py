
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

class LatLng(object):
   def __init__(self, lat, lon):
      self.lat = lat
      self.lon = lon
   def __str__(self):
      return "new nearmap.maps.LatLng(%f, %f)" % (self.lat, self.lon)


class NearMapCenter(object):
   def __init__(self, latLng, zoom):
      self.latLng = latLng
      self.zoom = zoom
   def __str__(self):
      return "setCenter(new nearmap.maps.LatLng(%f, %f), %d);\n" % (self.latLng.lat, self.latLng.lon, self.zoom)

class NearmapOverlayPolyline(object):
   latLngs = []
   def __init__(self, arrayOfLatLng):
      self.latLngs = arrayOfLatLng
      
class NearMap(object):
   polyLines = []
   def __init__(self, instance, element_frame):
      self.instance_ = instance
      self.element_frame_ = element_frame
   def setUIToDefault(self):
      self.setUIToDefault_ = True
	  
   def addOverlay(self, polyline):
      self.polyLines.append(polyline.latLngs)
		 
   def __str__(self):
      rr = 'var %s = new nearmap.maps.Map2(document.getElementById("%s"));\n' % (self.instance_, self.element_frame_)
      for field in self.__dict__:
         if field[-1] == '_':
            continue
         aa = getattr(self, field)

#       if aa.__class__ == str:
#            rr += str(aa)
#         else:
         rr += self.instance_ + "."
         rr += str(aa)
      if self.setUIToDefault_:
         rr += self.instance_ + ".setUIToDefault();\n"
      pln = 0
      for polyLine in self.polyLines:
         rr += "var polyline%d  = new nearmap.overlay.Polyline([" % pln
         for latLng in polyLine:
            rr += str(latLng)
            if latLng != polyLine[-1]:
               rr += ", "
         rr += "]);\n"
         rr += "map.addOverlay(polyline%d);\n" % pln
         pln += 1
      return rr


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
   print nmap
   fpo.write(str(nmap))
   fpo.write(tailerText)
   print "ALL Done"
