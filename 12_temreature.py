# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) 
# that returns the Fahrenheit value.

class TempreatureConveter:
    
    @staticmethod
    def celsius_to_fernheite(celcius):
        return (celcius * 9/5) + 32
    
print(TempreatureConveter.celsius_to_fernheite(10))
print(TempreatureConveter.celsius_to_fernheite(70))