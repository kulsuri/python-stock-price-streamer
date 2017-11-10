# modules
import zmq
import datetime
import plotly.plotly as ply
from plotly.graph_objs import *
import plotly.tools as pls

# plotly stream token
#stream_ids = pls.get_credentials_file()['stream_ids']
stream_ids = ['r2enzqwm9h']

# socket
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://10.50.0.119:5555')
socket.setsockopt_string(zmq.SUBSCRIBE, '')

# plotly
s = Stream(maxpoints=100, token=stream_ids[0])
t = Scatter(x=[], y=[], name='tick data', mode='lines+markers', stream=s)
d = Data([t])
l = Layout(title='Tick Data Stream')
f = Figure(data=d, layout=l)
ply.plot(f, filename='amazon_live_plot', auto_open=True)

st = ply.Stream(stream_ids[0])
st.open()

while True:
    msg = socket.recv_string()
    t = datetime.datetime.now()
    sym, value = msg.split()
    print('hellow world')
    print(str(t) + '  |  ' + msg)
    st.write({'x': t, 'y': float(value)})