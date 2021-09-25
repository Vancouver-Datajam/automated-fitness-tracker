import pandas as pd
import torch
import numpy as np
import torch.nn as nn
import Pre_processing


df = pd.read_csv(r'C:data/coords.csv')
df.drop(df.tail(10).index,inplace=True)

print(df.shape)

df_model = Pre_processing.Pre_process(df)


x = df_model.iloc[:,4:].to_numpy()
X = np.reshape(x,(-1,50,66)).astype(np.float)


n_hidden = 128
n_joints = 33*2
n_categories = 2
n_layer = 3

class LSTM(nn.Module):
    
    def __init__(self,input_dim,hidden_dim,output_dim,layer_num):
        super(LSTM,self).__init__()
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.lstm = torch.nn.LSTM(input_dim,hidden_dim,layer_num,batch_first=True)
        self.fc = torch.nn.Linear(hidden_dim,output_dim)
        self.bn = nn.BatchNorm1d(50)
        
    def forward(self,inputs):
        x = self.bn(inputs)
        lstm_out,(hn,cn) = self.lstm(x)
        out = self.fc(lstm_out[:,-1,:])
        return out

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

rnn = LSTM(n_joints,n_hidden,n_categories,n_layer)
rnn.to(device)
X=X.to(device)

rnn.load_state_dict(torch.load('C:/Users/austi/datajam/python-computer-vision/scripts/lstm_6_bn.pkl'))
rnn.eval()

prediction = rnn(X)

print(prediction)



