import tkinter as tk


def update_gui():
    # OBD-II 포트에서 정보를 읽어옵니다.
    # speed = obd.commands.SPEED.value
    # rpm = obd.commands.RPM.value
    # fuel = obd.commands.FUEL_LEVEL.value\

    speed = 40
    rpm = 50
    fuel = 40

    # GUI에 정보를 업데이트합니다.
    speed_label.configure(text="Speed: {}".format(speed))
    rpm_label.configure(text="RPM: {}".format(rpm))
    fuel_label.configure(text="Fuel level: {}".format(fuel))

    # 1초마다 GUI를 업데이트합니다.
    root.after(1000, update_gui)


# OBD-II 연결을 설정합니다.
# connection = obd.OBD()

# GUI를 생성합니다.
root = tk.Tk()

speed_label = tk.Label(root, text="Speed: ")
speed_label.pack()

rpm_label = tk.Label(root, text="RPM: ")
rpm_label.pack()

fuel_label = tk.Label(root, text="Fuel level: ")
fuel_label.pack()

# GUI를 업데이트합니다.
update_gui()

# Tkinter 이벤트 루프를 실행합니다.
root.mainloop()