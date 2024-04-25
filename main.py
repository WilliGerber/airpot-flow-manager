# Abrir o arquivo de texto no modo de leitura

from time import sleep


airplanesReady =   [
                        {"code": 918390, "send_signal":"00:00:00 04-11-2024"},
                        {"code": 293201, "send_signal":"01:00:00 04-11-2024"},
                        {"code": 883821, "send_signal":"02:00:00 04-11-2024"}
                    ]


for airplane in airplanesReady:
    airplane['waitingTime'] = 0

while True:
    for airplane in airplanesReady:
        airplane['waitingTime'] += 1
        print(airplane['waitingTime'])
    sleep(1)
    print(airplanesReady)
