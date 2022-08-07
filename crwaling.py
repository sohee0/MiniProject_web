import pymysql
import requests
import datetime

beachCodes = ['GYEONGPO', 'HAE', 'GORAEBUL', 'NAKSAN', 'DAECHON', 'MANGSANG', 'SOKCHO', 'SONGJUNG', 'IMRANG', 'JUNGMUN']

date = '20220%s%s' % (datetime.datetime.now().month, datetime.datetime.now().day)



def run(beachCode, date):
    params = {
        'ServiceKey': 'b38qqc2MYdXeRFQ5abrG8A==',
        'BeachCode': beachCode,
        'Date': date,
        'ResultType': 'json'
    }
    res = requests.get(
        'https://khoa.go.kr/api/oceangrid/ripCurrent/search.do',
        params=params)
    data = res.json()

    result = data['result']
    data2 = result['data']

    obs_time = data2[-1]['obs_time']
    air_temp = data2[-1]['air_temp']
    water_temp = data2[-1].get('water_temp')
    wind_speed = data2[-1]['wind_speed']
    wind_direct = data2[-1]['wind_direct']
    wave_height = data2[-1]['wave_height']
    wave_period = data2[-1]['wave_period']
    score = data2[-1]['score']
    score_msg = data2[-1]['score_msg']


    conn = pymysql.connect(host='15.164.153.191',
                           user='beach',
                           password='1234',
                           db='beach',
                           charset='utf8')

    sql = "INSERT INTO wave (id, obs_time, air_temp, water_temp, wind_speed, wind_direct, wave_height, wave_period, score, score_msg, beach_name) VALUES (null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, (obs_time, air_temp, water_temp, wind_speed, wind_direct, wave_height, wave_period, score, score_msg, beachCode))
            conn.commit()


# beachCodes = ['GYEONGPO', 'HAE', 'GORAEBUL', 'NAKSAN', 'DAECHON', 'MANGSANG', 'SOKCHO', 'SONGJUNG', 'IMRANG', 'JUNGMUN']
for beachCode in beachCodes:
    run(beachCode, date)

