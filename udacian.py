class Udacian():
      def __init__(self , name , city , entrollment , nanodegree, ststus):
          self.udacian_name= name
          self.udacian_city= city
          self.udacian_entrollment = entrollment
          self.udacian_nanodegree= nanodegree
          self.udacian_ststus = ststus

      def print_udacian(self):
          print(self.udacian_name+" is " + self.udacian_entrollment+ " in "+ self.udacian_city+ " studying "+ self.udacian_nanodegree + "he/she is " + self.udacian_ststus)


