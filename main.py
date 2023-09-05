import flet as ft
import pymongo
from time import sleep
import speedtest


def main(page:ft.Page):
    page.title="Internet SpeedTest App"
    page.theme_mode="dark"
    page.window_center=True
    page.spacing=30#the spacing for internet app to speed container
    page.padding=80
    page.auto_scroll=True
    
    
    
    page.vertical_alignment="center"
    page.horizontal_alignment="center"
    page.bgcolor="pink"
    page.window_bgcolor="blue"
    page.auto_scroll=True
    my_client=pymongo.MongoClient("mongodb://localhost:27017")
    mydb=my_client["network_test"]#database
    mycol=mydb["speed_test"]
    hello_text=ft.Text(value="Welcome",size=20,color="#1C2833",bgcolor="white")
    hello_text1=ft.Text(value="Internet SpeedTest App",color="white",bgcolor="#1C2833",size=25)
    hello_col=ft.Row([ft.Column([hello_text,hello_text1])])

    username1=ft.TextField(label="Username",width=450,bgcolor="white",color="black",focused_border_color="#FD6585")


    pass1=ft.TextField(label="Create Password",width=450,bgcolor="white",color="black",password=True,can_reveal_password=True,focused_border_color="#FD6585")
    conformpass1=ft.TextField(label="Conform Password",width=450,bgcolor="white",color="black",password=True,can_reveal_password=True,focused_border_color="#FD6585")
    gmail=ft.TextField(label="Gamil",width=450,bgcolor="white",color="black",focused_border_color="pink")


    username2=ft.TextField(label="Username",width=450,bgcolor="white",color="black",focused_border_color="orange")

    pass2=ft.TextField(label="Password",width=450,bgcolor="white",color="black",password=True,can_reveal_password=True,focused_border_color="orange")
    #---------------------------------------page1------------------------------------------------------------
    x10=ft.Row(controls=[ft.Text("*Internet",color="#FF4500",size=25,font_family="Wide Latin",bgcolor="#228B22"),
           ft.Text("-Speed-",color="white",size=25,font_family="Wide Latin"),
           ft.Text("Test*",color="#00AA00",size=25,font_family="Wide Latin",bgcolor="orange")],alignment="center")
    
    line1=ft.Text("please click start",color="black",style="Bold",size=20)
    line2=ft.Text("",color=ft.ColorScheme,style="Bold",size=20)
    progressbar1=ft.ProgressBar(width=400,color="#180DC3",bgcolor="white",opacity=0)
    progressbartext=ft.Text("   ")
    progressbar1_row=ft.Row(controls=[progressbartext,progressbar1])
    line3=ft.Text("",color="",font_family="Times New Roman",style="Bold",size=20)
    
    
    progressbar2=ft.ProgressBar(width=400,color="blue",bgcolor="white",opacity=0)
    progressbartext2=ft.Text("   ")
    progressbar2_row=ft.Row(controls=[progressbartext2,progressbar2])
    line4=ft.Text("",color="orange",font_family="Open Sans",size=20,style="Bold")
    line5=ft.Text("",color="black",font_family="Open Sans",size=20,style="Bold")
    line6=ft.Text("",color="orange",font_family="Open Sans",size=20,style="Bold")
    line7=ft.Text("",color=ft.colors.TEAL_700,font_family="Helvetica Neue",size=20,style="Bold")
    line8=ft.Text("",color=ft.colors.YELLOW_700,font_family="Times New Roman",size=20,style="Bold")
    line9=ft.Text("",color="pink",font_family="Lucida Fax",size=20,style="Bold")
    lines=ft.Column(controls=[line1,line2, line3,progressbar1_row,line4,line5,line6,progressbar2_row,line7,line8,line9])
    

    st=speedtest.Speedtest()
    
    speed_container=ft.Container(
        content=lines,
    
        width=200,
        height=50,
        bgcolor="grey",
        border_radius=10,
        padding=30,
        
        animate=ft.animation.Animation(1000,"bounceOut"),
        
        )
    global change_screen
    def change_screen(e):
       
        speed_container.width=610
        speed_container.height=610
        speed_container.update()
        line1.value="Calculate the Downloading Speed......"
        
        
        speed_container.update()
        sleep(1)
        
        idel_server=st.get_best_server()#this will find out the best server and connect the best posible server
     # in the it will give output in dictionary city name as "name",country
        city=idel_server["name"]
        country=idel_server["country"]
        cc=idel_server["cc"]
        line2.value=f"->Finding the best posibble server{city}, {country}, {(cc)}"
        speed_container.update()
        sleep(1)
        line3.value="->Connection establish, status okay...., fetching downloading speed"
        progressbar1_row.opacity=1
        progressbar1.opacity=1
        speed_container.update()
        downloading_speed=st.download()/1024/1024
        sleep(1)
        progressbar1.value=1
        
        line4.value=f"->The Download Speed is {str(round(downloading_speed,2))} Mbps"
        speed_container.update()
        line5.value="->Calculating upload speed,please  wait....."
        speed_container.update()
        sleep(1)
        line6.value="->Executing upload script, hold on"
        progressbar2_row.opacity=1
        progressbar2.opacity=1
        speed_container.update()
        uploading_speed=st.upload()/1024/1024
        sleep(1)
        progressbar2.value=1
        line7.value=f"->The upload speed is {str(round(uploading_speed,2))} Mbps"
        speed_container.update()
        sleep(1)
        line8.value="\t\t-----------------------------🙏🙏-----------------------------"
        line9.value="\t\t~~~~~~~~~Task completed sucessfully~~~~~~~~~\n\t\t\t\t\t\t\t\t\t\t\t\t\t✌️Be Happy Be Cool - Enjoy The Life✌️\n\t\t\t~~~~~~~~~~~Thanks visiting \t😊~~~~~~~~~~~\n\nInsta ID:- _ganesh__reddy"
        speed_container.update()

        #-----------------------------------------------page 2 code end-------------------------------------------
    #Be Happy Be Cool\Enjoy The Life

    
    #--------------------page 1 code ----------------------------------------------------
    global l
    
    def register(e):
        l=True
        if len(username1.value)==0:
            username1.error_text="Please enter the Username"
            page.update()
        elif not pass1.value:
            pass1.error_text="Please enter the Username"
            page.update()
        elif pass1.value != conformpass1.value:
            conformpass1.error_text="Password and Conformpassword are not same"
            page.update()
        else:
            x=mycol.find({"name":username1.value})
            
            for i in x:
                if i["name"]==username1.value:
                    l=False
                    username1.error_text="username already exist"
                    page.update()
            if l:
                x={"name":username1.value,"password":pass1.value}
                mycol.insert_one(x)
                l=0
                print(x)
                
                username1.visible= False
                pass1.visible=False
                #pass1.value="" HERE THE VALUE IS STE to text
                conformpass1.visible=False
                gmail.visible=False
                registerbut.visible=False
                page.update()
                register_details.controls.append(ft.Column(controls=[ft.Text("THANKS FOR REGISTERING",size=25,color="orange"),
                                                                    ft.Text("Register sucessfully....",color="green",size=20)],
                                                                    horizontal_alignment="center"))
                page.update()


    
      

    def login(e):
        x3=mycol.find({"name":username2.value})
        l=[]
        for i in x3:
            l.append(i["name"])
       
        
        
        if not username2.value:
            username2.error_text="Please Enter The Username"
            page.update()
        elif not pass2.value:
            pass2.error_text="Please Enter Passwotrd"
            page.update()
        elif len(l)==0:
            username2.error_text="Please Give Correct Username"
            page.update()
        else:
            x1=mycol.find({"name":username2.value})
            for i in x1:
                if i["name"]==username2.value and i["password"]!=pass2.value:
                    pass2.error_text="Wrong Password"
                    page.update()
                elif i["name"]==username2.value and i["password"]==pass2.value:
                    
                    page.clean()
                    page.update()
                    page.title="Internet SpeedTest App"
                    page.horizontal_alignment="center"
                    page.vertical_alignment="center"
                    page.window_bgcolor="pink"
                    page.window_progress_bar=True

                    page.bgcolor=ft.colors.BLACK
                    page.window_center=True
                    page.auto_scroll=True
                    page.padding=10
                    page.update()
                    page.add(
                        x10,
                        speed_container,
                        ft.IconButton(ft.icons.START_ROUNDED,icon_color="green",icon_size=30,on_click=change_screen,)
                    )
                else:
                    pass
                    


                
                
    """def reload5(e):
        
        tab.clean()
        page.update()
        page.add(tab)
        page.update()

    
    reload1=ft.IconButton(ft.icons.REFRESH_OUTLINED,on_click=reload5)"""
    def on_hover1(e):
        e.control.bgcolor="white" if e.data =='true' else "black"
        e.control.color=ft.colors.DEEP_ORANGE_900 if e.data=='true' else "white"
       
        e.control.update()

    registerbut=ft.ElevatedButton(text="Register",on_click=register,color="white",on_hover=on_hover1)
    register_details=ft.Column([
            username1,pass1,conformpass1,gmail,registerbut,
            
        ],spacing=20)
    #registerbut=ft.ElevatedButton(text="Register",on_click=register)
    
    
    loginbut=ft.ElevatedButton("Login",on_click=login,color="white",on_hover=on_hover1)
    x=ft.Container(
        content=register_details,
        
        
        width=450,
        height=450,
        border_radius=50,
        padding=50,
        
        animate=ft.animation.Animation(1000,"bounceOut")
     )
    y=ft.Container(
        ft.Column([
            username2,pass2,loginbut
        ]),
        width=450,
        height=450,
        padding=50,
        border_radius=50,
        animate=ft.animation.Animation(1000,"bounceOut")
    )

    tab=ft.Container(ft.Tabs(
        label_color="orange",#login and register colour
        animation_duration=2,

        
        indicator_border_radius=10,
        indicator_border_side=10,
        divider_color="pink",
        indicator_color='orange',
       


        
        
       
        tabs=[
        ft.Tab(
        
        text="Register",
        content=x,
        
      
        ),
       
        ft.Tab(
        

        
        
        text="Login",
        content=y,
        
  
        
       
       
        ),


        
    ],
    
    
    expand=1,
    
    ),
    width=550,
    height=550,
    bgcolor="white",
    alignment=ft.alignment.center
    )

        
    
    page.add(hello_col,
        tab
             )
    page.update()
    
ft.app(target=main)