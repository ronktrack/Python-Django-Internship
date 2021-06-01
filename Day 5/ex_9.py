class Scheme:
    scheme_id = 11
    scheme_name = "jio prepaid"
    outgoing_rate = 1.5
    message_charge = 2
    def display(self):
        print("scheme_id: ",self.scheme_id)
        print("scheme_name: ",self.scheme_name)
        print("outgoing_rate: ",self.outgoing_rate)
        print("message_charge: ",self.message_charge)

class Customer(Scheme):
    cust_id = 11
    name = "jevin"
    mobile_no = 122843883
    def display1(self):
        print("cust_id: ",self.cust_id)
        print("name: ",self.name)
        print("mobile_no: ",self.mobile_no)

cust = Customer()
cust.display()
cust.display1()