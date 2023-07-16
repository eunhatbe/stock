import pandas as pd
import plotly.graph_objects as go

# CSV 파일을 읽어옵니다. 파일 경로는 적절하게 수정하세요.
data = pd.read_csv("삼성전자2.csv", sep=",")

# 날짜 컬럼을 datetime 형식으로 변환합니다.
data['Date'] = pd.to_datetime(data['Date'])

# 필요한 컬럼만 추출합니다.
candle_data = data[['Date', 'Open', 'High', 'Low', 'Close']]

# 캔들스틱 차트 그리기
fig = go.Figure(data=[go.Candlestick(x=candle_data['Date'],
                                     open=candle_data['Open'],
                                     high=candle_data['High'],
                                     low=candle_data['Low'],
                                     close=candle_data['Close'])])

# 레이아웃 설정
fig.update_layout(title='삼성전자 주식차트',
                  xaxis_title='날짜',
                  yaxis_title='주가')

# 차트 표시
fig.show()
