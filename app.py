import streamlit as st
import pandas as pd
from binance.client import Client
st.set_page_config(page_icon= (":shark:"))

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

def view_count():
    @st.cache_resource()
    def Pageviews():
        return []
    pageviews=Pageviews()
    pageviews.append('dummy')
    try:
        st.markdown('Page viewed = {} times.'.format(len(pageviews)))
    except ValueError:
        st.markdown('Page viewed = {} times.'.format(1))
    return()

st.markdown("<h1 style='text-align: center; color: green;'>العملات الصاعدة</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: green;'> فريم اليوم </h1>", unsafe_allow_html=True)

cc='8d ago UTC'
d='1d'
aa=[]

info = Client(tld='us').get_exchange_info()
for c in info['symbols']:
    if c['quoteAsset']=='USDT' and c['status']=="TRADING":
        tt=(c['symbol'])
        aa.append(tt)


def get_data(a,d,cc):
    df=pd.DataFrame(Client(tld='us').get_historical_klines(a,d,cc))
    df=df.iloc[:,:6]
    df.columns=['time','open','high','low','close','volume']
    df=df.astype(float)
    df.time=pd.to_datetime(df['time'],unit='ms')
    df['low_p1']=df.low.shift(1)
    df['low_p2']=df.low.shift(2)
    df['low_p3']=df.low.shift(3)
    df['low_p4']=df.low.shift(4)
    df['high_p1']=df.high.shift(1)
    df['high_p2']=df.high.shift(2)
    df['high_p3']=df.high.shift(3)
    df['high_p4']=df.high.shift(4)
    df=df.dropna()
    return(df)


def test():
    for a in aa:
        df=get_data(a,d,cc)
        if  df['low_p1'].iloc[-1] > df['low_p2'].iloc[-1] >df['low_p3'].iloc[-1] > df['low_p4'].iloc[-1] and df['high_p1'].iloc[-1] > df['high_p2'].iloc[-1] > df['high_p3'].iloc[-1] > df['high_p4'].iloc[-1] :
            a
            # df['time'].iloc[-1]
    return()




txt=st.button('Start Test')
if txt:
    "..........برجاء الانتظار قليلا"
    tr=st.write(test())
else:
    pass

