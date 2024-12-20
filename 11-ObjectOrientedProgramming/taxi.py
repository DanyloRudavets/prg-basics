class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km



def main():
    # your program
    ride1=TaxiRide(5)
    ride2=TaxiRide(6)
    ride1.distance=40
    ride2.distance=20
    print(f' {TaxiRide.calculate_fare(ride1, ride1.distance)}')

if __name__ == "__main__":
    main()
