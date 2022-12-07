from datetime import datetime


def write_csv(result: dict):
    f = open('/app/app/prices_test.csv', 'w')
    for list_values in result.get('prices'):
        time_without_ms = divmod(list_values[0], 1000)[0]
        f.write("%s,%s\n" % (datetime.utcfromtimestamp(time_without_ms).strftime('%Y-%m-%d %H:%M:%S'), list_values[1]))
