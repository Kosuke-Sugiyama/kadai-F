from flask import Flask, render_template, request
import csv
import datetime
import os

app = Flask(__name__)


def main():
    if(os.path.isfile('bbs.csv') == False):
        with open('bbs.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["username", "message", "time"])


@app.route('/', methods=['POST', "GET"])
def bbs():
    bbs_list = []
    name = ""
    message = ""
    with open('bbs.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            bbs_dic = {}
            bbs_dic["name"] = row["username"]
            bbs_dic["message"] = row["message"]
            bbs_dic["time"] = row["time"]

            bbs_list.append(bbs_dic)

    if request.method == "GET":

        return render_template('bbs.html', username=name, umessage=message, message=bbs_list)

    if request.method == "POST":
        name = request.form['username']
        if name == "":
            name ="名無しさん"
        message = request.form['umessage']
        now = datetime.datetime.now()
        month = '{0:%m}月'.format(now)
        day = '{0:%m}日'.format(now)
        hour = '{0:%H}時'.format(now)
        minute = '{0:%M}分'.format(now)
        second = '{0:%M}秒'.format(now)
        time = f"{month}{day}{hour}{minute}{second}"

        bbs_dic = {}
        bbs_dic["name"] = name
        bbs_dic["message"] = message
        bbs_dic["time"] = time
        bbs_list.append(bbs_dic)
        with open('bbs.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([name, message, time])

    return render_template('bbs.html', username=name, umessage=message, message=bbs_list)


if __name__ == '__main__':
    main()
    app.run(debug=True, port=8888)
