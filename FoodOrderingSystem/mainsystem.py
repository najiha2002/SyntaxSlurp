from tkinter import *
from tkinter import messagebox
import random

# constants
sellerA = 'Western Fiesta'
sellerB = 'Manis Dessert'
sellerC = 'Kampung Malaysia'

codesellerA = "WF"
codesellerB = "MD"
codesellerC = "KM"

# ========== Classes which are classified as Pages/Windows ===========  #

class Customer:
    def __init__(self, cust_menu):
        self.cust_menu = cust_menu

        cust_menu.geometry("1350x720")
        cust_menu.configure(bg="#127782")
        cust_menu.title("Syntax Slurp")
        title = Label(cust_menu, text="Syntax Slurp", bd=12, relief=RIDGE, font=("Arial Black", 20), bg="#0C89A5",
                      fg="white").pack(fill=X)

        # Variables
        cust_menu.foodA1 = IntVar()
        cust_menu.foodA2 = IntVar()
        cust_menu.foodA3 = IntVar()
        cust_menu.foodA4 = IntVar()
        cust_menu.foodA5 = IntVar()
        cust_menu.foodA6 = IntVar()
        cust_menu.foodA7 = IntVar()
        cust_menu.foodA8 = IntVar()

        cust_menu.foodB1 = IntVar()
        cust_menu.foodB2 = IntVar()
        cust_menu.foodB3 = IntVar()
        cust_menu.foodB4 = IntVar()
        cust_menu.foodB5 = IntVar()
        cust_menu.foodB6 = IntVar()
        cust_menu.foodB7 = IntVar()
        cust_menu.foodB8 = IntVar()

        cust_menu.foodC1 = IntVar()
        cust_menu.foodC2 = IntVar()
        cust_menu.foodC3 = IntVar()
        cust_menu.foodC4 = IntVar()
        cust_menu.foodC5 = IntVar()
        cust_menu.foodC6 = IntVar()
        cust_menu.foodC7 = IntVar()
        cust_menu.foodC8 = IntVar()

        cust_menu.total_priceA = StringVar()
        cust_menu.total_priceB = StringVar()
        cust_menu.total_priceC = StringVar()
        cust_menu.total_price = StringVar()
        cust_menu.total_tax = StringVar()
        cust_menu.a = StringVar()
        cust_menu.b = StringVar()
        cust_menu.c = StringVar()
        cust_menu.c_name = StringVar()
        cust_menu.address = StringVar()
        cust_menu.bill_num = StringVar()
        x = random.randint(1000, 9999)
        cust_menu.bill_num.set(str(x))
        cust_menu.phone = StringVar()

        # Customer details label frame
        details = LabelFrame(cust_menu, text="Customer Details", font=("Arial Black", 12), bg="#0C89A5", fg="white",
                             relief=GROOVE, bd=10)
        details.place(x=0, y=80, relwidth=1)

        cust_name = Label(details, text="Customer Name", font=("Arial Black", 14), bg="#0C89A5", fg="white").grid(row=0,
                                                                                                                  column=0,
                                                                                                                  padx=15)
        cust_entry = Entry(details, borderwidth=4, width=30, textvariable=cust_menu.c_name).grid(row=0, column=1,
                                                                                                 padx=8)

        contact_name = Label(details, text="Contact No.", font=("Arial Black", 14), bg="#0C89A5", fg="white").grid(
            row=0,
            column=2,
            padx=10)
        contact_entry = Entry(details, borderwidth=4, width=30, textvariable=cust_menu.phone).grid(row=0, column=3,
                                                                                                   padx=8)

        bill_name = Label(details, text="Bill No.", font=("Arial Black", 14), bg="#0C89A5", fg="white").grid(row=0,
                                                                                                             column=4,
                                                                                                             padx=10)
        bill_entry = Entry(details, borderwidth=4, width=30, textvariable=cust_menu.bill_num).grid(row=0, column=5,
                                                                                                   padx=8)

        address_name = Label(details, text="Address", font=("Arial Black", 14), bg="#0C89A5", fg="white").grid(
            row=1, column=0, padx=15)

        address_entry = Entry(details, borderwidth=4, width=30, textvariable=cust_menu.address).grid(row=1, column=1,
                                                                                                     padx=8)

        # Label Frame 1
        foodA = LabelFrame(cust_menu, text="Western Fiesta", font=("Arial Black", 12), bg="#9AD5E7", fg="#127782",
                           relief=GROOVE,
                           bd=10)
        foodA.place(x=5, y=180, height=380, width=325)

        food_listA = []
        with open('itemslistA.txt') as A:
            for line in A:
                food_listA.append(line.strip().split(":"))
        A.close()

        if len(food_listA) >= 1:
            food1 = Label(foodA, text=food_listA[0][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=0, column=0,
                pady=11)
            food1_price = Label(foodA, text=f"RM {food_listA[0][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=0, column=1,
                                                   padx=15)
            food1_entry = Entry(foodA, borderwidth=2, width=5, textvariable=cust_menu.foodA1).grid(row=0, column=2,
                                                                                                   padx=10)

        if len(food_listA) >= 2:
            food2 = Label(foodA, text=food_listA[1][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=1, column=0,
                pady=11)
            food2_price = Label(foodA, text=f"RM {food_listA[1][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=1, column=1, padx=15)
            food2_entry = Entry(foodA, borderwidth=2, width=5, textvariable=cust_menu.foodA2).grid(row=1, column=2,
                                                                                                   padx=10)

        if len(food_listA) >= 3:
            food3 = Label(foodA, text=food_listA[2][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=2, column=0,
                pady=11)
            food3_price = Label(foodA, text=f"RM {food_listA[2][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=2, column=1, padx=15)
            food3_entry = Entry(foodA, borderwidth=2, width=5, textvariable=cust_menu.foodA3).grid(row=2, column=2,
                                                                                                   padx=10)

        if len(food_listA) >= 4:
            food4 = Label(foodA, text=food_listA[3][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=3, column=0,
                pady=11)
            food4_price = Label(foodA, text=f"RM {food_listA[3][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=3, column=1, padx=15)
            food4_entry = Entry(foodA, borderwidth=2, width=5, textvariable=cust_menu.foodA4).grid(row=3, column=2,
                                                                                                   padx=10)

        if len(food_listA) >= 5:
            food5 = Label(foodA, text=food_listA[4][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=4, column=0,
                pady=11)
            food5_price = Label(foodA, text=f"RM {food_listA[4][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=4, column=1, padx=15)
            food5_entry = Entry(foodA, borderwidth=2, width=5, textvariable=cust_menu.foodA5).grid(row=4, column=2,
                                                                                                   padx=10)

        if len(food_listA) >= 6:
            food6 = Label(foodA, text=food_listA[5][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=5, column=0,
                pady=11)
            food6_price = Label(foodA, text=f"RM {food_listA[5][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=5, column=1, padx=15)
            food6_entry = Entry(foodA, borderwidth=2, width=5, textvariable=cust_menu.foodA6).grid(row=5, column=2,
                                                                                                   padx=10)

        if len(food_listA) >= 7:
            food7 = Label(foodA, text=food_listA[6][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=6, column=0,
                pady=11)
            food7_price = Label(foodA, text=f"RM {food_listA[6][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=6, column=1, padx=15)
            food7_entry = Entry(foodA, borderwidth=2, width=5, textvariable=cust_menu.foodA7).grid(row=6, column=2,
                                                                                                   padx=10)

        if len(food_listA) >= 8:
            food8 = Label(foodA, text=food_listA[7][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=7, column=0,
                pady=11)
            food8_price = Label(foodA, text=f"RM {food_listA[7][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=7, column=1, padx=15)
            food8_entry = Entry(foodA, borderwidth=2, width=5, textvariable=cust_menu.foodA8).grid(row=7, column=2,
                                                                                                   padx=10)

        # Seller B
        foodB = LabelFrame(cust_menu, text="Manis Dessert", font=("Arial Black", 12), relief=GROOVE, bd=10,
                           bg="#9AD5E7",
                           fg="#127782")
        foodB.place(x=337, y=180, height=380, width=325)

        food_listB = []
        with open('itemslistB.txt') as B:
            for line in B:
                food_listB.append(line.strip().split(":"))
        B.close()

        if len(food_listB) >= 1:
            food1 = Label(foodB, text=food_listB[0][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=0, column=0,
                pady=11)
            food1_price = Label(foodB, text=f"RM {food_listB[0][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=0, column=1,
                                                   padx=15)
            food1_entry = Entry(foodB, borderwidth=2, width=5, textvariable=cust_menu.foodB1).grid(row=0, column=2,
                                                                                                   padx=10)

        if len(food_listB) >= 2:
            food2 = Label(foodB, text=food_listB[1][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=1, column=0,
                pady=11)
            food2_price = Label(foodB, text=f"RM {food_listB[1][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=1, column=1, padx=15)
            food2_entry = Entry(foodB, borderwidth=2, width=5, textvariable=cust_menu.foodB2).grid(row=1, column=2,
                                                                                                   padx=10)

        if len(food_listB) >= 3:
            food3 = Label(foodB, text=food_listB[2][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=2, column=0,
                pady=11)
            food3_price = Label(foodB, text=f"RM {food_listB[2][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=2, column=1, padx=15)
            food3_entry = Entry(foodB, borderwidth=2, width=5, textvariable=cust_menu.foodB3).grid(row=2, column=2,
                                                                                                   padx=10)

        if len(food_listB) >= 4:
            food4 = Label(foodB, text=food_listB[3][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=3, column=0,
                pady=11)
            food4_price = Label(foodB, text=f"RM {food_listB[3][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=3, column=1, padx=15)
            food4_entry = Entry(foodB, borderwidth=2, width=5, textvariable=cust_menu.foodB4).grid(row=3, column=2,
                                                                                                   padx=10)

        if len(food_listB) >= 5:
            food5 = Label(foodB, text=food_listB[4][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=4, column=0,
                pady=11)
            food5_price = Label(foodB, text=f"RM {food_listB[4][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=4, column=1, padx=15)
            food5_entry = Entry(foodB, borderwidth=2, width=5, textvariable=cust_menu.foodB5).grid(row=4, column=2,
                                                                                                   padx=10)

        if len(food_listB) >= 6:
            food6 = Label(foodB, text=food_listB[5][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=5, column=0,
                pady=11)
            food6_price = Label(foodB, text=f"RM {food_listB[5][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=5, column=1, padx=15)
            food6_entry = Entry(foodB, borderwidth=2, width=5, textvariable=cust_menu.foodB6).grid(row=5, column=2,
                                                                                                   padx=10)

        if len(food_listB) >= 7:
            food7 = Label(foodB, text=food_listB[6][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=6, column=0,
                pady=11)
            food7_price = Label(foodB, text=f"RM {food_listB[6][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=6, column=1, padx=15)
            food7_entry = Entry(foodB, borderwidth=2, width=5, textvariable=cust_menu.foodB7).grid(row=6, column=2,
                                                                                                   padx=10)

        if len(food_listB) >= 8:
            food8 = Label(foodB, text=food_listB[7][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=7, column=0,
                pady=11)
            food8_price = Label(foodB, text=f"RM {food_listB[7][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=7, column=1, padx=15)
            food8_entry = Entry(foodB, borderwidth=2, width=5, textvariable=cust_menu.foodB8).grid(row=7, column=2,
                                                                                                   padx=10)

        # Seller C
        foodC = LabelFrame(cust_menu, text="Kampung Malaysia", font=("Arial Black", 12), relief=GROOVE, bd=10,
                           bg="#9AD5E7",
                           fg="#127782")
        foodC.place(x=670, y=180, height=380, width=325)

        food_listC = []
        with open('itemslistC.txt') as C:
            for line in C:
                food_listC.append(line.strip().split(":"))
        C.close()

        if len(food_listC) >= 1:
            food1 = Label(foodC, text=food_listC[0][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=0, column=0,
                pady=11)
            food1_price = Label(foodC, text=f"RM {food_listC[0][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=0, column=1,
                                                   padx=15)
            food1_entry = Entry(foodC, borderwidth=2, width=5, textvariable=cust_menu.foodC1).grid(row=0, column=2,
                                                                                                   padx=10)

        if len(food_listC) >= 2:
            food2 = Label(foodC, text=food_listC[1][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=1, column=0,
                pady=11)
            food2_price = Label(foodC, text=f"RM {food_listC[1][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=1, column=1, padx=15)
            food2_entry = Entry(foodC, borderwidth=2, width=5, textvariable=cust_menu.foodC2).grid(row=1, column=2,
                                                                                                   padx=10)

        if len(food_listC) >= 3:
            food3 = Label(foodC, text=food_listC[2][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=2, column=0,
                pady=11)
            food3_price = Label(foodC, text=f"RM {food_listC[2][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=2, column=1, padx=15)
            food3_entry = Entry(foodC, borderwidth=2, width=5, textvariable=cust_menu.foodC3).grid(row=2, column=2,
                                                                                                   padx=10)

        if len(food_listC) >= 4:
            food4 = Label(foodC, text=food_listC[3][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=3, column=0,
                pady=11)
            food4_price = Label(foodC, text=f"RM {food_listC[3][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=3, column=1, padx=15)
            food4_entry = Entry(foodC, borderwidth=2, width=5, textvariable=cust_menu.foodC4).grid(row=3, column=2,
                                                                                                   padx=10)

        if len(food_listC) >= 5:
            food5 = Label(foodC, text=food_listC[4][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=4, column=0,
                pady=11)
            food5_price = Label(foodC, text=f"RM {food_listC[4][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=4, column=1, padx=15)
            food5_entry = Entry(foodC, borderwidth=2, width=5, textvariable=cust_menu.foodC5).grid(row=4, column=2,
                                                                                                   padx=10)

        if len(food_listC) >= 6:
            food6 = Label(foodC, text=food_listC[5][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=5, column=0,
                pady=11)
            food6_price = Label(foodC, text=f"RM {food_listC[5][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=5, column=1, padx=15)
            food6_entry = Entry(foodC, borderwidth=2, width=5, textvariable=cust_menu.foodC6).grid(row=5, column=2,
                                                                                                   padx=10)

        if len(food_listC) >= 7:
            food7 = Label(foodC, text=food_listC[6][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=6, column=0,
                pady=11)
            food7_price = Label(foodC, text=f"RM {food_listC[6][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=6, column=1, padx=15)
            food7_entry = Entry(foodC, borderwidth=2, width=5, textvariable=cust_menu.foodC7).grid(row=6, column=2,
                                                                                                   padx=10)

        if len(food_listC) >= 8:
            food8 = Label(foodC, text=food_listC[7][0], font=("Arial Black", 11), bg="#9AD5E7", fg="#127782").grid(
                row=7, column=0,
                pady=11)
            food8_price = Label(foodC, text=f"RM {food_listC[7][1]}", font=("Arial Black", 11), bg="#9AD5E7",
                                fg="#127782").grid(row=7, column=1, padx=15)
            food8_entry = Entry(foodC, borderwidth=2, width=5, textvariable=cust_menu.foodC8).grid(row=7, column=2,
                                                                                                   padx=10)

        # receipt
        receipt = Frame(cust_menu, bd=10, relief=GROOVE, bg="#9AD5E7")
        receipt.place(x=1010, y=188, width=330, height=372)

        receipt_title = Label(receipt, text="Receipt", font=("Arial Black", 17), bd=7, relief=GROOVE, bg="#9AD5E7",
                              fg="#127782").pack(fill=X)

        scroll_y = Scrollbar(receipt, orient=VERTICAL)
        cust_menu.txtarea = Text(receipt, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=cust_menu.txtarea.yview)
        cust_menu.txtarea.pack(fill=BOTH, expand=1)

        # Receipt Details
        receipt_details = LabelFrame(cust_menu, text="Order Summary", font=("Arial Black", 12), relief=GROOVE, bd=10,
                                     bg="#0C89A5", fg="white")
        receipt_details.place(x=0, y=560, relwidth=1, height=155)

        total_foodA = Label(receipt_details, text="Total Western Fiesta", font=("Arial Black", 11), bg="#0C89A5",
                            fg="white").grid(
            row=0, column=0)
        total_foodA_entry = Entry(receipt_details, width=15, borderwidth=2, textvariable=cust_menu.total_priceA).grid(
            row=0, column=1, padx=10,
            pady=7)

        tax_foodA = Label(receipt_details, text="Tax Western Fiesta", font=("Arial Black", 11), bg="#0C89A5",
                          fg="white").grid(row=1,
                                           column=0)
        tax_foodA_entry = Entry(receipt_details, width=15, borderwidth=2, textvariable=cust_menu.a).grid(row=1,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=7)
        total_foodB = Label(receipt_details, text="Total Manis Dessert", font=("Arial Black", 11), bg="#0C89A5",
                            fg="white").grid(row=0, column=2)
        total_foodB_entry = Entry(receipt_details, width=15, borderwidth=2, textvariable=cust_menu.total_priceB).grid(
            row=0,
            column=3,
            padx=10,
            pady=7)
        tax_foodB = Label(receipt_details, text="Tax Manis Dessert", font=("Arial Black", 11), bg="#0C89A5",
                          fg="white").grid(row=1, column=2)
        tax_foodB_entry = Entry(receipt_details, width=15, borderwidth=2, textvariable=cust_menu.b).grid(row=1,
                                                                                                         column=3,
                                                                                                         padx=10,
                                                                                                         pady=7)

        total_foodC = Label(receipt_details, text="Total Kampung Malaysia ", font=("Arial Black", 11), bg="#0C89A5",
                            fg="white").grid(row=0, column=5)
        total_foodC_entry = Entry(receipt_details, width=15, borderwidth=2, textvariable=cust_menu.total_priceC).grid(
            row=0,
            column=6,
            padx=10,
            pady=7)
        tax_foodC = Label(receipt_details, text="Tax Kampung Malaysia", font=("Arial Black", 11), bg="#0C89A5",
                          fg="white").grid(row=1, column=5)
        tax_foodB_entry = Entry(receipt_details, width=15, borderwidth=2, textvariable=cust_menu.c).grid(row=1,
                                                                                                         column=6,
                                                                                                         padx=10,
                                                                                                         pady=7)

        button_frame = Frame(receipt_details, bd=6, relief=GROOVE, bg="#0C89A5")
        button_frame.place(x=900, width=425, height=95)
        button_total = Button(button_frame, text="Total Price", font=("Arial Black", 15), pady=10, bg="white",
                              fg="#127782",
                              command=lambda: total(cust_menu)).grid(row=0, column=0, padx=5)
        button_clear = Button(button_frame, text="Clear Field", font=("Arial Black", 15), pady=10, bg="white",
                              fg="#127782",
                              command=lambda: clear(cust_menu)).grid(row=0, column=1, padx=5, pady=6)
        button_proceed = Button(button_frame, text="Proceed", font=("Arial Black", 15), pady=10, bg="white",
                                fg="#127782", width=8, command=lambda: open_Payment(cust_menu)).grid(row=0, column=2, padx=5,
                                                                                                pady=6)

        intro(cust_menu)

class Payment(Customer):
    def __init__(self, cust_menu, payment):
        super().__init__(cust_menu)

        self.payment = payment
        payment.custname = StringVar()

        payment.geometry("700x600")
        payment.configure(bg="#127782")

        # payment.customerName = StringVar()
        # Window payment label
        title = Label(payment, text="Payment", bd=12, relief=RIDGE, font=("Arial Black", 20), bg="#0C89A5",
                      fg="white").pack(fill=X)

        # Customer info frame
        customer_frame = Frame(payment, bd=7, relief=GROOVE, bg="#0C89A5")
        customer_frame.place(x=0, y=100, width=600, height=400)
        customer_frame.pack(padx=10, pady=10)

        # Ask for customer's name
        Name = Label(customer_frame, text="Enter name: ", font=("Arial Black", 14), bg="#0C89A5",
                     fg="white")
        Name.grid(row=1, column=13, padx=25, pady=25)

        # Enter customer name
        customerName = Entry(customer_frame, borderwidth=4, width=30, textvariable=payment.custname)
        customerName.grid(row=1, column=14, padx=25, pady=25)

        # Total price label
        Total = Label(customer_frame, text="Your total: ", font=("Arial Black", 14), bg="#0C89A5", fg="white")
        Total.grid(row=3, column=13, padx=25, pady=25)

        # Display total price
        price = Label(customer_frame, text=str_total, font=("Arial Black", 14), bg="#0C89A5",
                      fg="white")  # adjust dkt text = "RM25"
        price.grid(row=3, column=14, padx=25, pady=25)

        # Declare variable clicked
        clicked = StringVar()

        # Payment method label
        Pay = Label(customer_frame, text="Choose payment method: ", font=("Arial Black", 14), bg="#0C89A5", fg="white")
        Pay.grid(row=4, column=13, padx=25, pady=25)

        # Payment method list
        method = ["Debit/Credit", "Online Banking", "COD"]
        clicked.set(method[0])

        # Creating drop down for payment method
        drop = OptionMenu(customer_frame, clicked, *method)
        drop.config(font=("Arial", 13))
        drop.grid(row=4, column=14, padx=25, pady=25)

        # Function for message box
        def message_box():
            if payment.custname.get() == "":
                messagebox.showerror("Error", "Please enter your name first.")
            else:
                messagebox.showinfo("Done!", "Your food has been paid. Enjoy your meal!")

        # Creating a button Pay and display message box
        buttonPay = Button(customer_frame, text="Pay Now", command=message_box, font=("Arial Black", 14))
        buttonPay.grid(row=5, column=14, padx=25, pady=25)

class Seller:
    def __init__(self, sellerlogin_screen):

        self.sellerlogin_screen = sellerlogin_screen

        sellerlogin_screen.username_verify = StringVar()
        sellerlogin_screen.password_verify = StringVar()

        sellerlogin_screen.title("Login")
        sellerlogin_screen.geometry("500x350")
        sellerlogin_screen.configure(bg="#127782")

        Label(sellerlogin_screen, text="Please enter details below to login", width="300", height="2", bd=12,
              relief=RIDGE,
              font=("Arial Black", 14), bg="powder blue", fg="black").pack()
        Label(sellerlogin_screen, text="Seller Name * ", font=("Arial Black", 10), width="20",
              fg="white", bg="#127782").place(x=165, y=120)
        username_login_entry = Entry(sellerlogin_screen, textvariable=sellerlogin_screen.username_verify,
                                     font=("Calibri", 10), width=30)
        username_login_entry.place(x=150, y=150)
        Label(sellerlogin_screen, text="Password * ", font=("Arial Black", 10), fg="white",
              width="20", bg="#127782").place(x=165, y=180)
        password_login_entry = Entry(sellerlogin_screen, textvariable=sellerlogin_screen.password_verify,
                                     font=("Calibri", 10), width=30, show='*')
        password_login_entry.place(x=150, y=210)
        loginButton = Button(sellerlogin_screen, text="Login", width=10, height=1, command=lambda: login_verify(sellerlogin_screen), font=("Arial Black", 12),
               bg="turquoise", fg="black").place(x=195, y=260)

class SeeOrder(Seller):
    def __init__(self, sellerlogin_screen, see_order):
        super().__init__(sellerlogin_screen)

        self.see_order = see_order

        see_order.geometry("500x620")
        see_order.configure(bg="#127782")
        see_order.title("Track Orders")
        title = Label(see_order, text="Syntax Slurp", bd=12, relief=RIDGE, font=("Arial Black", 20),
                      bg="#0C89A5",fg="white").pack(fill=X)

        see_order.s_name = StringVar()

        details = LabelFrame(see_order, text="Orders", font=("Arial Black", 12), bg="#0C89A5", fg="white",
                             relief=GROOVE, bd=10)
        details.place(x=0, y=80, relwidth=1)

        seller_name = Label(details, text="Seller Name", font=("Arial Black", 14), bg="#0C89A5", fg="white").grid(row=0,
                                                                                                                  column=0,
                                                                                                                  padx=15)
        seller_entry = Entry(details, borderwidth=4, width=30, textvariable=see_order.s_name).grid(row=0, column=1,
                                                                                                 padx=8)

        # receipt
        receipt = Frame(see_order, bd=10, relief=GROOVE, bg="#9AD5E7")
        receipt.place(x=45, y=150, width=400, height=372)

        receipt_title = Label(receipt, text="Receipt", font=("Arial Black", 17), bd=7, relief=GROOVE, bg="#9AD5E7",
                              fg="#127782").pack(fill=X)

        scroll_y = Scrollbar(receipt, orient=VERTICAL)
        see_order.txtarea = Text(receipt, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=see_order.txtarea.yview)
        see_order.txtarea.pack(fill=BOTH, expand=1)


        button_frame = Frame(see_order, bd=6, relief=GROOVE, bg="#0C89A5")
        button_frame.place(x=170, y=530, width=150, height=70)
        button_total = Button(button_frame, text="See Orders", font=("Arial Black", 15), pady=10, bg="white",
                              fg="#127782",
                              command=lambda: display_orders(see_order)).grid(row=0, column=0, padx=5)

class AddItem(Seller):
    def __init__(self, sellerlogin_screen, sellerAD):
        super().__init__(sellerlogin_screen)
        self.sellerAD = sellerAD

        sellerAD.geometry("550x600")
        sellerAD.configure(bg="#127782")
        sellerAD.title("Syntax Slurp")
        sellerAD_title = Label(sellerAD, text="Seller Add Item", bd=12, relief=RIDGE, font=("Arial Black", 20), bg="#0C89A5",
                               fg="white").pack(fill=X)

        # Variables
        sellerAD.s_name = StringVar()
        sellerAD.item_name = StringVar()
        sellerAD.item_price = DoubleVar()

        # Seller Add Item details label frame

        sellerName_frame = Frame(sellerAD, bd=7, relief=GROOVE, bg="#0C89A5")
        sellerName_frame.place(x=90, y=160, width=350, height=50)
        seller_name = Label(sellerName_frame, text="Seller Name", font=("Arial Black", 14), bg="#0C89A5",
                            fg="white").grid(row=0, column=0, padx=2)
        sellerName_entry = Entry(sellerName_frame, borderwidth=4, width=20, textvariable=sellerAD.s_name).grid(row=0,
                                                                                                               column=1,
                                                                                                               padx=8)

        sellerItem_frame = Frame(sellerAD, bd=7, relief=GROOVE, bg="#0C89A5")
        sellerItem_frame.place(x=90, y=230, width=350, height=50)
        seller_item = Label(sellerItem_frame, text="Item", font=("Arial Black", 14), bg="#0C89A5", fg="white").grid(
            row=0, column=0, padx=10)
        sellerItem_entry = Entry(sellerItem_frame, borderwidth=4, width=25, textvariable=sellerAD.item_name).grid(row=0,
                                                                                                                  column=1,
                                                                                                                  padx=8)

        sellerPrice_frame = Frame(sellerAD, bd=7, relief=GROOVE, bg="#0C89A5")
        sellerPrice_frame.place(x=90, y=300, width=350, height=50)
        seller_price = Label(sellerPrice_frame, text="Price", font=("Arial Black", 14), bg="#0C89A5", fg="white").grid(
            row=0, column=0, padx=10)
        sellerPrice_entry = Entry(sellerPrice_frame, borderwidth=4, width=25, textvariable=sellerAD.item_price).grid(
            row=0,
            column=1,
            padx=8)
        addItem_frame = Frame(sellerAD, bd=7, relief=GROOVE, bg="#0C89A5")
        addItem_frame.place(x=200, y=410, width=134, height=81)
        add_item_submit = Button(addItem_frame, text="Add Item", font=("Arial Black", 15), pady=10, bg="white",
                                 fg="#127782", command=lambda: add_item(sellerAD)).grid(row=0, column=0)

class SellerMenu(Seller):
    def __init__(self, sellerlogin_screen, sellermenu):
        super().__init__(sellerlogin_screen)

        self.sellermenu = sellermenu

        sellermenu.geometry("500x400")
        sellermenu.configure(bg="#127782")
        sellermenu.title("Syntax Slurp")

        sellermenu.customerName = StringVar()
        title = Label(sellermenu, text="Seller Menu", bd=12, relief=RIDGE, font=("Arial Black", 20), bg="#0C89A5",
                      fg="white").pack(fill=X)

        seller_frame = Frame(sellermenu, bd=7, relief=GROOVE, bg="#0C89A5")
        seller_frame.place(x=25, y=80, width=450, height=300)

        addItem_Button = Button(seller_frame, text="Add Item", font=("Arial Black", 15), padx=48, pady=30, bg="#127782",
                                fg="#127782", command=lambda: open_Seller_AddItem(sellerlogin_screen)).place(relx=0.5, rely=0.4, anchor=S)
        seeOrders_Button = Button(seller_frame, text="See Orders", font=("Arial Black", 15), padx=40, pady=30,
                                  bg="#127782", fg="#127782", command=lambda: open_Seller_SeeOrder(sellerlogin_screen)).place(relx=0.5, rely=0.5, anchor=N)


# ========== Functions ===========  #

def display_orders(see_order):
    if see_order.s_name.get() == "":
        messagebox.showerror("Error", "Fill in Seller Name")

    see_order.txtarea.delete(1.0, END)

    if see_order.s_name.get() == codesellerA:
        see_order.txtarea.insert(END, f"\tORDERS: Western Fiesta\n\n")

        order_listA = []
        with open('ordersA.txt') as A:
            for line in A:
                order_listA.append(line.strip().split("/"))
        A.close()

        for i in range(0, len(order_listA)):
            see_order.txtarea.insert(END, f"Name\t: {order_listA[i][0]}\n")
            see_order.txtarea.insert(END, f"Address\t: {order_listA[i][1]}\n")
            see_order.txtarea.insert(END, f"Phone No.: {order_listA[i][2]}\n")
            see_order.txtarea.insert(END, f"Orders\t: {order_listA[i][3]}\n")
            see_order.txtarea.insert(END, f"Total Price (exc. tax): {order_listA[i][4]}\n")
            see_order.txtarea.insert(END, "\n")

    elif see_order.s_name.get() == codesellerB:
        see_order.txtarea.insert(END, f"\tORDERS: Manis Dessert\n\n")
        order_listB = []
        with open('ordersB.txt') as B:
            for line in B:
                order_listB.append(line.strip().split("/"))
        B.close()

        for i in range (0,len(order_listB)):
            see_order.txtarea.insert(END, f"Name\t: {order_listB[i][0]}\n")
            see_order.txtarea.insert(END, f"Address\t: {order_listB[i][1]}\n")
            see_order.txtarea.insert(END, f"Phone No.: {order_listB[i][2]}\n")
            see_order.txtarea.insert(END, f"Orders\t: {order_listB[i][3]}\n")
            see_order.txtarea.insert(END, f"Total Price (exc. tax): {order_listB[i][4]}\n")
            see_order.txtarea.insert(END, "\n")

    elif see_order.s_name.get() == codesellerC:
        see_order.txtarea.insert(END, f"\tORDERS: Kampung Malaysia\n\n")
        order_listC = []
        with open('ordersC.txt') as C:
            for line in C:
                order_listC.append(line.strip().split("/"))
        C.close()

        for i in range (0, len(order_listC)):
            see_order.txtarea.insert(END, f"Name\t: {order_listC[i][0]}\n")
            see_order.txtarea.insert(END, f"Address\t: {order_listC[i][1]}\n")
            see_order.txtarea.insert(END, f"Phone No.: {order_listC[i][2]}\n")
            see_order.txtarea.insert(END, f"Orders\t: {order_listC[i][3]}\n")
            see_order.txtarea.insert(END, f"Total Price (exc. tax): {order_listC[i][4]}\n")
            see_order.txtarea.insert(END, "\n")

def intro(cust_menu):
    cust_menu.txtarea.delete(1.0, END)
    cust_menu.txtarea.insert(END, "\tWELCOME TO SYNTAX SLURP\n\tPhone-No.739275410")
    cust_menu.txtarea.insert(END, f"\n\nBill no. : {cust_menu.bill_num.get()}")
    cust_menu.txtarea.insert(END, f"\nCustomer Name : {cust_menu.c_name.get()}")
    cust_menu.txtarea.insert(END, f"\nPhone No. : {cust_menu.phone.get()}")
    cust_menu.txtarea.insert(END, f"\nAddress : {cust_menu.address.get()}")
    cust_menu.txtarea.insert(END, "\n====================================\n")
    cust_menu.txtarea.insert(END, "\nProduct\t\tQty\tPrice\n")
    cust_menu.txtarea.insert(END, "\n====================================\n")

def total(cust_menu):

    while True:
        if cust_menu.c_name.get() == "" or cust_menu.phone.get() == "" or cust_menu.address.get() == "":
            messagebox.showerror("Error", "Fill the complete Customer Details!!")
            break

        food_listA = []
        with open('itemslistA.txt') as A:
            for line in A:
                food_listA.append(line.strip().split(":"))
        A.close()

        total_foodA_price = 0
        if len(food_listA) >= 1:
            cust_menu.fooda1 = cust_menu.foodA1.get() * float(food_listA[0][1])
            total_foodA_price += cust_menu.fooda1
        if len(food_listA) >= 2:
            cust_menu.fooda2 = cust_menu.foodA2.get() * float(food_listA[1][1])
            total_foodA_price += cust_menu.fooda2
        if len(food_listA) >= 3:
            cust_menu.fooda3 = cust_menu.foodA3.get() * float(food_listA[2][1])
            total_foodA_price += cust_menu.fooda3
        if len(food_listA) >= 4:
            cust_menu.fooda4 = cust_menu.foodA4.get() * float(food_listA[3][1])
            total_foodA_price += cust_menu.fooda4
        if len(food_listA) >= 5:
            cust_menu.fooda5 = cust_menu.foodA5.get() * float(food_listA[4][1])
            total_foodA_price += cust_menu.fooda5
        if len(food_listA) >= 6:
            cust_menu.fooda6 = cust_menu.foodA6.get() * float(food_listA[5][1])
            total_foodA_price += cust_menu.fooda6
        if len(food_listA) >= 7:
            cust_menu.fooda7 = cust_menu.foodA7.get() * float(food_listA[6][1])
            total_foodA_price += cust_menu.fooda7
        if len(food_listA) >= 8:
            cust_menu.fooda8 = cust_menu.foodA8.get() * float(food_listA[7][1])
            total_foodA_price += cust_menu.fooda8

        cust_menu.total_priceA.set("RM " + str(total_foodA_price))
        cust_menu.a.set("RM " + str(round(total_foodA_price * 0.05, 3)))

        food_listB = []
        with open('itemslistB.txt') as B:
            for line in B:
                food_listB.append(line.strip().split(":"))
        B.close()

        total_foodB_price = 0
        if len(food_listB) >= 1:
            cust_menu.foodb1 = cust_menu.foodB1.get() * float(food_listB[0][1])
            total_foodB_price += cust_menu.foodb1
        if len(food_listB) >= 2:
            cust_menu.foodb2 = cust_menu.foodB2.get() * float(food_listB[1][1])
            total_foodB_price += cust_menu.foodb2
        if len(food_listB) >= 3:
            cust_menu.foodb3 = cust_menu.foodB3.get() * float(food_listB[2][1])
            total_foodB_price += cust_menu.foodb3
        if len(food_listB) >= 4:
            cust_menu.foodb4 = cust_menu.foodB4.get() * float(food_listB[3][1])
            total_foodB_price += cust_menu.foodb4
        if len(food_listB) >= 5:
            cust_menu.foodb5 = cust_menu.foodB5.get() * float(food_listB[4][1])
            total_foodB_price += cust_menu.foodb5
        if len(food_listB) >= 6:
            cust_menu.foodb6 = cust_menu.foodB6.get() * float(food_listB[5][1])
            total_foodB_price += cust_menu.foodb6
        if len(food_listB) >= 7:
            cust_menu.foodb7 = cust_menu.foodB7.get() * float(food_listB[6][1])
            total_foodB_price += cust_menu.foodb7
        if len(food_listB) >= 8:
            cust_menu.foodb8 = cust_menu.foodB8.get() * float(food_listB[7][1])
            total_foodB_price += cust_menu.foodb8

        cust_menu.total_priceB.set("RM " + str(total_foodB_price))
        cust_menu.b.set("RM " + str(round(total_foodB_price * 0.05, 3)))

        food_listC = []
        with open('itemslistC.txt') as C:
            for line in C:
                food_listC.append(line.strip().split(":"))
        C.close()

        total_foodC_price = 0
        if len(food_listC) >= 1:
            cust_menu.foodc1 = cust_menu.foodC1.get() * float(food_listC[0][1])
            total_foodC_price += cust_menu.foodc1
        if len(food_listC) >= 2:
            cust_menu.foodc2 = cust_menu.foodC2.get() * float(food_listC[1][1])
            total_foodC_price += cust_menu.foodc2
        if len(food_listC) >= 3:
            cust_menu.foodc3 = cust_menu.foodC3.get() * float(food_listC[2][1])
            total_foodC_price += cust_menu.foodc3
        if len(food_listC) >= 4:
            cust_menu.foodc4 = cust_menu.foodC4.get() * float(food_listC[3][1])
            total_foodC_price += cust_menu.foodc4
        if len(food_listC) >= 5:
            cust_menu.foodc5 = cust_menu.foodC5.get() * float(food_listC[4][1])
            total_foodC_price += cust_menu.foodc5
        if len(food_listC) >= 6:
            cust_menu.foodc6 = cust_menu.foodC6.get() * float(food_listC[5][1])
            total_foodC_price += cust_menu.foodc6
        if len(food_listC) >= 7:
            cust_menu.foodc7 = cust_menu.foodC7.get() * float(food_listC[6][1])
            total_foodC_price += cust_menu.foodc7
        if len(food_listC) >= 8:
            cust_menu.foodc8 = cust_menu.foodC8.get() * float(food_listC[7][1])
            total_foodC_price += cust_menu.foodc8

        cust_menu.total_priceC.set("RM " + str(total_foodC_price))
        cust_menu.c.set("RM " + str(round(total_foodC_price * 0.05, 3)))

        total_tax = (round(total_foodA_price * 0.05, 3)) + (round(total_foodB_price * 0.05, 3)) + (
            round(total_foodC_price * 0.05, 3))
        cust_menu.total_tax = ("RM " + str(total_tax))

        cust_menu.total_all_bill = (total_foodA_price +
                                    total_foodB_price +
                                    total_foodC_price +
                                    total_tax +
                                    5.00)

        cust_menu.total_all_bil = "RM " + str(cust_menu.total_all_bill)

        global str_total
        str_total = cust_menu.total_all_bil

        receiptdetails(cust_menu)

        break

def receiptdetails(cust_menu):
    intro(cust_menu)

    str_order = (cust_menu.c_name.get() + '/' +
                 cust_menu.address.get() + '/' +
                 cust_menu.phone.get() + '/')
    str_orderA = str_order
    str_orderB = str_order
    str_orderC = str_order

    food_listA = []
    with open('itemslistA.txt') as A:
        for line in A:
            food_listA.append(line.strip().split(":"))
    A.close()

    if cust_menu.foodA1.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listA[0][0]}\t\t {cust_menu.foodA1.get()}\t{cust_menu.fooda1}\n")
        str_orderA += food_listA[0][0] + ":" + str(cust_menu.foodA1.get()) + " "
    if cust_menu.foodA2.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listA[1][0]}\t\t {cust_menu.foodA2.get()}\t{cust_menu.fooda2}\n")
        str_orderA += food_listA[1][0] + ":" + str(cust_menu.foodA2.get()) + " "
    if cust_menu.foodA3.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listA[2][0]}\t\t {cust_menu.foodA3.get()}\t{cust_menu.fooda3}\n")
        str_orderA += food_listA[2][0] + ":" + str(cust_menu.foodA3.get()) + " "
    if cust_menu.foodA4.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listA[3][0]}\t\t {cust_menu.foodA4.get()}\t{cust_menu.fooda4}\n")
        str_orderA += food_listA[3][0] + ":" + str(cust_menu.foodA4.get()) + " "
    if cust_menu.foodA5.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listA[4][0]}\t\t {cust_menu.foodA5.get()}\t{cust_menu.fooda5}\n")
        str_orderA += food_listA[4][0] + ":" + str(cust_menu.foodA5.get()) + " "
    if cust_menu.foodA6.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listA[5][0]}\t\t {cust_menu.foodA6.get()}\t{cust_menu.fooda6}\n")
        str_orderA += food_listA[5][0] + ":" + str(cust_menu.foodA6.get()) + " "
    if cust_menu.foodA7.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listA[6][0]}\t\t {cust_menu.foodA7.get()}\t{cust_menu.fooda7}\n")
        str_orderA += food_listA[6][0] + ":" + str(cust_menu.foodA7.get()) + " "
    if cust_menu.foodA8.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listA[7][0]}\t\t {cust_menu.foodA8.get()}\t{cust_menu.fooda8}\n")
        str_orderA += food_listA[7][0] + ":" + str(cust_menu.foodA8.get()) + " "

    food_listB = []
    with open('itemslistB.txt') as B:
        for line in B:
            food_listB.append(line.strip().split(":"))
    B.close()

    if cust_menu.foodB1.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listB[0][0]}\t\t {cust_menu.foodB1.get()}\t{cust_menu.foodb1}\n")
        str_orderB += food_listB[0][0] + ":" + str(cust_menu.foodB1.get()) + " "
    if cust_menu.foodB2.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listB[1][0]}\t\t {cust_menu.foodB2.get()}\t{cust_menu.foodb2}\n")
        str_orderB += food_listB[1][0] + ":" + str(cust_menu.foodB2.get()) + " "
    if cust_menu.foodB3.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listB[2][0]}\t\t {cust_menu.foodB3.get()}\t{cust_menu.foodb3}\n")
        str_orderB += food_listB[2][0] + ":" + str(cust_menu.foodB3.get()) + " "
    if cust_menu.foodB4.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listB[3][0]}\t\t {cust_menu.foodB4.get()}\t{cust_menu.foodb4}\n")
        str_orderB += food_listB[3][0] + ":" + str(cust_menu.foodB4.get()) + " "
    if cust_menu.foodB5.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listB[4][0]}\t\t {cust_menu.foodB5.get()}\t{cust_menu.foodb5}\n")
        str_orderB += food_listB[4][0] + ":" + str(cust_menu.foodB5.get()) + " "
    if cust_menu.foodB6.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listB[5][0]}\t\t {cust_menu.foodB6.get()}\t{cust_menu.foodb6}\n")
        str_orderB += food_listB[5][0] + ":" + str(cust_menu.foodB6.get()) + " "
    if cust_menu.foodB7.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listB[6][0]}\t\t {cust_menu.foodB7.get()}\t{cust_menu.foodb7}\n")
        str_orderB += food_listB[6][0] + ":" + str(cust_menu.foodB7.get()) + " "
    if cust_menu.foodB8.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listB[7][0]}\t\t {cust_menu.foodB8.get()}\t{cust_menu.foodb8}\n")
        str_orderB += food_listB[7][0] + ":" + str(cust_menu.foodB8.get()) + " "

    food_listC = []
    with open('itemslistC.txt') as C:
        for line in C:
            food_listC.append(line.strip().split(":"))
    C.close()

    if cust_menu.foodC1.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listC[0][0]}\t\t {cust_menu.foodC1.get()}\t{cust_menu.foodc1}\n")
        str_orderC += food_listC[0][0] + ":" + str(cust_menu.foodC1.get()) + " "
    if cust_menu.foodC2.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listC[1][0]}\t\t {cust_menu.foodC2.get()}\t{cust_menu.foodc2}\n")
        str_orderC += food_listC[1][0] + ":" + str(cust_menu.foodC2.get()) + " "
    if cust_menu.foodC3.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listC[2][0]}\t\t {cust_menu.foodC3.get()}\t{cust_menu.foodc3}\n")
        str_orderC += food_listC[2][0] + ":" + str(cust_menu.foodC3.get()) + " "
    if cust_menu.foodC4.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listC[3][0]}\t\t {cust_menu.foodC4.get()}\t{cust_menu.foodc4}\n")
        str_orderC += food_listC[3][0] + ":" + str(cust_menu.foodC4.get()) + " "
    if cust_menu.foodC5.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listC[4][0]}\t\t {cust_menu.foodC5.get()}\t{cust_menu.foodc5}\n")
        str_orderC += food_listC[4][0] + ":" + str(cust_menu.foodC5.get()) + " "
    if cust_menu.foodC6.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listC[5][0]}\t\t {cust_menu.foodC6.get()}\t{cust_menu.foodc6}\n")
        str_orderC += food_listC[5][0] + ":" + str(cust_menu.foodC6.get()) + " "
    if cust_menu.foodC7.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listC[6][0]}\t\t {cust_menu.foodC7.get()}\t{cust_menu.foodc7}\n")
        str_orderC += food_listC[6][0] + ":" + str(cust_menu.foodC7.get()) + " "
    if cust_menu.foodC8.get() != 0:
        cust_menu.txtarea.insert(END, f"{food_listC[7][0]}\t\t {cust_menu.foodC8.get()}\t{cust_menu.foodc8}\n")
        str_orderC += food_listC[7][0] + ":" + str(cust_menu.foodC8.get()) + " "

    cust_menu.txtarea.insert(END, f"------------------------------------\n")
    if cust_menu.a.get() != "RM 0.0":
        cust_menu.txtarea.insert(END, f"Total Western Fiesta\t: {cust_menu.total_priceA.get()}\n")
        str_orderA += "/" + cust_menu.total_priceA.get()
        add_order('A', str_orderA)
    if cust_menu.b.get() != "RM 0.0":
        cust_menu.txtarea.insert(END, f"Total Manis Dessert\t: {cust_menu.total_priceB.get()}\n")
        str_orderB += "/" + cust_menu.total_priceB.get()
        add_order('B', str_orderB)
    if cust_menu.c.get() != "RM 0.0":
        cust_menu.txtarea.insert(END, f"Total Kampung Malaysia: {cust_menu.total_priceC.get()}\n")
        str_orderC += "/" + cust_menu.total_priceC.get()
        add_order('C', str_orderC)

    cust_menu.txtarea.insert(END, f"\nTotal Tax: {cust_menu.total_tax}\n")
    cust_menu.txtarea.insert(END, f"Delivery Charge : RM 5.0\n")
    cust_menu.txtarea.insert(END, f"Total Order Amount : {cust_menu.total_all_bil}\n")
    cust_menu.txtarea.insert(END, f"------------------------------------\n")

def add_order(seller, details):
    if seller == 'A':
        with open('ordersA.txt', 'a') as A:
            A.write(details)
            A.write("\n")
        A.close()
    elif seller == 'B':
        with open('ordersB.txt', 'a') as B:
            B.write(details)
            B.write("\n")
        B.close()
    elif seller == 'C':
        with open('ordersC.txt', 'a') as C:
            C.write(details)
            C.write("\n")
        C.close()

def clear(cust_menu):
    cust_menu.txtarea.delete(1.0, END)
    cust_menu.foodA1.set(0)
    cust_menu.foodA2.set(0)
    cust_menu.foodA3.set(0)
    cust_menu.foodA4.set(0)
    cust_menu.foodA5.set(0)
    cust_menu.foodA6.set(0)
    cust_menu.foodA7.set(0)
    cust_menu.foodA8.set(0)

    cust_menu.foodB1.set(0)
    cust_menu.foodB2.set(0)
    cust_menu.foodB3.set(0)
    cust_menu.foodB4.set(0)
    cust_menu.foodB5.set(0)
    cust_menu.foodB6.set(0)
    cust_menu.foodB7.set(0)
    cust_menu.foodB8.set(0)

    cust_menu.foodC1.set(0)
    cust_menu.foodC2.set(0)
    cust_menu.foodC3.set(0)
    cust_menu.foodC4.set(0)
    cust_menu.foodC5.set(0)
    cust_menu.foodC6.set(0)
    cust_menu.foodC7.set(0)
    cust_menu.foodC8.set(0)

    cust_menu.total_priceA.set(0)
    cust_menu.total_priceB.set(0)
    cust_menu.total_priceC.set(0)
    cust_menu.total_price.set(0)
    cust_menu.a.set(0)
    cust_menu.b.set(0)
    cust_menu.c.set(0)

def add_item(sellerAD):
    # Determine which seller belongs to each textfile

    str_additem = sellerAD.item_name.get()+ ":" + str(f"{sellerAD.item_price.get():.2f}")

    if sellerAD.s_name.get() == codesellerA:
        with open("itemslistA.txt", "a") as file:
            file.write("\n")
            file.write(str_additem)
        file.close()
    elif sellerAD.s_name.get() == codesellerB:
        with open("itemslistB.txt", "a") as file:
            file.write("\n")
            file.write(str_additem)
        file.close()
    elif sellerAD.s_name.get() == codesellerC:
        with open("itemslistC.txt", "a") as file:
            file.write("\n")
            file.write(str_additem)
        file.close()

    messagebox.showinfo("Seller Add Item", "ITEM ADDED!")

def login_verify(sellerlogin_screen):
    username1 = sellerlogin_screen.username_verify.get()
    password2 = sellerlogin_screen.password_verify.get()

    print(username1)

    if username1 == sellerA:
        if password2 == "wf123":
            login_sucess(sellerlogin_screen)
        else:
            password_not_recognised()
    elif username1 == sellerB:
        if password2 == "md123":
            login_sucess(sellerlogin_screen)
        else:
            password_not_recognised()
    elif username1 == sellerC:
        if password2 == "km123":
          login_sucess(sellerlogin_screen)
        else:
            password_not_recognised()
    else:
        user_not_found()

def login_sucess(sellerlogin_screen):
    global login_success_screen
    login_success_screen = Toplevel(main_menu)
    login_success_screen.title("Success")
    login_success_screen.geometry("200x200")
    login_success_screen.configure(bg="powder blue")
    Label(login_success_screen, text="Login Success!!", font=("Century", 10), bg="azure", fg="black").place(x=60, y=60)
    Button(login_success_screen, text="OK", bg="azure", command=lambda: delete_login_success(sellerlogin_screen)).place(x=85, y=110)

# Designing popup for login invalid password
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(main_menu)
    password_not_recog_screen.title("Error")
    password_not_recog_screen.geometry("200x200")
    password_not_recog_screen.configure(bg="powder blue")
    Label(password_not_recog_screen, text="Invalid Password!!", font=("Century", 10), bg="azure", fg="black").place(x=50, y=60)
    Button(password_not_recog_screen, text="OK", bg="azure", command=lambda:delete_password_not_recognised()).place(x=85, y=110)

# Designing popup for user not found
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(main_menu)
    user_not_found_screen.title("Error")
    user_not_found_screen.geometry("200x200")
    user_not_found_screen.configure(bg="powder blue")
    Label(user_not_found_screen, text="User Not Found!!", font=("Century", 10), bg="azure", fg="black").place(x=50, y=60)
    Button(user_not_found_screen, text="OK", bg="azure", command=delete_user_not_found_screen).place(x=85, y=110)

# Deleting popups
def delete_login_success(sellerlogin_screen):
    login_success_screen.withdraw()
    sellerlogin_screen.withdraw()
    open_Seller_Menu(sellerlogin_screen)

def delete_password_not_recognised():
    password_not_recog_screen.withdraw()

def delete_user_not_found_screen():
    user_not_found_screen.withdraw()



# ========== Functions for Opening Windows ===========  #

def open_Customer_Menu():
    window = Toplevel(main_menu)
    cust_menu = Customer(window)

def open_Payment(cust_menu):
    cust_menu.withdraw()
    window = Toplevel(main_menu)
    payment = Payment(cust_menu, window)

def open_Seller_Login():
    window = Toplevel(main_menu)
    sellerlogin = Seller(window)

def open_Seller_Menu(sellerlogin_screen):
    window = Toplevel(main_menu)
    seller_menu = SellerMenu(sellerlogin_screen, window)

def open_Seller_AddItem(sellerlogin_screen):
    window = Toplevel(main_menu)
    sellerAD = AddItem(sellerlogin_screen, window)

def open_Seller_SeeOrder(sellerlogin_screen):
    window = Toplevel(main_menu)
    see_order = SeeOrder(sellerlogin_screen, window)


# ========== Main Function (Main Menu) ===========  #


def main():
    global main_menu
    main_menu = Tk()
    main_menu.title("Syntax Slurp")
    main_menu.geometry("500x600")
    main_menu.configure(bg="#9AD5E7")
    title = Label(main_menu, text="Syntax Slurp", bd=12, relief=RIDGE, font=("Arial Black", 20),
                  bg="#0C89A5",
                  fg="white").pack(fill=X)

    lblWelcome = Label(main_menu, text="Welcome!", relief=FLAT, font=("Arial Black", 50),
                       bg="#9AD5E7",
                       fg="#075263")
    lblWelcome.place(x=110, y=115)

    lblIntro = Label(main_menu, text="please select your mode:", relief=FLAT, font=("Arial Bold Italic", 12),
                     bg="#9AD5E7",
                     fg="#075263")
    lblIntro.place(x=155, y=265)

    lblIntroBG = Frame(main_menu, relief=FLAT, bg="#075263")
    lblIntro = Label(main_menu, text="For more information, visit us at @syntaxslurp", relief=FLAT, font=("Arial Italic", 10),
                     bg="#075263",
                     fg="white")
    lblIntroBG.place(x=150, y=530)
    lblIntro.place(x=0, y=530, width=500, height=40)

    #button settings for SELLER and CUSTOMER
    seller_frame = Frame(main_menu, bd=7, relief=GROOVE, bg="#0C89A5")
    seller_frame.place(x=94, y=300, width=290, height=90)

    cust_frame = Frame(main_menu, bd=7, relief=GROOVE, bg="#0C89A5")
    cust_frame.place(x=94, y=390, width=290, height=90)

    seller_button = Button(seller_frame, text="SELLER", relief=FLAT, font=("Arial Black", 15), pady=10, bg="white",
                               fg="#0C89A5", width=20, height=1, command=lambda: open_Seller_Login()).grid(row=0, column=0, padx=4, pady=4)
    cust_button = Button(cust_frame, text="CUSTOMER", relief=FLAT, font=("Arial Black", 15), pady=10, bg="white",
                           fg="#0C89A5", width=20, height=1, command=lambda: open_Customer_Menu()).grid(row=0, column=0,
                                                                                                      padx=4, pady=4)

    main_menu.mainloop()

main()
