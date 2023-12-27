from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/user/machineconfig', methods=['POST'])
def machineconfig():
    # You can add logic here to handle the form data for ipconfig
    post_data = request.form.get('post')

    if post_data == '3':
        return jsonify({"error":0,"data":{},"message":""})

    if post_data != '1':
        return jsonify({"error": 0, "message": ""})
    
    # Mock response data for ipconfig
    response_data_ipconfig = {
          "error": 0,
          "data": {
            "pools": [
              {
                "no": 1,
                "addr": "stratum+tcp://kheavyhash.auto.nicehash.com:9200",
                "user": "NHb...L6D",
                "pass": "x",
                "connect": False,
                "diff": "0.00 G",
                "priority": 1,
                "accepted": 0,
                "rejected": 0,
                "diffa": 0,
                "diffr": 0,
                "state": 0,
                "lsdiff": 0,
                "lstime": "00:00:00"
              },
              {
                "no": 2,
                "addr": "stratum+tcp://asia-kas.2miners.com:2323",
                "user": "kaspa:qqp...jzj",
                "pass": "x",
                "connect": True,
                "diff": "70368.74 G",
                "priority": 2,
                "accepted": 16,
                "rejected": 2,
                "diffa": 0,
                "diffr": 0,
                "state": 1,
                "lsdiff": 0,
                "lstime": "00:00:00"
              },
              {
                "no": 3,
                "addr": "stratum+tcp://us-kas.2miners.com:2323",
                "user": "kaspa:qqp...jzj",
                "pass": "x",
                "connect": False,
                "diff": "0.00 G",
                "priority": 3,
                "accepted": 0,
                "rejected": 0,
                "diffa": 0,
                "diffr": 0,
                "state": 0,
                "lsdiff": 0,
                "lstime": "00:00:00"
              }
            ],
            "ratio": 1,
            "mode": 1
          },
          "message": ""
        }

    return jsonify(response_data_ipconfig)

@app.route('/user/ipconfig', methods=['POST'])
def ipconfig():
    # You can add logic here to handle the form data for ipconfig
    post_data = request.form.get('post')

    if post_data != '1':
        return jsonify({"error": 0, "message": ""})
    
    # Mock response data for ipconfig
    response_data_ipconfig = {
        "error": 0,
        "data": {
            "nic": "eth0",
            "mac": "52-8c-03-36-ec-e7",
            "ip": "192.168.1.16",
            "netmask": "255.255.255.0",
            "host": "petalinux_config13",
            "dhcp": False,
            "gateway": "192.168.1.1",
            "dns": "192.168.1.1"
        },
        "message": ""
    }

    return jsonify(response_data_ipconfig)

@app.route('/user/userpanel', methods=['POST'])
def userpanel():
    # You can add logic here to handle the form data for userpanel
    post_data = request.form.get('post')

    if post_data != '4':
        return jsonify({"error": 0, "message": ""})
    
    # Mock response data for userpanel
    response_data_userpanel = {
        "error": 0,
        "data": {
          "model": "none",
          "algo": "none",
          "online": True,
          "firmver1": "BOOT_2_0.BIN",
          "firmver2": "image_1.0",
          "softver1": "5977449_ks3m_miner",
          "softver2": "5977449_ks3m_bg",
          "firmtype": "Factory",
          "nic": "eth0",
          "mac": "52-8c-03-36-ec-e7",
          "ip": "192.168.1.16",
          "netmask": "255.255.255.0",
          "host": "petalinux_config13",
          "dhcp": False,
          "gateway": "192.168.1.1",
          "dns": "192.168.1.1",
          "locate": False,
          "rtpow": "6226G",
          "avgpow": "6308G",
          "reject": 2.403846,
          "runtime": "00:09:36:02",
          "unit": "G",
          "pows": {
            "board1": [
              6135,
              6120,
              6212,
              6076,
              6439,
              6113,
              6160,
              6421,
              6039,
              6036,
              6135,
              6135,
              6289,
              6274,
              6311,
              6322,
              6212,
              6318,
              6358,
              6149,
              6362,
              6435,
              6226
            ]
          },
          "pows_x": [
            "0 mins",
            "5 mins",
            "10 mins",
            "15 mins",
            "20 mins",
            "25 mins",
            "30 mins",
            "35 mins",
            "40 mins",
            "45 mins",
            "50 mins",
            "55 mins",
            "60 mins",
            "65 mins",
            "70 mins",
            "75 mins",
            "80 mins",
            "85 mins",
            "90 mins",
            "95 mins",
            "100 mins",
            "105 mins",
            "110 mins"
          ],
          "powstate": True,
          "netstate": True,
          "fanstate": True,
          "tempstate": True,
          "fans": [
            1028,
            1028,
            1028,
            1072
          ],
          "pools": [
            {
              "no": 1,
              "addr": "stratum+tcp://kheavyhash.auto.nicehash.com:9200",
              "user": "NHb...L6D",
              "pass": "x",
              "connect": False,
              "diff": "0.00 G",
              "priority": 1,
              "accepted": 0,
              "rejected": 0,
              "diffa": 0,
              "diffr": 0,
              "state": 0,
              "lsdiff": 0,
              "lstime": "00:00:00"
            },
            {
              "no": 2,
              "addr": "stratum+tcp://asia-kas.2miners.com:2323",
              "user": "kaspa:qqp...jzj",
              "pass": "x",
              "connect": True,
              "diff": "70368.74 G",
              "priority": 2,
              "accepted": 3058,
              "rejected": 76,
              "diffa": 0,
              "diffr": 0,
              "state": 1,
              "lsdiff": 0,
              "lstime": "00:00:00"
            },
            {
              "no": 3,
              "addr": "stratum+tcp://us-kas.2miners.com:2323",
              "user": "kaspa:qqp...jzj",
              "pass": "x",
              "connect": False,
              "diff": "0.00 G",
              "priority": 3,
              "accepted": 0,
              "rejected": 0,
              "diffa": 0,
              "diffr": 0,
              "state": 0,
              "lsdiff": 0,
              "lstime": "00:00:00"
            }
          ],
          "boards": [
            {
              "no": 1,
              "chipnum": 18,
              "chipsuc": 0,
              "error": 0,
              "freq": 875,
              "rtpow": "2151.38G",
              "avgpow": "2146.49G",
              "idealpow": "0.00G",
              "tempnum": "(null)",
              "pcbtemp": "0.00-0.00-0.00-0.00",
              "intmp": 26,
              "outtmp": 49,
              "state": True,
              "false": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18
              ]
            },
            {
              "no": 2,
              "chipnum": 18,
              "chipsuc": 0,
              "error": 0,
              "freq": 875,
              "rtpow": "2114.73G",
              "avgpow": "2104.34G",
              "idealpow": "0.00G",
              "tempnum": "(null)",
              "pcbtemp": "0.00-0.00-0.00-0.00",
              "intmp": 25,
              "outtmp": 126,
              "state": True,
              "false": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18
              ]
            },
            {
              "no": 3,
              "chipnum": 18,
              "chipsuc": 0,
              "error": 0,
              "freq": 875,
              "rtpow": "1960.80G",
              "avgpow": "2057.92G",
              "idealpow": "0.00G",
              "tempnum": "(null)",
              "pcbtemp": "0.00-0.00-0.00-0.00",
              "intmp": 26,
              "outtmp": 49,
              "state": True,
              "false": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18
              ]
            }
          ],
          "refTime": "2023-04-14 01:21:51 UTC"
        },
        "message": ""
    }
    return jsonify(response_data_userpanel)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
