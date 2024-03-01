import requests
from datetime import datetime


def convert_amount_to_num(amount):
    return float(amount.replace("$", "").replace(",", ""))


def filter_by_date(data, monthYear_timestamp):
    result = []

    for dat in data:
        ts = datetime.utcfromtimestamp(dat['timestamp']/1000)
        ts_date = ts.strftime("%m-%Y")
        if ts_date == monthYear_timestamp:
            result.append(dat)

    print(result)
    return result


def get_average_monthly_txn(data, monthYear_timestamp):
    filtered_data = filter_by_date(data, monthYear_timestamp)

    total_amount = sum(convert_amount_to_num(data['amount']) for data in filtered_data)

    return total_amount / len(filtered_data) if filtered_data else 0


def get_txn_greater_than_monthly_average(data, monthYear_timestamp, monthly_average_spending):
    filtered_data = filter_by_date(data, monthYear_timestamp)
    return sorted((dat['id'] for dat in filtered_data if convert_amount_to_num(dat['amount']) >= monthly_average_spending), reverse=True)


def getUserTransaction(uid, txnType, monthYear):
    # Write your code here
    url = f"https://jsonmock.hackerrank.com/api/transactions/search?userId={uid}&txnType={txnType}"
    data = requests.get(url).json()['data']

    monthly_average_spending = get_average_monthly_txn(data, uid, txnType, monthYear)
    return get_txn_greater_than_monthly_average(data, uid, txnType, monthYear, monthly_average_spending)


uid = 1
txnType = 'debit'
monthYear = '05-2019'
print(getUserTransaction(uid, txnType, monthYear))




# from datetime import datetime
#
# input = '02-2019'
# dt = datetime.strptime(input, '%m-%Y')
# dt = dt.replace(day=1)
# timestamp_utc = int((dt-datetime(1970,1,1)).total_seconds())*1000
# print(timestamp_utc)
#
# sample = 1548979200090
# print(sample > timestamp_utc)


print('02-2019' == '02-2019')