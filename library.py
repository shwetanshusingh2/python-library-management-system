import mysql.connector
from appJar import gui
from datetime import datetime
from datetime import timedelta
from datetime import date
db=mysql.connector.connect(host='localhost',database='mysql',user='root',password='mysql123')
cursor=db.cursor()
cursor.execute("use db1")
pk=10
jk="BOOK_NAME"
app=gui()
kol=1
counter=1
com=1
def swaroski():
    app=gui()
    def loc(win):
        global counter
        global kol
        global com
        if(win=="search book" and counter>com):
            kol=1
            com=counter

        app.setBg("orange")
        app.showSubWindow(win)

    # start initial, vertical pane
    app.startPanedFrameVertical("p1")
    app.setGeometry("400x400")
    app.setBg("orange")
    app.addButton("add new book",loc)


    # start additional panes inside initial pane
    app.startPanedFrame("p2")
    app.setBg("orange")
    app.addButton("search book",loc)
    app.stopPanedFrame()

    app.startPanedFrame("p3")
    app.setBg("orange")
    app.addButton("Return book", loc)
    app.stopPanedFrame()

    """app.startPanedFrame("p4")
    app.setBg("orange")
    app.addButton("issue", loc)
    app.stopPanedFrame()"""

    # stop initial pane
    app.stopPanedFrame()







    # this is a pop-up
    app.startSubWindow("add new book")

    def pressed(button):
        global counter
        if button == "Cancel":
            app.stop()
            swaroski()
        else:
            bookname = app.getEntry("bookname")
            author = app.getEntry("author")
            publisher = app.getEntry("publisher")
            price = app.getEntry("price")
            edition = app.getEntry("edition")
            subject = app.getEntry("subject")
            no=app.getEntry("Noofbooks")
            count = 0
            try:

                if (str(bookname) != bookname or str(author) != author or str(publisher) != publisher or str(
                    edition) != edition or str(subject) != subject):
                    count = count + 1
                else:

                    bookname = str(bookname)
                    author = str(author)
                    publisher = str(publisher)
                    edition = str(edition)
                    subject = str(subject)
                    price = int(price)
                    no = int(no)
                    for kll in range(no):
                        sql = "INSERT INTO BOOK(BOOK_NAME,\
                                   AUTHOR,PUBLISHER, PRICE,EDITION,SUBJECT)\
                                   VALUES('%s','%s','%s','%d','%s','%s')" % \
                        (bookname, author, publisher, price, edition, subject)

                        # Execute the SQL command
                        cursor.execute(sql)
                        #    Commit your changes in the database
                        db.commit()

            except:
                # Rollback in case there is any error
                count = count + 1


            if (count == 0):
                app.infoBox("new window", "entry successful", parent="add new book")

            else:
                app.infoBox("new window", "entry usuccessful", parent="add new book")
        counter=counter+1
        print("counter:" + str(counter))
        app.stop()
        swaroski()
        app.startsubwindow()


    app.addLabelEntry("bookname")
    app.addLabelEntry("author")
    app.addLabelEntry("publisher")
    app.addLabelEntry("price")
    app.addLabelEntry("edition")
    app.addLabelEntry("subject")
    app.addLabelEntry("Noofbooks")

    app.addButtons(["Add", "Cancel"], pressed)
    app.stopSubWindow()







    # this is another pop-up
    app.startSubWindow("search book" )


    def pr(button):
            global kol
            global eg
            global pk
            pk=pk+1

            def kero(button):
                    counte=0
                    lo=app.getRadioButton(str(kol) + str(pk))
                    index=0
                    bookid=lo[0]
                    for x in lo:
                        if (x=="/"):
                            break
                        else:

                            index=index+1

                    for j in range(1,index):
                        bookid=bookid+lo[j]
                    print(bookid)

                    app.setRadioButtonTooltip(str(kol)+str(pk),"available")
                    cool=app.textBox(str(kol)+str(pk),"enter member id", parent="search book",)
                    print("your member id is",cool)
                    if(cool!="null"):
                        counter=0
                        try:
                            now = datetime.now()
                            year=str(now.year)
                            month=str(now.month)
                            day=str(now.day)
                            idate=year+"-"+month+"-"+day
                            rdate=datetime.now() + timedelta(days=15)
                            year = str(rdate.year)
                            month = str(rdate.month)
                            day = str(rdate.day)
                            rdate1 = year + "-" + month + "-" + day
                            print("return",rdate1)
                            print(idate)
                            lll = "INSERT INTO take(BOOKID,\
                                                       MEMBERID,ISSUE_DATE,RETURN_DATE)\
                                                       VALUES('%s','%s','%s','%s')" % \
                              (bookid, cool, idate, rdate1)
                            cursor.execute(lll)
                            db.commit()
                        except:
                            app.infoBox(str(kol)+str(pk)+"99", "entry unsuccessful", parent="search book")
                            counte=counte+1
                        if(counte==0):
                            app.infoBox(str(kol) + str(pk)+"9", "book issued", parent="search book")
            if(kol>1):
                print(kol)
                app.removePanedFrame(str(kol))






            kol=kol+1
            app.openPanedFrame("helen")
            app.startPanedFrame(str(kol))
            app.startScrollPane(str(kol))

            k = app.getOptionBox("Options")

            lol =   "Select * from book where (%s='%s')" % \
              (k,app.getEntry("searchme"))

            fasa="Select bookid from take"
            list1=[]
            cursor.execute(fasa)
            lok=cursor.fetchall()
            for mp in lok:
                index=0
                chu=str(mp)
                bookid = chu[1]
                for x in mp:
                    if (x == ","):
                        break
                    else:

                        index = index + 1
                print("index",index)
                for j in range(1, index):
                    bookid = bookid + chu[j]

                list1.append(int(bookid))
            print(list1)

            app.setBg("orange")

            app.setSticky("news")
            app.setExpand("both")
            app.setFont(20)


            app.addLabel("lpp1"+str(kol)+str(pk), "BOOK_ID", 1, 0)
            app.addLabel("lppp2"+str(kol)+str(pk), "BOOK_NAME", 1, 1)
            app.addLabel("lpp3"+str(kol)+str(pk), "AUTHOR", 1, 2)
            app.addLabel("lpp4"+str(kol)+str(pk), "PUBLISHER", 1, 3)
            app.addLabel("lpp5"+str(kol)+str(pk), "PRICE", 1, 4)
            app.addLabel("lpp6"+str(kol)+str(pk), "EDITION", 1, 5)
            app.addLabel("lpp7"+str(kol)+str(pk), "SUBJECT", 1, 6)
            app.addButton("lpp8"+str(kol)+str(pk),kero,1,7)

            cursor.execute("use db1")

        # Execute the SQL command
            cursor.execute(lol)

            km=1
        # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            l=cursor.rowcount

            for row in results:
                lodha=0
                app.setSticky("news")
                app.setExpand("both")
                app.setFont(20)

                app.addLabel(str(pk)+str(kol)+"l1%s" % str(km), "%s" % row[0], km+1, 0)
                app.addLabel(str(pk)+str(kol)+"m2%s" % str(km), "%s" % row[1], km+1, 1)
                app.addLabel(str(pk)+str(kol)+"n3%s" % str(km), "%s" % row[2], km+1, 2)
                app.addLabel(str(pk)+str(kol)+"o4%s" % str(km), "%s" % row[3], km+1, 3)
                app.addLabel(str(pk)+str(kol)+"p5%s" % str(km), "%d" % row[4], km+1, 4)
                app.addLabel(str(pk)+str(kol)+"q6%s" % str(km), "%s" % row[5], km+1, 5)
                app.addLabel(str(pk)+str(kol)+"r7%s" % str(km), "%s" % row[5], km+1, 6)
                for mp in list1:
                    if(mp==row[0]):
                        lodha=lodha+1
                    print(lodha)
                if(lodha==0):
                    app.addRadioButton(str(kol)+str(pk),str(row[0])+str("/")+str(pk)+str(kol)+"r7%s" % str(km),km+1,7 )


                km=km+1


            app.stopScrollPane()
            app.stopPanedFrame()

            app.stopPanedFrame()
    app.setSticky("news")
    app.setFont(10)
    app.setExpand("both")

    app.startPanedFrameVertical("helen")

    app.addLabelOptionBox("Options", ["BOOK_ID", "BOOK_NAME", "PUBLISHER",
                                      "AUTHOR"], 0, 1)
    app.addLabelEntry("searchme", 0, 2)

    app.addButton("show data", pr, 0, 3)


    app.stopPanedFrame()

    app.stopSubWindow()







    #this is another popup

    app.startSubWindow("Return book")
    app.addLabel("l3", "SubWindow Three")



    def pre(button):
        global counter
        london = app.getDatePicker("dp")
        if button == "cancelo":
            app.stop()
            swaroski()
        else:
            try:
                fname1 = app.getEntry("MEMBERID")
                lname1 = app.getEntry("BOOKID")
                lname=int(lname1)
                fname = int(fname1)




                lsql ="select return_date from take where BOOKID=%s and MEMBERID=%s" %(lname,fname)

                        # Execute the SQL command
                cursor.execute(lsql)
                        #    Commit your changes in the database

                lpr=cursor.fetchall()




                d0 = date(lpr[0][0].year,lpr[0][0].month,lpr[0][0].day)
                d1 = date(london.year,london.month,london.day)
                delta = d1-d0
                print(delta.days)
                if(delta.days-15)>0:
                    cash=30+(delta.days-15)*5
                elif(delta.days<=0):
                    cash=0
                else:
                    cash = delta.days * 2

                app.infoBox("new window","fine: "+str(cash), parent="Return book")

                lsql = "DELETE FROM take \
                                        WHERE(BOOKID='%s' AND MEMBERID='%s')" % \
                      (lname,fname)
                cursor.execute(lsql)
                db.commit()
            except:
                app.infoBox("new window","book not fund", parent="Return book")
        counter = counter + 1
        app.stop()
        swaroski()

    app.addLabelEntry("MEMBERID")
    app.addLabelEntry("BOOKID")
    app.addDatePicker("dp")
    app.setDatePickerRange("dp", 2000, 2100)
    app.setDatePicker("dp")
    app.addButtons(["Submito", "Cancelo"], pre)





    app.stopSubWindow()







    #this is another popup
    """def issues(button):
        global counter
        if button == "Cancel":
            app.stop()
            swaroski()
        else:
            bid = app.getEntry("book_id")
            mid = app.getEntry("member_id")
            idate= app.getEntry("issue_date")
            rdate = app.getEntry("return_date")
            bid=int(bid)
            mid=int(mid)

            sql = "INSERT INTO take(BOOKID,\
                               MEMBERID,ISSUE_DATE,RETURN_DATE)\
                               VALUES('%s','%s','%s','%s')" % \
                           (bid, mid,idate,rdate)

            # Execute the SQL command
            cursor.execute(sql)
            #    Commit your changes in the database
            db.commit()
            app.infoBox("new window", "entry successful", parent="issue")
        counter=counter+1
        print("counter:" + str(counter))
        app.stop()
        swaroski()

    app.startSubWindow("issue")

    app.addLabelEntry("book_id")
    app.addLabelEntry("member_id")
    app.addLabelEntry("issue_date")
    app.addLabelEntry("return_date")
    app.addButton("do",issues)


    app.stopSubWindow()"""


    app.go()

app.startLabelFrame("Login Details")
app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")

app.setBg("orange")
app.setFont(18)
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        if(usr=="user" and pwd=="mysql"):


                    app.infoBox("new window","congrats connection successful", parent=None)
                    app.stop()
                    swaroski()



        else:
                    app.infoBox("new window", "unsuccessful try again", parent=None)


app.addButtons(["Submit", "Cancel"], press)
app.stopLabelFrame()


app.go()

