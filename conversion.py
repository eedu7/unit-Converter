class TemperatureUnit:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit - 32) * 5 / 9 + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        return (kelvin - 273.15) * 9 / 5 + 32


class WeightUnit:
    @staticmethod
    def milligram_to_gram(mg):
        return mg / 1000

    @staticmethod
    def milligram_to_kilogram(mg):
        return mg / 1_000_000

    @staticmethod
    def milligram_to_ounce(mg):
        return mg / 28_349.5

    @staticmethod
    def milligram_to_pound(mg):
        return mg / 453_592

    @staticmethod
    def gram_to_milligram(g):
        return g * 1000

    @staticmethod
    def gram_to_kilogram(g):
        return g / 1000

    @staticmethod
    def gram_to_ounce(g):
        return g / 28.3495

    @staticmethod
    def gram_to_pound(g):
        return g / 453.592

    @staticmethod
    def kilogram_to_milligram(kg):
        return kg * 1_000_000

    @staticmethod
    def kilogram_to_gram(kg):
        return kg * 1000

    @staticmethod
    def kilogram_to_ounce(kg):
        return kg * 35.274

    @staticmethod
    def kilogram_to_pound(kg):
        return kg * 2.20462

    @staticmethod
    def ounce_to_milligram(oz):
        return oz * 28_349.5

    @staticmethod
    def ounce_to_gram(oz):
        return oz * 28.3495

    @staticmethod
    def ounce_to_kilogram(oz):
        return oz / 35.274

    @staticmethod
    def ounce_to_pound(oz):
        return oz / 16

    @staticmethod
    def pound_to_milligram(lb):
        return lb * 453_592

    @staticmethod
    def pound_to_gram(lb):
        return lb * 453.592

    @staticmethod
    def pound_to_kilogram(lb):
        return lb / 2.20462

    @staticmethod
    def pound_to_ounce(lb):
        return lb * 16


class LengthUnit:
    @staticmethod
    def millimeter_to_centimeter(mm):
        return mm / 10

    @staticmethod
    def millimeter_to_meter(mm):
        return mm / 1000

    @staticmethod
    def millimeter_to_kilometer(mm):
        return mm / 1_000_000

    @staticmethod
    def millimeter_to_inch(mm):
        return mm / 25.4

    @staticmethod
    def millimeter_to_foot(mm):
        return mm / 304.8

    @staticmethod
    def millimeter_to_yard(mm):
        return mm / 914.4

    @staticmethod
    def millimeter_to_mile(mm):
        return mm / 1_609_344

    @staticmethod
    def centimeter_to_millimeter(cm):
        return cm * 10

    @staticmethod
    def centimeter_to_meter(cm):
        return cm / 100

    @staticmethod
    def centimeter_to_kilometer(cm):
        return cm / 100_000

    @staticmethod
    def centimeter_to_inch(cm):
        return cm / 2.54

    @staticmethod
    def centimeter_to_foot(cm):
        return cm / 30.48

    @staticmethod
    def centimeter_to_yard(cm):
        return cm / 91.44

    @staticmethod
    def centimeter_to_mile(cm):
        return cm / 160_934.4

    @staticmethod
    def meter_to_millimeter(m):
        return m * 1000

    @staticmethod
    def meter_to_centimeter(m):
        return m * 100

    @staticmethod
    def meter_to_kilometer(m):
        return m / 1000

    @staticmethod
    def meter_to_inch(m):
        return m * 39.3701

    @staticmethod
    def meter_to_foot(m):
        return m * 3.28084

    @staticmethod
    def meter_to_yard(m):
        return m * 1.09361

    @staticmethod
    def meter_to_mile(m):
        return m / 1609.344

    @staticmethod
    def kilometer_to_millimeter(km):
        return km * 1_000_000

    @staticmethod
    def kilometer_to_centimeter(km):
        return km * 100_000

    @staticmethod
    def kilometer_to_meter(km):
        return km * 1000

    @staticmethod
    def kilometer_to_inch(km):
        return km * 39_370.1

    @staticmethod
    def kilometer_to_foot(km):
        return km * 3_280.84

    @staticmethod
    def kilometer_to_yard(km):
        return km * 1_093.61

    @staticmethod
    def kilometer_to_mile(km):
        return km / 1.609344

    @staticmethod
    def inch_to_millimeter(inch):
        return inch * 25.4

    @staticmethod
    def inch_to_centimeter(inch):
        return inch * 2.54

    @staticmethod
    def inch_to_meter(inch):
        return inch / 39.3701

    @staticmethod
    def inch_to_kilometer(inch):
        return inch / 39_370_000

    @staticmethod
    def inch_to_foot(inch):
        return inch / 12

    @staticmethod
    def inch_to_yard(inch):
        return inch / 36

    @staticmethod
    def inch_to_mile(inch):
        return inch / 63_360

    @staticmethod
    def foot_to_millimeter(foot):
        return foot * 304.8

    @staticmethod
    def foot_to_centimeter(foot):
        return foot * 30.48

    @staticmethod
    def foot_to_meter(foot):
        return foot * 0.3048

    @staticmethod
    def foot_to_kilometer(foot):
        return foot / 3_280_840

    @staticmethod
    def foot_to_inch(foot):
        return foot * 12

    @staticmethod
    def foot_to_yard(foot):
        return foot / 3

    @staticmethod
    def foot_to_mile(foot):
        return foot / 5_280

    @staticmethod
    def yard_to_millimeter(yard):
        return yard * 914.4

    @staticmethod
    def yard_to_centimeter(yard):
        return yard * 91.44

    @staticmethod
    def yard_to_meter(yard):
        return yard * 0.9144

    @staticmethod
    def yard_to_kilometer(yard):
        return yard / 1_093_613

    @staticmethod
    def yard_to_inch(yard):
        return yard * 36

    @staticmethod
    def yard_to_foot(yard):
        return yard * 3

    @staticmethod
    def yard_to_mile(yard):
        return yard / 1_760

    @staticmethod
    def mile_to_millimeter(mile):
        return mile * 1_609_344

    @staticmethod
    def mile_to_centimeter(mile):
        return mile * 160_934.4

    @staticmethod
    def mile_to_meter(mile):
        return mile * 1_609.344

    @staticmethod
    def mile_to_kilometer(mile):
        return mile * 1.609344

    @staticmethod
    def mile_to_inch(mile):
        return mile * 63_360

    @staticmethod
    def mile_to_foot(mile):
        return mile * 5_280

    @staticmethod
    def mile_to_yard(mile):
        return mile * 1_760
