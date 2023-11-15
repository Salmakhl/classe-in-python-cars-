class car():
    def __init__(self,name,color,type,enginePower,year) :
        self.name=name
        self.color = color
        self.type = type
        self.eP = enginePower
        self.year = year
       

    def information(self):
        print("the car name is :{} .year: {}  the engine power : {} , type: {} and color :{}. "
              .format(self.name,self.year,self.eP,self.type,self.color))


#the main programe
c1=car("Lotus Evija" ,2023,"1.500 kW (2,012 hp; 2,039 PS)",	"Electric","red")
c2=car("Aspark Owl" ,2020,"1.480 kW (1,985 hp; 2,012 PS)"	,"Electric","grey")
c3=car("Rimac Nevera/Pininfarina Battista",2022,"1.408 kW (1,888 hp; 1,914 PS)",	"Electric","black")
c4=car("Hennessey Venom F5",2022,"1.355 kW (1,817 hp; 1,842 PS)",	"Internal combustion","blue"	)
c5=car("SSC Tuatara"	,2022,	"1.305 kW (1,750 hp; 1,774 PS)", "Internal combustion",	"purple")


c1.information()
c2.information()
c3.information()
c4.information()
c5.information()


