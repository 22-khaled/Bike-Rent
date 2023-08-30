import datetime


class bikeshop:
    def __init__(self, s):


        self.s = s

    def stok(self):
        print("We have currently {} bikes available to rent.".format(self.s))
        return self.s

    def rent_per_hour(self, h):
        # h is an input, for available number of bikes customer want
        if h <= 0 and h > self.s :
            print("Number should be positive \n in our market we have only {} bike available".format(self.s))
            return 0
        else:
            now = datetime.datetime.now()
            print(
                'you have rented {} bike(s) on hourly rented basis today at {} hour '.format(h, now))
            print('you will be charged by 5$ per hour')
            print('hope enjoy this service')
            self.s -= h
            return now

    def rent_per_day(self, h):
        # h is an input, for available number of bikes in the shop
        if h <= 0 and h > self.s:
            print("Number should be positive \n in our market we have only {} bike available".format(
                self.s))
            return 0
        else:
            now = datetime.datetime.now()
            print(
                'you have rented {} bike(s) on daily rented basis today at {} hour '.format(h, now))
            print('you will be charged by 20$ per day')
            print('hope enjoy this service')
            self.s -= h
            return now

    def rent_per_week(self, h):
        # h is an input, for available number of bikes in the shop
        if h <= 0 and h > self.s:
            print("Number should be positive \n in our market we have only {} bike available".format(
                self.s))
            return 0
        else:
            now = datetime.datetime.now()
            print(
                'you have rented {} bike(s) on weekly rented basis today at {} hour '.format(h, now))
            print('you will be charged by 60$ per week')
            print('hope enjoy this service')
            self.s -= h
            return now

    def returnbike(self, a, bill=0):
        # a set for ask to return the bike
        rentaltime, rentalbase, NumberOfBikes = a
        if rentaltime and rentalbase and NumberOfBikes:
            self.s += NumberOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentaltime

            if rentalbase == 1:
                bill = (rentalPeriod.seconds / 3600) * 5 * NumberOfBikes
            elif rentalbase == 2:
                bill = (rentalPeriod.day) * 20 * NumberOfBikes
            elif rentalbase == 3:
                bill = (rentalPeriod.day / 7) * 60 * NumberOfBikes

            if (3 <= NumberOfBikes <= 5):
                print("You are eligible for Family rental promotion of 30% discount")
                bill = bill * 0.7
            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            return bill
        else:
            print("Are you sure you rented a bike with us?")
            return 0


class Customer:
    def __init__(self):
        self.NumberOfBikes = 0
        self.rentalbase = 0
        self.rentaltime = 0
        self.bill = 0

    def requestBike(self):
        NumberOfBikes = input('how many bike you want to rent?')
        try:
            NumberOfBikes % 2 == 0
        except ValueError:
            print("Invalid NUM")
            return 0

        else:
            self.NumberOfBikes = NumberOfBikes
                return self.bikes

    def returnBike(self):
        if self.rentalbase and self.rentaltime and self.NumberOfBikes:
            return self.rentaltime, self.rentalbase, self.NumberOfBikes
        else:
            return 0, 0, 0


def main():
    stok=bikeshop(int(input('how many bike do we have in our shop? ')))
    stok.stok()
    
    rentalbase=int(input('We rent bikes in 3 bases, \n 1. Rent per hour -  1hour = 5$ \n 2. Rent per day - 1day = 20$ \n 3. Rent per week - 1week = 60$ \n choose one from the above bases:  '))
    if rentalbase==1:
        hour=(stok.rent_per_hour(int(input('how many bike you want to rent'))))
    if rentalbase==2:
        day=stok.rent_per_day(int(input('how many bike you want to rent')))
    if rentalbase==3:
        week=stok.rent_per_week(int(input('how many bike you want to rent')))
    return rentalbase and stok
    
a=int(input('do you want to return your bike? Y/N'))
if a=='Y'.upper:
    bikeshop.returnbike
    
<<<<<<< Updated upstream
#while True   
main=main()
=======
    
m=main()
>>>>>>> Stashed changes
        
     
