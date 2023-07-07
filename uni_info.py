#! C:\Users\sudhanshu\AppData\Local\Programs\Python\Python311\python.exe
print ("Content-Type: text/html\r\n\r\n")
import cgi
import mysql.connector
con=mysql.connector.connect(host="localhost",user="pl",passwd="rays@1324",database="patna")
x=con.cursor()
f=cgi.FieldStorage()
try:
    d=f.getvalue('t')
    if(d=='ent'):
        d1=f.getvalue('t1').title()
        d2=f.getvalue('t2').title()
        d3=f.getvalue('t3').upper()
        d4=f.getvalue('t4')
        d5=str(f.getvalue('t5'))
        d6=str(f.getvalue('t6'))
        d7=str(f.getvalue('t7'))
        url="insert into university_info values(%s,%s,%s,%s,%s,%s,%s)"
        x.execute(url,(d1,d2,d3,d4,d5,d6,d7))
        con.commit()
        print('Successfully Inserted!')
    elif(d=='load'):
        d1=f.getvalue('t1').upper()
        x.execute("select distinct mode from university_info where u_name='"+d1+"'")
        res=x.fetchall()
        list={'Online','Regular','Private','Distance','Vocational','Part Time','Full Time'} 
        x=set()
        for a in res:
            for t in a:
                x.add(t)
        for a in list:
            if a not in x:
                print('<option>'+a+'</option>')
    elif(d=='click'):
        a=set()
        b=set()
        x.execute('select u_name,mode from university_info')
        res=x.fetchall()
        for i in res:
            a.add(i[0])
            b.add(i[1])
        for i in a:
            print('<option>'+i+'</option>')
        print(',,,')
        for i in b:
            print('<option>'+i+'</option>')
    elif(d=='click1'):
        d1=f.getvalue('t1')
        x.execute("select distinct mode from university_info where u_name='"+d1+"'")
        res=x.fetchall()
        for a in res:
            print('<option>'+a[0]+'</option>')
    elif(d=='search'):
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        url="select u_name,mode,u_reg,link from university_info where"
        if(d1!=None):
            url=url+" u_name='"+d1+"'"
        if(d2!=None and d1!=None):
            url=url+" and mode='"+d2+"'"
        if(d2!=None and d1==None):
            url=url+" mode='"+d2+"'"
        x.execute(url)
        res=x.fetchall()
        print('<br><div style="text-align: right;"><input type="button" value="Update" id="b5"><input type="button" value="Delete" id="b6"></div><br><br><br><table id="t3"><thead><tr><th id="th1">UNIVERSITY NAME</th><th id="th2">MODE</th><th id="th3">UNI_RECOG</th><th id="th4">LINK</th><th id="th5" id="rr1" class="rr1">Check</th></tr></thead><tbody>')
        for a in res:
            print('<tr><td data-label="UNIVERSITY NAME : ">'+a[0]+'   '+'</td><td data-label="MODE : ">'+a[1]+'   '+'</td><td data-label="UNI_RECOG : " contenteditable="true" id="e">'+a[2]+'   '+'</td><td data-label="LINK : " contenteditable="true" id="e">'+a[3]+'   '+'</td><td id="rr2" class="rr1"><input type="radio" name="r" id="r1"></td></tr>')
        print('</tbody></table>')
    elif(d=='update'):
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        url="update university_info set u_reg='"+d3+"',link='"+d4+"' where u_name='"+d1+"' and mode='"+d2+"'"
        x.execute(url)
        con.commit()
        print('Successfully Updated!')
    elif(d=='delete'):
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        x.execute("delete from university_info where u_name='"+d1+"' and mode='"+d2+"';")
        if d3=='yes':
            x.execute("delete from program_details where u_name='"+d1+"' and mode='"+d2+"';")
        con.commit()
        print('Successfully Deleted!')
    elif(d=='load1'):
        x.execute('select distinct u_name from university_info')
        res=x.fetchall()
        for a in res:
            print('<option>'+a[0]+'</option>')
    elif(d=='ent1'):
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        d6=f.getvalue('t6')
        d7=f.getvalue('t7')
        d8=f.getvalue('t8')
        d9=f.getvalue('t9')
        d10=f.getvalue('t10')
        d11=f.getvalue('t11')
        d12=f.getvalue('t12')
        d13=f.getvalue('t13')
        x.execute("select u_name,mode,p_name from program_details where u_name='"+d1+"' and mode='"+d2+"' and p_name='"+d3+"'")
        res=x.fetchall()
        if res==[]:
            url="insert into program_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            x.execute(url,(d1,d2,d3,d7,d5,d6,d4,d8,d9,d10,d11,d12,d13))
            con.commit()
            print('Successfully Inserted!')
        else:
            print(0)
    elif(d=='click2'):
        a=set()
        b=set()
        c=set()
        x.execute('select u_name,p_name,mode from program_details')
        res=x.fetchall()
        for i in res:
            a.add(i[0])
            b.add(i[1])
            c.add(i[2])
        for i in a:
            print('<option>'+i+'</option>')
        print(',,,')
        for i in b:
            print('<option>'+i+'</option>')
        print(',,,')
        for i in c:
            print('<option>'+i+'</option>')
    elif(d=='search1'):
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        url="select * from program_details where"
        if(d1!=None):
            url=url+" u_name='"+d1+"'"
        if(d2!=None and d1!=None):
            url=url+" and p_name='"+d2+"'"
        if(d2!=None and d1==None):
            url=url+" p_name='"+d2+"'"
        if(d3!=None and (d2!=None or d1!=None)):
            url=url+" and mode='"+d3+"'"
        if(d3!=None and d2==None and d1==None):
            url=url+" mode='"+d3+"'"
        # print(url)
        x.execute(url)
        res=x.fetchall()
        if res!=[]:
            print('<br><br><div style="text-align: right;"><input type="button" value="Update" id="b5"><input type="button" value="Delete" id="b6"></div><br><table id="t3"><thead><tr><th>University Name</th><th>Mode</th><th>Course</th><th>Lat_Ent</th><th>Min_dur</th><th>Max_dur</th><th>Eligibility</th><th>Session</th><th>Prog Fee</th><th>Admi Fee</th><th>Exm Fee</th><th>Ser Charge</th><th>Ref Fee</th><th>Share</th><th id="rr1" class="rr1">Check</th></tr></thead><tbody>')
            for i in res:
                print('<tr><td data-label="UNIVERSITY NAME : ">'+i[0]+'   '+'</td><td data-label="MODE : ">'+i[1]+'   '+'</td><td data-label="COURSE : ">'+str(i[2])+'   '+'</td><td data-label="LATERAL ENTRY : " contenteditable="true" id="e">'+str(i[3])+'   '+'</td><td data-label="MIN. DURATION : " contenteditable="true" id="e">'+str(i[4])+'   '+'</td><td data-label="MAX. DURATION : " contenteditable="true" id="e">'+str(i[5])+'   '+'</td><td data-label="ELIGIBILITY : " contenteditable="true" id="e">'+str(i[6])+'   '+'</td><td contenteditable="true" data-label="SESSION : " id="e">'+str(i[7])+'   '+'</td><td data-label="PROGRAM FEE : " contenteditable="true" id="e">'+str(i[8])+'   '+'</td><td data-label="ADMISSION FEE : " contenteditable="true" id="e">'+str(i[9])+'   '+'</td><td data-label="EXAM FEE : " contenteditable="true" id="e">'+str(i[10])+'   '+'</td><td data-label="SERVICE CHARGE : " contenteditable="true" id="e">'+str(i[11])+'   '+'</td><td data-label="REFERAL FEE : " contenteditable="true" id="e">'+str(i[12])+'   '+'</td><td data-label="Share : "><input type="button" class="fa" value="&#xf1e0;" id="b7"></td><td id="rr2" class="rr1"><input type="radio" name="r" id="r1"></td></tr>')
            print('</tbody></table>')
        else:
            print(0)
    elif(d=='delete1'):
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        url="delete from program_details where u_name='"+d1+"' and mode='"+d2+"' and p_name='"+d3+"'"
        x.execute(url)
        con.commit()
        print('Successfully Deleted!')
    elif(d=='update1'):
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        d6=f.getvalue('t6')
        d7=f.getvalue('t7')
        d8=f.getvalue('t8')
        d9=f.getvalue('t9')
        d10=f.getvalue('t10')
        d11=f.getvalue('t11')
        d12=f.getvalue('t12')
        d13=f.getvalue('t13')
        url="update program_details set lateral_Entry='"+d4+"',min_dur='"+d5+"',max_dur='"+d6+"',eligibility='"+d7+"',session='"+d8+"',pro_fees='"+d9+"',adm_fees='"+d10+"',exam_fees='"+d11+"',ser_fees='"+d12+"',ref_fees='"+d13+"' where u_name='"+d1+"' and mode='"+d2+"' and p_name='"+d3+"'"
        x.execute(url)
        con.commit()
        print('Successfully Updated!')
    if(d=='ready'):
        x.execute('select * from sign_up')
        res=x.fetchall()
        if res==[]:
            print(0)
        else:
            print(4)
    if(d=='sign'):
        d1=f.getvalue('t1').title()
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        d6=f.getvalue('t6')
        d7=f.getvalue('t7')
        x.execute('select uid from sign_up where uid="'+d2+'"')
        r=x.fetchall()
        if r==[]:
            url='insert into sign_up (un,uid,pw,sq,sa,role,status) values(%s,%s,%s,%s,%s,%s,%s)'
            x.execute(url,(d1,d2,d3,d4,d5,d6,d7))
            con.commit()
            print('Successfully Sign Up')
        else:
            print(0)
    elif(d=='login'):
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        x.execute("select un,role,status from sign_up where uid='"+d1+"' and pw='"+d2+"'")
        res=x.fetchall()
        if res==[]:
            print(0)
        else:
            if res[0][2]=='0':
                print(1)
            else:
                print(res[0][0],res[0][1],sep=',,,')
    elif (d=="show"):
        x.execute("select uid,un from sign_up where status='0' order by sn desc")
        res=x.fetchall()
        print("""<div class="t_r" id="t_r">""")
        print("""<p class="t35">LOG IN TABLE STATUS</p>""")
        print("""<table class="table_1"><tr class="t36"><th>USER ID</th><th>USER NAME</th><th>STATUS</th><th>ROLE</th><th>UPDATE</th><th>DELETE</th></tr>""")
        if res!=[]:
            for r in res:
                print("<tr class='u'><td>"+r[0]+"   </td><td>"+r[1]+"   </td>")
                print("<td><select id='a_i'><option value='0' selected>Inactive</option><option value='1'>Active</option></select></td>")
                print("<td><select id='rol'><option value='3' selected>User</option><option value='2'>Counsellor</option><option value='1'>Admin</option></select></td>")
                print("</select></td>")
                print("<td><input type='checkbox' class='t41 up'></td><td><input type='checkbox' class='t41 dl'></td></tr>")
        else:
            print("<tr><td colspan='6'>DATA NOT FOUND</td></tr>")
        print("</table>")
        print("""</div>""")  
    elif (d=="up1"):
        a=f.getvalue('a')
        b=f.getvalue('b')
        c=f.getvalue('c')
        url="update sign_up set status='"+b+"', role='"+c+"' where uid='"+a+"'"
        x.execute(url)
        con.commit()
        print("Records Successfilly Updated")
    elif (d=="del1"):
        a=f.getvalue('a')
        url="delete from sign_up where uid='"+a+"'"
        x.execute(url)
        con.commit()
        print("Records Successfilly Deleted!")
    elif (d=="search_3"):
            url="select un,uid,role,status from sign_up where status='1' and role!='0'"
            x.execute(url)
            res=x.fetchall()
            print("""<div class="t_r2" id="t_r">""")
            print("""<table class='table_3'><tr class='t36'><th class="th_1">USER NAME</th><th class="th_1">USER ID</th><th class="th_1">ROLE</th><th class="th_1">STATUS</th></tr>""")
            if(res!=[]):
                for a in res:
                    print("<tr class='u2'><td>"+a[0]+"   </td><td>"+a[1]+"   </td><td>"+a[2]+"   </td><td>"+a[3]+"   </td>")
            else:
                print("<tr><td style='text-align: center;height:100px; font-size:25px;' colspan='5'>Records not found!</td></tr>")
            print("""</table>""")
            print("""</div>""")
    elif (d=="search_2"):
        a=f.getvalue('a')
        b=f.getvalue('b')
        if(a=='Username'):
            url="select un,uid,role from sign_up where status='1' and role!='0' and un='"+str(b)+"'"
        else:
            url="select un,uid,role from sign_up where status='1' and role!='0' and uid='"+str(b)+"'"
        x.execute(url)
        res=x.fetchall()
        print("""<div class="t_r2" id="t_r">""")
        print("""<table class='table_2 table_3'><tr class='t36'><th class="th_1">USER NAME</th><th class="th_1">USER ID</th><th class="th_1">ROLE</th><th class="th_1">STATUS</th><th class="th_1">Check</th></tr>""")
        if(res!=[]):
            for a in res:
                print("<tr class='u2'><td>"+a[0]+"   </td><td>"+a[1]+"   </td><td class='single'>"+a[2]+"   </td>")
                print("<td><select id='a_i'><option value='1' selected>Active</option><option value='0'>Inactive</option></select></td>")
                print("<td><input type='checkbox' name='radio1' class='t41 r1'></td></tr>")
        else:
            print("<tr><td style='text-align: center;height:100px; font-size:25px;' colspan='5'>Records not found!</td></tr>")
            print("""</table>""")
            print("""</div>""")
    elif (d=="up3"):
        a=f.getvalue('a')
        b=f.getvalue('b')
        url="update sign_up set status='"+b+"' where uid='"+a+"'"
        x.execute(url)
        con.commit()
        print("Successfully updated")
    elif(d=='pdf'):
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        x.execute("select u_reg,link,broch,pors,a_f from university_info where u_name='"+d1+"' and mode='"+d2+"'")
        res=x.fetchall()
        print(res[0][0],',,,',res[0][1],',,,',res[0][2],',,,',res[0][3],',,,',res[0][4])
    elif d=='xyz':
        a=f.getvalue('a')
        b=f.getvalue('b')
        c=f.getvalue('c')
        e=int(f.getvalue('e'))
        x.execute("select pw from sign_up where uid='"+a+"' and sq='"+b+"' and sa='"+c+"' and status='1'")
        res=x.fetchall()
        if res==[]:
            if e==1:
                x.execute("update sign_up set status='0' where uid='"+a+"'")
                con.commit()
            a=0
            print(a)
        else:
            a=1
            print(a)
    elif d=="f_p":
        a=f.getvalue('a')
        b=f.getvalue('b')
        c=f.getvalue('c')
        d=f.getvalue('d')
        url="update sign_up set pw='%s' where uid='%s' and sq='%s' and sa='%s'"%(d,a,b,c)
        x.execute(url)
        con.commit()
        print("Password Changed now you can login!")
except Exception as e:
    print('Fail',e)