import streamlit as st
st.title("funny")
tabroblox,tabfacebook,tabmessanger,tabtest,tabhelp,tabteststeps,tabtestheartrate,tabdrink,tabheight=st.tabs(["roblox","facebook","messanger","test","help","steps","heart","drink","height"])
with tabroblox:
    st.header("roblox.com")
    st.title("play other game or make your own to let another play it")
with tabfacebook:
    st.header("facebook.com")
    st.title("chating, friends, watching other videos, read another post or you can make your own")
with tabmessanger:
    st.header("messanger.com")
    st.title("chating or friends...only that")
with tabtest:
    st.header("test.com")
    st.title("what is your age?")
    iq=st.number_input("YoUr Iq:",min_value=0.0,max_value=1000.0,value=100.0,step=0.1)
    if st.button("IQ"):
        st.success(f"Ok:{iq:.0f}")
        if iq<85:
            st.warning("you StUpId")
        elif 85<iq<116:
            st.info("yo bro your brain is normal")
        elif iq>115:
            st.info("you are better than me T_T(crying)")
        else:
            st.error("you write wrong but..... HOW CAN YOU WRITE WRONG... THIS CANT BE TRUE")
with tabhelp:
    st.header("help.com")
    st.title("bmi")
    weight=st.number_input("YoUr WeIgHt(kg):",min_value=10.0,max_value=1000.0,value=60.0,step=1.0)
    height=st.number_input("YoUr HeIgHt(Meter):",min_value=0.4,max_value=2.5,value=1.7,step=0.01)
    bmi=weight/height**2
    if st.button("bmi"):
        st.success(f"Ok bmi:{bmi:.2f}")
        if bmi<18.5:
            st.warning("you're skinny")
        elif 18.4<bmi<24.9:
            st.info("yo bro your weight is normal")
        elif bmi>25:
            st.warning("you're overweight")
        elif 25<bmi<30:
            st.warning("the token of obesity")
        elif 30<bmi<34.9:
            st.warning("obesity level1")
        elif 34.9<bmi<40.1:
            st.warning("obesity level2")
        elif bmi>40:
            st.warning("obesity level3")
        else:
            st.error("you write wrong but..... HOW CAN YOU WRITE WRONG... THIS CANT BE TRUE")
with tabtestheartrate:
    st.header("test3.com")
    st.title("safe heartrate")
    age=int(st.number_input("YoUr AgE:",min_value=0.0,max_value=130.0,value=18.0,step=1.0,key="heart"))
    heartrate=st.number_input("YoUr HeArTrAtE(bpm):",min_value=0.0,max_value=200.0,value=80.0,step=1.0)
    if st.button("heart"):
        if age<=1 and heartrate<100 or heartrate>160:
            st.warning("your baby heartrate is not safe")
        elif 1<age<11 and heartrate<70 or heartrate>120:
            st.warning("your heartrate is not safe")
        elif 10<=age<=64 and heartrate<60 or heartrate>100:
            st.warning("your heartrate is not safe")
        elif age>65 and heartrate<50 or heartrate>100:
            st.warning("your heartrate is not safe")
        elif age<=1 and 100<=heartrate<=160:
            st.info("your baby heartrate is normal")
        elif 1<age<11 and 70<=heartrate<=120:
            st.info("your heartrate is normal")
        elif 10<age<64 and 60<=heartrate<=100:
            st.info("your heartrate is normal")
        elif age>65 and 50<=heartrate<=100:
            st.info("your heartrate is normal")
        else:
            st.error("you write wrong but..... HOW CAN YOU WRITE WRONG... THIS CANT BE TRUE")
with tabteststeps:
    st.header("test2.com")
    st.title("appropriate number of steps per day")
    age2=int(st.number_input("YoUr AgE:",min_value=0.0,max_value=130.0,value=18.0,step=1.0,key="age steps"))
    if st.button("steps"):
        st.success(f"ok age:{age2:.0f}")
        if age2<18:
            st.info("you must walk 12000-15000 steps")
        elif 17<age2<40:
            st.info("you must walk 8000-10000 steps")
        elif 39<age2<65:
            st.warning("you must walk 7000-9000 steps")
        elif age2>64:
            st.warning("you must walk 6000-8000 steps")
        else:
            st.error("you write wrong but..... HOW CAN YOU WRITE WRONG... THIS CANT BE TRUE")
with tabdrink:
    st.header("test3.com")
    st.title("safe liter of water per day")
    drink=st.number_input("YoUr DrInK pEr DaY(liter):",min_value=1.0,max_value=8.0,value=2.0,step=1.0)
    age3=int(st.number_input("YoUr AgE:",min_value=0.0,max_value=130.0,value=18.0,step=1.0,key="age_drink"))
    if st.button("drink"):
        if age3<=3 and drink<1.2 or drink>1.4:
            st.warning("your baby is drink not safe value of liter water per day")
        elif 3<age3<9 and drink<1.6 or drink>1.8:
            st.warning("you are drink not safe value of liter water per day")
        elif 9<=age3<=13 and drink<=2.1 or drink>=2.4:
            st.warning("you are drink not safe value of liter water per day")
        elif 14<=age3<=18 and drink<2.3 or drink>3.3:
            st.warning("you are drink not safe value of liter water per day")
        elif 19<=age3<=50 and drink<2.7 or drink>3.7:
            st.warning("you are drink not safe value of liter water per day")
        elif age3>50 and drink<2.5 or drink>3.0:
            st.warning("you are drink not safe value of liter water per day")
        elif age3<=3 and 1.2<=drink<=1.4:
            st.warning("your baby is drink normal value of liter water per day")
        elif 3<age3<9 and 1.6<=drink<=1.8:
            st.warning("you are drink normal value of liter water per day")
        elif 9<=age3<=13 and 2.1<=drink<=2.4:
            st.warning("you are drink normal value of liter water per day")
        elif 14<=age3<=18 and 2.3<=drink<=3.3:
            st.warning("you are drink normal value of liter water per day")
        elif 19<=age3<=50 and 2.7<=drink<=3.7:
            st.warning("you are drink normal value of liter water per day")
        elif age3>50 and 2.5<=drink<=3:
            st.warning("you are drink normal value of liter water per day")
        else:
            st.error("you write wrong but..... HOW CAN YOU WRITE WRONG... THIS CANT BE TRUE")
with tabheight:
    st.header("test4.com")
    st.title("normal height")
    height=st.number_input("YoUr HeIgHt(meter):",min_value=0.0,max_value=2.5,value=1.7,step=0.01)
    age4=int(st.number_input("YoUr AgE:",min_value=0.0,max_value=130.0,value=18.0,step=1.0,key="height age"))
    if st.button("sure?"):
        if age4<1 and height<0.40:
            st.warning("your baby height is shorter than the normal height")  
        elif age4==1 and height<0.65:
            st.warning("your baby height is shorter than the normal height")
        elif 1<age<=2 and height<0.75:
            st.warning("your baby height is shorter than the normal height")
        elif 2<age<=3 and height<0.85:
            st.warning("your baby height is shorter than the normal height")
        elif 3<age<=4 and height<0.9:
            st.warning("your baby height is shorter than the normal height")
        elif 4<age<=5 and height<1.0:
            st.warning("your baby height is shorter than the normal height")
        elif 5<age<=7 and height<1.05:
            st.warning("your baby height is shorter than the normal height")
        elif 7<age<=10 and height<1.3:
            st.warning("your height is shorter than the normal height")
        elif 10<age<=13 and height<1.4:
            st.warning("your height is shorter than the normal height")
        elif 13<age<=16 and height<1.5:
            st.warning("your height is shorter than the normal height")
        elif age4>16 and height<1.6:
            st.warning("your height is shorter than the normal height")
        elif age4<1 and height>0.50:
            st.info("your baby height is taller than the normal height")  
        elif age4==1 and height>0.85:
            st.info("your baby height is taller than the normal height")
        elif 1<age<=2 and height>0.95:
            st.info("your baby height is taller than the normal height")
        elif 2<age<=3 and height>1.0:
            st.info("your baby height is taller than the normal height")
        elif 3<age<=4 and height>1.05:
            st.info("your baby height is taller than the normal height")
        elif 4<age<=5 and height>1.1:
            st.info("your baby height is taller than the normal height")
        elif 5<age<=7 and height>1.3:
            st.info("your baby height is tallerr than the normal height")
        elif 7<age<=10 and height>1.4:
            st.info("your height is taller than the normal height")
        elif 10<age<=13 and height>1.5:
            st.info("your height is taller than the normal height")
        elif 13<age<=16 and height>1.7:
            st.info("your height is taller than the normal height")
        elif age4>16 and height>1.8:
            st.info("your height is taller than the normal height")
        elif age4>=17 and height==1.90:
            st.info("your height is equal Gojo Satoru height (just search jujutsu kaisen)")
        elif age4<1 and 0.40<=height<=0.50:
            st.info("your baby height is normal")  
        elif age4==1 and 0.65<=height<=0.85:
            st.info("your baby height is normal")
        elif 1<age<=2 and 0.75<=height<=0.95:
            st.info("your baby height is normal")
        elif 2<age<=3 and 0.85<=height<=1:
            st.info("your baby height is normal")
        elif 3<age<=4 and 0.9<=height<=1.05:
            st.info("your baby height is normal")
        elif 4<age<=5 and 1<=height<=1.1:
            st.info("your baby height is normal")
        elif 5<age<=7 and 1.05<=height<=1.3:
            st.info("your baby height is normal")
        elif 7<age<=10 and 1.3<=height<=1.4:
            st.info("your height is normal")
        elif 10<age<=13 and 1.4<=height<=1.5:
            st.info("your height is normal")
        elif 13<age<=16 and 1.5<=height<=1.7:
            st.info("your height is normal")
        elif age4>16 and 1.6<=height<=1.8:
            st.info("your height is normal")
# 1	~75 cm
# 2	~85 cm
# 3	~95 cm
# 4	~100 cm
# 5 – 7	110 – 130
# 8 – 10	130 – 140
# 11 – 13	140 – 150
# 14 – 16	150 – 170
# Trên 16	160 – 18050
