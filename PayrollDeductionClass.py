class Payroll_deduction:
    def __init__(self, desc, date, chrg_amt, ID):
        self.desc = desc
        self.ID = ID
        self.date = date 
        self.chrg_amt = chrg_amt
    ## set   
    def set_desc(self, desc):
        self.__desc = desc
    def set_ID(self, ID):
        self.__ID = ID 
    def set_date(self, date):
        self.__date = date  
    def set_chrg_amt(self, chrg_amt):
        self.__chrg_amt = chrg_amt
    ## get
    def get_desc(self):
        return self.__desc
    def get_ID(self):
        return self.__ID
    def get_date(self):
        return self.__date
    def get_chrg_amt(self):
        return self.__chrg_amt
