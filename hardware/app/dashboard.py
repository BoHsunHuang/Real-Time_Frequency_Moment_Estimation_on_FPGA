from reg_defines_reference_nic import *
from param import *
from read_freq import *
from read_entropy import *
from collections import deque
import time
import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
import webbrowser
from threading import Timer
from scipy.special import gamma
#C + Python
from ctypes import *

time_interval_sec = 10
time_interval = time_interval_sec*1000
time_interval_name = 'Time Interval ({} sec/Interval)'.format(time_interval_sec)
exe_time = 0

#Up to 3000 intervals
entropy_srcip_array               = deque(maxlen=3000)
entropy_dstip_array               = deque(maxlen=3000)
entropy_srcport_array             = deque(maxlen=3000)
entropy_dstport_array             = deque(maxlen=3000)
entropy_protocol_array            = deque(maxlen=3000)
f2_srcip_array                    = deque(maxlen=3000)
f2_dstip_array                    = deque(maxlen=3000)
f2_srcport_array                  = deque(maxlen=3000)
f2_dstport_array                  = deque(maxlen=3000)
f2_protocol_array                 = deque(maxlen=3000)
#f3_srcip_array                    = deque(maxlen=3000)
#f3_dstip_array                    = deque(maxlen=3000)
#f3_srcport_array                  = deque(maxlen=3000)
#f3_dstport_array                  = deque(maxlen=3000)
#f3_protocol_array                 = deque(maxlen=3000)
#f4_srcip_array                    = deque(maxlen=3000)
#f4_dstip_array                    = deque(maxlen=3000)
#f4_srcport_array                  = deque(maxlen=3000)
#f4_dstport_array                  = deque(maxlen=3000)
#f4_protocol_array                 = deque(maxlen=3000)
distinct_srcip_array              = deque(maxlen=3000)
distinct_dstip_array              = deque(maxlen=3000)
distinct_srcport_array            = deque(maxlen=3000)
distinct_dstport_array            = deque(maxlen=3000)
pkt_count_array                   = deque(maxlen=3000)
weibull_k_array_srcip             = deque(maxlen=3000)
theta_array_srcip                 = deque(maxlen=3000)
weibull_k_array_dstip             = deque(maxlen=3000)
theta_array_dstip                 = deque(maxlen=3000)

entropy_srcip               = 0
entropy_dstip               = 0
entropy_srcport             = 0
entropy_dstport             = 0
entropy_protocol            = 0
f2_srcip                    = 0
f2_dstip                    = 0
f2_srcport                  = 0
f2_dstport                  = 0
f2_protocol                 = 0
f3_srcip                    = 0
f3_dstip                    = 0
f3_srcport                  = 0
f3_dstport                  = 0
f3_protocol                 = 0
f4_srcip                    = 0
f4_dstip                    = 0
f4_srcport                  = 0
f4_dstport                  = 0
f4_protocol                 = 0
distinct_srcip              = 0
distinct_dstip              = 0
distinct_srcport            = 0
distinct_dstport            = 0
pkt_count                   = 0
weibull_k                   = 0
theta                       = 0
mean                        = 0
var                         =0          
#----------------test---------------
X                           = deque(maxlen=10000)
X.append(1)
#-----------------------------------


######COLOR FOR HTML######

colors = {
    'plotcolor' : '#111111',
    'background': '#111111',
    'text': '#FFFFFF'
}


app = dash.Dash(__name__)
app.layout = html.Div(
    [
        html.H1(children='Statistical Information Live Update',style={'textAlign': 'center','color': colors['text']}),
        dcc.Graph(id='entropy-live-graph', animate=True),
        dcc.Graph(id='f2-live-graph', animate=True),
        dcc.Graph(id='pkt-count-graph', animate=True),
        dcc.Graph(id='distinct-graph', animate=True),
        #dcc.Graph(id='shape-graph', animate=True),
        #dcc.Graph(id='scale-graph', animate=True),
        dcc.Interval(id='graph-update',interval=time_interval,n_intervals = 0),
    ], style={'backgroundColor': colors['background']}
)

@app.callback(
        dash.dependencies.Output('entropy-live-graph', 'figure'),
        dash.dependencies.Output('f2-live-graph', 'figure'),
        dash.dependencies.Output('pkt-count-graph', 'figure'),
        dash.dependencies.Output('distinct-graph', 'figure'),
        #dash.dependencies.Output('shape-graph', 'figure'),
        #dash.dependencies.Output('scale-graph', 'figure'),
        [dash.dependencies.Input('graph-update', 'n_intervals')]
    )
def update_graph_scatter(n):
    
    X.append(X[-1]+1)


    entropy_srcip, entropy_dstip, entropy_srcport, entropy_dstport,  entropy_protocol, distinct_srcip, distinct_dstip, distinct_srcport, distinct_dstport,  pkt_count= read_entropy()
    f2_srcip, f2_dstip, f2_srcport, f2_dstport, f2_protocol, f3_srcip, f3_dstip, f3_srcport, f3_dstport, f3_protocol, f4_srcip, f4_dstip, f4_srcport, f4_dstport, f4_protocol = read_freq()
    entropy_srcip_array.append(entropy_srcip)
    entropy_dstip_array.append(entropy_dstip)
    entropy_srcport_array.append(entropy_srcport)
    entropy_dstport_array.append(entropy_dstport)
    entropy_protocol_array.append(entropy_protocol)
    distinct_srcip_array.append(distinct_srcip)
    distinct_dstip_array.append(distinct_dstip)
    distinct_srcport_array.append(distinct_srcport)
    distinct_dstport_array.append(distinct_dstport)
    pkt_count_array.append(pkt_count)
      

    if(pkt_count>0):
        f2_srcip_array.append(f2_srcip/pow(pkt_count,2))
        f2_dstip_array.append(f2_dstip/pow(pkt_count,2))
        f2_srcport_array.append(f2_srcport/pow(pkt_count,2))
        f2_dstport_array.append(f2_dstport/pow(pkt_count,2))
        f2_protocol_array.append(f2_protocol/pow(pkt_count,2))
        #mean = pkt_count / distinct_srcip
        #var = (f2_srcip / distinct_srcip) - mean**2
        #weibull_k = (mean / (var**0.5))**(1.086)
        #theta = mean/gamma(1+1/weibull_k)
        #weibull_k_array_srcip.append(weibull_k)
        #theta_array_srcip.append(theta)

        #mean = pkt_count / distinct_dstip
        #var = (f2_dstip / distinct_dstip) - mean**2
        #weibull_k = (mean / (var**0.5))**(1.086)
        #theta = mean/gamma(1+1/weibull_k)
        #weibull_k_array_dstip.append(weibull_k)
        #theta_array_dstip.append(theta)
    else:
        f2_srcip_array.append(np.nan)
        f2_dstip_array.append(np.nan)
        f2_srcport_array.append(np.nan)
        f2_dstport_array.append(np.nan)
        f2_protocol_array.append(np.nan)
        #weibull_k_array_srcip.append(np.nan)
        #theta_array_srcip.append(np.nan)
        #weibull_k_array_dstip.append(np.nan)
        #theta_array_dstip.append(np.nan)

    #f3_srcip_array.append(f3_srcip)
    #f3_dstip_array.append(f3_dstip)
    #f3_srcport_array.append(f3_srcport)
    #f3_dstport_array.append(f3_dstport)
    #f3_protocol_array.append(f3_protocol)
    #f4_srcip_array.append(f4_srcip)
    #f4_dstip_array.append(f4_dstip)
    #f4_srcport_array.append(f4_srcport)
    #f4_dstport_array.append(f4_dstport)
    #f4_protocol_array.append(f4_protocol)
    #print(pkt_count)
    ######################ENTROPY###########################
    plot_entropy_srcip_array = plotly.graph_objs.Scatter(
                                            x=list(X),
                                            y=list(entropy_srcip_array),
                                            name='Src IP Entropy',
                                            mode= 'lines',
                                            line=dict(color='#70f3ff'),
                                            )# setting 
    plot_entropy_dstip_array = plotly.graph_objs.Scatter(
                                            x=list(X),
                                            y=list(entropy_dstip_array),
                                            name='Dst IP Entropy',
                                            mode= 'lines',
                                            line=dict(color='#ff3333'),
                                            )# setting 
    plot_entropy_srcport_array = plotly.graph_objs.Scatter(
                                            x=list(X),
                                            y=list(entropy_srcport_array),
                                            name='Src Port Entropy',
                                            mode= 'lines',
                                            line=dict(color='#6f33ff'),
                                            )# setting    
    plot_entropy_dstport_array = plotly.graph_objs.Scatter(
                                            x=list(X),
                                            y=list(entropy_dstport_array),
                                            name='Dst Port Entropy',
                                            mode= 'lines',
                                            line=dict(color='#e0e7b6'),
                                            )# setting  
    plot_entropy_protocol_array = plotly.graph_objs.Scatter(
                                            x=list(X),
                                            y=list(entropy_protocol_array),
                                            name='Protocol Entropy',
                                            mode= 'lines',
                                            line=dict(color='#81ea60'),
                                            )# setting
      
    ######################F2###########################
    plot_f2_srcip_array = plotly.graph_objs.Scatter(
                                            x=list(X),
                                            y=list(f2_srcip_array),
                                            name='Src IP F2',
                                            mode= 'lines',
                                            line=dict(color='#70f3ff'),
                                            )# setting 
    plot_f2_dstip_array = plotly.graph_objs.Scatter(
                                            x=list(X),
                                            y=list(f2_dstip_array),
                                            name='Dst IP F2',
                                            mode= 'lines',
                                            line=dict(color='#ff3333'),
                                            )# setting 
    plot_f2_srcport_array = plotly.graph_objs.Scatter(
                                            x=list(X),
                                            y=list(f2_srcport_array),
                                            name='Src Port F2',
                                            mode= 'lines',
                                            line=dict(color='#6f33ff'),
                                            )# setting    
    plot_f2_dstport_array = plotly.graph_objs.Scatter(
                                            x=list(X),
                                            y=list(f2_dstport_array),
                                            name='Dst Port F2',
                                            mode= 'lines',
                                            line=dict(color='#e0e7b6'),
                                            )# setting  
    plot_f2_protocol_array = plotly.graph_objs.Scatter(
                                            x=list(X),
                                            y=list(f2_protocol_array),
                                            name='Protocol F2',
                                            mode= 'lines',
                                            line=dict(color='#81ea60'),
                                            )# setting
    ######################PKT COUNT###########################
    plot_pkt_array = plotly.graph_objs.Scatter(
                                            x=list(X),
                                            y=list(pkt_count_array),
                                            name='Packet Count',
                                            mode= 'lines',
                                            line=dict(color='#19d3f3'),
    )

    #####################DISTINCT COUNT########################
    plot_distinct_srcip_array = plotly.graph_objs.Scatter(
                                            x=list(X),
                                            y=list(distinct_srcip_array),
                                            name='Src IP Distinct',
                                            mode= 'lines',
                                            line=dict(color='#70f3ff'),
                                            )# setting 
    plot_distinct_dstip_array = plotly.graph_objs.Scatter(
                                            x=list(X),
                                            y=list(distinct_dstip_array),
                                            name='Dst IP Distinct',
                                            mode= 'lines',
                                            line=dict(color='#ff3333'),
                                            )# setting 
    plot_distinct_srcport_array = plotly.graph_objs.Scatter(
                                            x=list(X),
                                            y=list(distinct_srcport_array),
                                            name='Src Port Distinct',
                                            mode= 'lines',
                                            line=dict(color='#6f33ff'),
                                            )# setting    
    plot_distinct_dstport_array = plotly.graph_objs.Scatter(
                                            x=list(X),
                                            y=list(distinct_dstport_array),
                                            name='Dst Port Distinct',
                                            mode= 'lines',
                                            line=dict(color='#e0e7b6'),
                                            )# setting  #
    ######################### SHAPE ###########################
    #plot_shape_srcip_array = plotly.graph_objs.Scatter(
    #                                        x=list(X),
    #                                        y=list(weibull_k_array_srcip),
    #                                        name='Src IP',
    #                                        mode= 'lines',
    #                                        line=dict(color='#70f3ff'),
    #                                        )# setting 
    #plot_shape_dstip_array = plotly.graph_objs.Scatter(
    #                                        x=list(X),
    #                                        y=list(weibull_k_array_dstip),
    #                                        name='Dst IP',
    #                                        mode= 'lines',
    #                                        line=dict(color='#ff3333'),
    #                                        )# setting 
    ######################### SCALE ###########################
    #plot_scale_srcip_array = plotly.graph_objs.Scatter(
    #                                        x=list(X),
    #                                        y=list(theta_array_srcip),
    #                                        name='Src IP',
    #                                        mode= 'lines',
    #                                        line=dict(color='#70f3ff'),
    #                                        )# setting 
    #plot_scale_dstip_array = plotly.graph_objs.Scatter(
    #                                        x=list(X),
    #                                        y=list(theta_array_dstip),
    #                                        name='Dst IP',
    #                                        mode= 'lines',
    #                                        line=dict(color='#ff3333'),
    #                                        )# setting 

    #######################################################################
    #                           SETTING GRAPH                             #
    #######################################################################

    graph1= {'data': [plot_entropy_srcip_array,plot_entropy_dstip_array,plot_entropy_srcport_array,plot_entropy_dstport_array,plot_entropy_protocol_array],
            'layout' : go.Layout(
                                            title= 'FPGA Entropy',
                                            xaxis=dict(range=[min(X),max(X)],title= time_interval_name),
                                            yaxis=dict(range=[0,1],title= 'Entropy'),
                                            font={'color':colors['text']},
                                            plot_bgcolor = colors['background'],
                                            paper_bgcolor = colors['background'],
                                            barmode='group',
                                            bargap=0,
                                            bargroupgap=0,
                                            #width=1280,
                                            #height=720,
                                            showlegend=True)}
    graph2= { 'data': [plot_f2_srcip_array,plot_f2_dstip_array,plot_f2_srcport_array,plot_f2_dstport_array,plot_f2_protocol_array,
                                            ],'layout' : go.Layout(title= 'FPGA F2 Normalized Value',
                                            xaxis=dict(range=[min(X),max(X)],title= time_interval_name),
                                            yaxis=dict(range=[0,1],title= 'F2 Normalized value'),
                                            font={'color':colors['text']},
                                            barmode='group',
                                            bargap=0,
                                            bargroupgap=0,
                                            plot_bgcolor = colors['background'],
                                            paper_bgcolor = colors['background'],
                                            #width=1280,
                                            #height=720,
                                            showlegend=True
                                            )}
    graph3= { 'data': [plot_pkt_array],'layout' : go.Layout(title= 'Packet Count Value',
                                            xaxis=dict(range=[min(X),max(X)],title= time_interval_name),
                                            yaxis=dict(title= 'pkt_count'),
                                            font={'color':colors['text']},
                                            barmode='group',
                                            bargap=0,
                                            bargroupgap=0,
                                            plot_bgcolor = colors['background'],
                                            paper_bgcolor = colors['background'],
                                            #width=1280,
                                            #height=720,
                                            showlegend=True
                                            )}
    graph4= {'data': [plot_distinct_srcip_array,plot_distinct_dstip_array,plot_distinct_srcport_array,plot_distinct_dstport_array,
                                            ],'layout' : go.Layout(
                                            title= 'FPGA Distinct Count',
                                            xaxis=dict(range=[min(X),max(X)],title= time_interval_name),
                                            yaxis=dict(title= 'Distinct Count'),
                                            font={'color':colors['text']},
                                            plot_bgcolor = colors['background'],
                                            paper_bgcolor = colors['background'],
                                            barmode='group',
                                            bargap=0,
                                            bargroupgap=0,
                                            #width=1280,
                                            #height=720,
                                            showlegend=True)}   
    #graph5= { 'data': [plot_shape_srcip_array,plot_shape_dstip_array,
    #                                        ],'layout' : go.Layout(title= 'SHAPE',
    #                                        xaxis=dict(range=[min(X),max(X)],title= time_interval_name),
    #                                        yaxis=dict(range=[0,1],title= 'weibull k value'),
    #                                        font={'color':colors['text']},
    #                                        barmode='group',
    #                                        bargap=0,
    #                                        bargroupgap=0,
    #                                        plot_bgcolor = colors['background'],
    #                                        paper_bgcolor = colors['background'],
    #                                        #width=1280,
    #                                        #height=720,
    #                                        showlegend=True
    #                                        )}
    #graph6= { 'data': [plot_scale_srcip_array,plot_scale_dstip_array,
    #                                        ],'layout' : go.Layout(title= 'SCALE',
    #                                        xaxis=dict(range=[min(X),max(X)],title= time_interval_name),
    #                                        yaxis=dict(range=[0,1],title= 'theta value'),
    #                                        font={'color':colors['text']},
    #                                        barmode='group',
    #                                        bargap=0,
    #                                        bargroupgap=0,
    #                                        plot_bgcolor = colors['background'],
    #                                        paper_bgcolor = colors['background'],
    #                                        #width=1280,
    #                                        #height=720,
    #                                        showlegend=True
    #                                        )}                                            
    return [graph1, graph2, graph3, graph4]
    #return [graph2, graph3, graph4]
    #return [graph2, graph5, graph6]
    #return [graph4]

     
    
    

def open_browser():
    webbrowser.open_new("http://localhost:{}".format(8050))    

if __name__ == '__main__':

    Timer(1,open_browser).start()
    app.run_server(debug=False, use_reloader=False)



    #print ('#############################')
    #print ('#       Read Entropy{:>3d}     #'.format(exe_time))
    #print ('#############################\n')

    #entropy_srcip, entropy_dstip, entropy_srcport, entropy_dstport,  entropy_protocol, distinct_srcip, distinct_dstip, distinct_srcport, distinct_dstport, pkt_count = read_entropy()
    #print ('#############################')
    #print ('#       Read Moment{:>3d}      #'.format(exe_time))
    #print ('#############################\n')
    #f2_srcip, f2_dstip, f2_srcport, f2_dstport, f2_protocol, f3_srcip, f3_dstip, f3_srcport, f3_dstport, f3_protocol, f4_srcip, f4_dstip, f4_srcport, f4_dstport, f4_protocol = read_freq()
    #
    #print ('---  SrcIP Std = {:.3f}  ---  '.format(std_srcip),end='')
    #print ('SrcIP Skew = {:.3f}  ---  '.format(skew_srcip),end='')
    #print ('SrcIP Kurt = {:.3f}'.format(kurt_srcip))

