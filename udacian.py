class Udacian():
      def __init__(self , name , city , entrollment , nanodegree, ststus):
          self.udacian_name= name
          self.udacian_city= city
          self.udacian_entrollment = entrollment
          self.udacian_nanodegree= nanodegree
          self.udacian_ststus = ststus

      def print_udacian(self):
          print(self.udacian_name+" is " + self.udacian_entrollment+ " in "+ self.udacian_city+ " studying "+ self.udacian_nanodegree + "he/she is " + self.udacian_ststus)


enterd_name = input("Input name: ")
enterd_city = input("Input city: ")
enterd_nanodegree = input("Input nanodegree(ex: FSND in sat with Ms. elham ): ")
enterd_status =input("Input status(ex:ontrack - not in track): ")

user = Udacian(enterd_name ,enterd_city , "entrolled" , enterd_nanodegree , enterd_status)
