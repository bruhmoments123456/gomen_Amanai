import streamlit as st
st.title("funny")
tabroblox,tabfacebook,tabmessanger,tabtest,tabhelp,tabteststeps,tabtestheartrate=st.tabs(["roblox","facebook","messanger","test","help","steps","heart"])
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
            st.error("you write wrong bruh, you need to write number and 115 is normal iq")
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
            st.error("you write wrong bruh, you need to write number and 18,5-24,9 is normal bmi")
with tabtestheartrate:
    st.header("test3.com")
    st.title("safe heartrate")
    heartrate=st.number_input("YoUr HeArTrAtE(bpm):",min_value=0.0,max_value=200.0,value=80.0,step=1.0)
    age=st.number_input("YoUr AgE:",min_value=0.0,max_value=100.0,value=18.0,step=1.0)
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
            st.error("you write wrong")
with tabteststeps:
    st.header("test2.com")
    st.title("appropriate number of steps per day")
    age2=st.number_input("YoUr AgE:",min_value=0.0,max_value=130.0,value=18.0,step=1.0)
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
            st.error("you write wrong")