import EmployeeClass as EC 
import PayrollDeductionClass as PDC 


def main():
    #Jimmy part 
    # name = "Jimmy Smith"
    # ID = "58475"
    # department = "Informaton Systems"
    # job_title = "developer"
    # month_sal = 6800.00

    #Jimmy instance 
    emp = EC.Employee("Jimmy Smith", "58475", "Informaton Systems", "developer", 6800.00) 


    # 5 deductions part 
    # desc1 = "food court"
    # date1 = "8/14/2022"
    # chrg1 = 22.50
    # ID1 = "39119"

    # desc2 = "gift contribution"
    # date2 = "8/12/2022"
    # chrg2 = 25.00
    # ID2 = "58475"

    # desc3 = "food court"
    # date3 = "8/17/2022"
    # chrg3 = 15.25
    # ID3 = "21547"

    # desc4 = "vending machine"
    # date4 = "8/22/2022"
    # chrg4 = 3.00
    # ID4 = "58475"

    # desc5 = "vending machine"
    # date5 = "8/5/2022"
    # chrg5 = 2.75
    # ID5 = "58475"

    #deduction instances 
    ded1 = PDC.Payroll_deduction("food court","8/14/2022", 22.50,"39119")
    ded2 = PDC.Payroll_deduction("gift contribution","8/12/2022",25.00,"58475")
    ded3 = PDC.Payroll_deduction("food court","8/17/2022",15.25,"21547")
    ded4 = PDC.Payroll_deduction("vending machine","8/22/2022",3.00,"58475")
    ded5 = PDC.Payroll_deduction("vending machine","8/5/2022",2.75,"58475")

    
    #gross_pay = emp.get_mon_sal() - ded2.get_chrg_amt() - ded4.get_chrg_amt() - ded5.get_chrg_amt()



    #print functions 

    print('*** Employee Pay ***')
    print('Name: ', emp.get_name())
    print('ID Number: ', emp.get_ID())
    print('Department: ', emp.get_department())
    print('Gross Pay: ' emp.get_mon_sal())
    Net_pay = emp.get_mon_sal() - ded2.get_chrg_amt() - ded4.get_chrg_amt() - ded5.get_chrg_amt()
    print('Net Pay: ', Net_pay)


main()

#comments are from trying to do this another way 

