import MySQLdb
import req_cls


conn = MySQLdb.connect('localhost', 'root', '123456', 'btc_hour')
cursor = conn.cursor()

array = req_cls.RequestPrice(10, 2)

for i in range(len(array.final_response)):
    price = array[i]
    time = price.get('time')
    close = price.get('close')
    high = price.get('high')
    low = price.get('low')
    open_p = price.get('open')
    col = 0 if (open_p - close) < 0 else 1  # 0 is green candle, 1 is red candle
    volume = price.get('volumeto')
    min_delta = abs(open_p - close)
    max_delta = abs(high - low)
    sql = 'INSERT INTO btc_price (time, open, close, high, low, color, volume, min_delta, max_delta) ' \
          'VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {})'.format(time, open_p, close, high, low,
                                                               col, volume, min_delta, max_delta)
    cursor.execute(sql)
    conn.autocommit('on')


