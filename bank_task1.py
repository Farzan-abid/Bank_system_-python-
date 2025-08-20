def main():
    acc1={"name":"farzan",
             "account no":1111222233334444,
             "balance":20000,
             "pin":1234}
    acc2={
        "name":"ayan",
        "account no":4444333322221111,
        "balance":30000,
        "pin":4321


    }
    acclist=[acc1,acc2]

    transaction=[]
    tid=0

    while  True:
       op=int(input("enter 1 to login \n enter 2 to exit"))
       if op==1:
           acc_no=int(input("enter account no:"))
           acc_pin=int(input("enter account pin:"))
           acc_presence=False
           for acc in acclist:
               if acc["pin"]==acc_pin and acc["account no"]==acc_no:
                   acc_presence=True
                   ch=None
                   while ch!=7:
                    print(" enter 1 to withdraw")
                    print("enter 2 to deposit")
                    print("enter 3 to transfer")
                    print("enter 4 to view balance")
                    print("enter 5  to pay bill")
                    print("enter 6 to view transactions")
                    print("enter 7 to exit")
                    ch=int(input(""))
                    match ch:
                        case 1:
                            amount=int(input("enter amount:"))
                            if amount<=acc["balance"]:
                             acc["balance"]-=amount
                             tid+=1
                             t={"account no":acc["account no"],"amount":amount,"Type":"withdrawal","TID":tid}
                             transaction.append(t)
                             print("funds withdrawal successfull")
                            else:
                                print("Insufficient funds")
                        case 2:
                            amount=int(input("enter the amount to deposit:"))
                            acc["balance"]+=amount
                            tid += 1
                            t = {"account no": acc["account no"], "amount": amount, "Type": "deposition", "TID": tid}
                            transaction.append(t)
                            print(" funds successfully deposited")
                        case 3:
                            rec_acc_no=int(input("enter recievers accno:"))
                            rec_acc_presence=False
                            for ac1 in acclist:
                                if ac1["account no"]==rec_acc_no:
                                    rec_acc_presence=True
                                    amount=int(input("enter the amount to transfer: "))
                                    acc["balance"]-=amount
                                    ac1["balance"]+=amount
                                    tid += 1
                                    t = {"account no": acc["account no"],"rec account no":ac1["account no"], "amount": amount, "Type": "transfer",
                                         "TID": tid}
                                    transaction.append(t)


                                    print(" funds successfully transferred")
                            if rec_acc_presence==False:
                                print(" account not found")
                        case 4:
                            print(f"BALANCE:{acc['balance']}")
                        case 5:
                            print(" press 1 to pay lesco:")
                            print("press 2 to pay PTCL")
                            print("press 3 to pay SNGPL")
                            inp1=int(input(""))
                            match inp1:
                                case 1:
                                    reference=int(input("enter reference:"))
                                    amount=int(input("enter amount to pay:"))
                                    ref_ac1_presence=False
                                    for ac1 in acclist:

                                        if ac1["account no"]==reference:
                                            ref_ac1_presence=True
                                            amount=int(input("enter the amount to pay:"))
                                            if amount<=acc["balance"]:
                                                acc["balance"]-=amount
                                                ac1["balance"]+=amount
                                                tid += 1
                                                tid += 1
                                                t = {"account no": acc["account no"],
                                                     "rec account no": ac1["account no"], "amount": amount,
                                                     "Type": "transfer",
                                                     "TID": tid}
                                                transaction.append(t)
                                                print(" Bill paid successfully")

                                    if ref_ac1_presence==False:
                                        print(" account not found")
                                case 2:
                                    pno=int(input("enter pno:"))
                                    for ac1 in acclist:
                                        pno_presence=False
                                        if ac1["account no"]==pno:
                                            pno_presence=True
                                            amount=int(input("enter the amount to pay:"))
                                            if amount<=acc["balance"]:
                                                acc["balance"]-=amount
                                                ac1["balance"]+=amount
                                                tid += 1
                                                t = {"account no": acc["account no"],
                                                     "rec account no": ac1["account no"], "amount": amount,
                                                     "Type": "transfer",
                                                     "TID": tid}
                                                transaction.append(t)
                                                print(" Bill paid successfully")
                                            else:
                                                print("Insufficient funds")
                                    if pno_presence==False:
                                        print(" account not found")
                                case 3:
                                    sngpl=int(input("enter SNGPL id:"))
                                    sngpl_presence=False
                                    for ac1 in acclist:
                                        if ac1["account no"]==sngpl:
                                            sngpl_presence=True
                                            amount=int(input("enter the amount to pay:"))
                                            if amount<=ac1["balance"]:
                                                ac1["balance"]+=amount
                                                acc["balance"]-=amount
                                                tid += 1
                                                t = {"account no": acc["account no"],
                                                     "rec account no": ac1["account no"], "amount": amount,
                                                     "Type": "transfer",
                                                     "TID": tid}
                                                transaction.append(t)
                                                print("Bill paid successfully")
                                    if sngpl_presence==False:
                                      print("account no found")
                        case 6:
                            for t in transaction:
                                if t["account no"]==acc["account no"] or t["rec account no"]==acc["account no"]:
                                    if t["Type"]=="transfer":
                                        print(f" \n TID :{t["TID"]} \n amount :{t["amount"]}  \n type :{t["Type"]}  \n Receiver account no:{t["rec account no"]}",end="")
                                        for ac1 in acclist:
                                            if ac1["account no"]==t["rec account no"]:
                                                print(f", Reciever Name : {ac1["name"]}")

                                    else :
                                        print(f" \n TID :{t["TID"]} \n amount :{t["amount"]}  \n type :{t["Type"]}"  )








                        case _:
                            print("invalid input")












           if acc_presence==False:
               print("account doesnot exist")


       else:
           break


main()








