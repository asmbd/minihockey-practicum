from flask import Flask
from practicum import find_mcu_boards, McuBoard, PeriBoard
from time import sleep

isPlaying = 0
count = 0
seconds = 0
scorePlayer2 = 0
scorePlayer1 = 0
isStop = 0

devs = find_mcu_boards()
app = Flask(__name__)

if len(devs) == 0:
    print("*** No practicum board found.")
    exit(1)

mcu = McuBoard(devs[0])
print("*** Practicum board found")
print("*** Manufacturer: %s" %
      mcu.handle.getString(mcu.device.iManufacturer, 256))
print("*** Product: %s" %
      mcu.handle.getString(mcu.device.iProduct, 256))
peri = PeriBoard(mcu)


@app.route("/player1")
def Player1():
    scorePlayer1 = str(peri.get_score1())
    print("Player 1: ", scorePlayer1)
    return scorePlayer1


@app.route("/player2")
def Player2():
    scorePlayer2 = str(peri.get_score2())
    print("Player 2: ", scorePlayer2)
    return scorePlayer2


@app.route("/getstatus")
def getStatus():
    isPlaying = peri.get_status()
    print("Playing: ", isPlaying)
    return str(isPlaying)


@app.route("/stopgame")
def stopGame():
    peri.set_status(0)
    isPlaying = 0
    return str(isPlaying)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
