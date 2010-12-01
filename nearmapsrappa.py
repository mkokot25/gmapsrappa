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
