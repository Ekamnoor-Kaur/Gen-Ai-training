# ticket booking system
class BookTicket:
    def __init__(self,eventname):
        self.eventname=eventname
        self.seatsavailable=2000
        self.seatsbooked=0
        self.price=500
        self.bookingid=1000

    def checkAvailability(self,seats):
        if self.seatsavailable>=seats:
            print("seats are available")
            print("Price per seat: ",self.price)
        else:
            print("seats not available")

    def bookTicket(self,seats):
         if self.seatsavailable>=seats:
            self.seatsavailable-=seats
            self.seatsbooked+=seats
            totalamt=seats*self.price
            self.bookingid+=1
            print("Ticket Booked!")
            print("Event name: ",self.eventname)
            print("Booking Id: ",self.bookingid )
            print("Seats booked: ",seats)
            print("Total amount to be paid",totalamt)
         else:
            print("Booking failed! Not enough seats available.")

    def eventStatus(self):
        print("Event name:",self.eventname)
        print("Total seats:",self.seatsbooked+self.seatsavailable)
        print("Seats left:",self.seatsavailable)
        print("Seats booked:",self.seatsbooked)

t=BookTicket("Sunburn Festival")
while True:
    print("1. Seats Availability")
    print("2. Book Ticket")
    print("3. Event Status")
    print("4. Exit")
    ch=int(input("enter choice"))
    if ch==1:
        s=int(input("Enter required number of seats:"))
        t.checkAvailability(s)
    elif ch==2:
        s=int(input("Enter number of seats to book:"))
        t.bookTicket(s)
    elif ch==3:
        print("Event status: ")
        t.eventStatus()
    elif ch==4:
        print("Exiting... Thank you!")
        break
    else:
        print("invalid choice")