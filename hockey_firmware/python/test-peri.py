from practicum import find_mcu_boards, McuBoard, PeriBoard
from time import sleep

devs = find_mcu_boards()

if len(devs) == 0:
    print("*** No practicum board found.")
    exit(1)

mcu = McuBoard(devs[0])
print("*** Practicum board found")
print("*** Manufacturer: %s" % \
        mcu.handle.getString(mcu.device.iManufacturer, 256))
print("*** Product: %s" % \
        mcu.handle.getString(mcu.device.iProduct, 256))
peri = PeriBoard(mcu)

count = 0

seconds = 0
isLoop = 0
scorePlayer2 = 0
scorePlayer1 = 0
while True:
    if seconds == 0:
        isLoop = peri.get_status()
    scorePlayer1 = peri.get_score1()
    scorePlayer2 = peri.get_score2()
    minutes = 0
    if isLoop == 1:
        seconds = 59
        isLoop = 0
    print("TIME: %d : %d | Player 1: %d / Player 2: %d" % (minutes, seconds, scorePlayer1,scorePlayer2))
    if seconds > 0:
        seconds -= 1
    if (seconds == 0):
        peri.set_status(0)
        scorePlayer2 = 0
        scorePlayer1 = 0


    sleep(1)


