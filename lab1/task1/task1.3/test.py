


import OrderItem, Product, datetime,Order,OrderManager

if __name__ == '__main__':
    # name, type, price, expiredDate
    banhTrang =  Product('Banh trang', 'Do an vat', 15000, datetime.date(2023, 2, 15))
    huTieu = Product('Hu tieu', 'Mon an chinh', 25000, datetime.date(2023, 2, 15))
    xoai = Product('Xoai', 'Trai cay', 5000, datetime.date(2023, 2, 15))
    chuoi = Product('chuoi', 'Trai cay', 6000, datetime.date(2023, 2, 15))
    cam = Product('cam', 'Trai cay', 8000, datetime.date(2023, 2, 15))

    orderItem1= OrderItem(banhTrang, 1)
    orderItem2= OrderItem(huTieu, 1)
    orderItem3 = OrderItem(xoai, 4)
    orderItem4 = OrderItem(chuoi, 10)
    orderItem5 = OrderItem(cam, 15)

    list1=list()
    list1.append(orderItem1)
    list2=list()
    list2.append(orderItem2)
    list3=list()
    list3.append(orderItem3)
    list3.append(orderItem4)
    list3.append(orderItem5)

    order1= Order('001', 'Nguyen Van A', 'Hanh Hanh', datetime.date.today(), list1)
    order2= Order('002', 'Nguyen Van B', 'Thanh Thanh', datetime.date.today(), list2)
    order3= Order('001', 'Nguyen Van A', 'Hanh Hanh', datetime.date.today(), list3)

    listOrder=list()
    listOrder.append(order1)
    listOrder.append(order2)
    listOrder.append(order3)
    orderManager = OrderManager(list)