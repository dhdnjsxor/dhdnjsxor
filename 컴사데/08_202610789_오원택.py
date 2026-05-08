bus_line = ['김수뭉', '이사슴', '박밀레']
bus_line.append('최자하')

bus_seat = ['구백년', '서교수']

bus_seat.append(bus_line.pop(0))
bus_seat.append(bus_line.pop(0))
bus_seat.append(bus_line.pop(0))
bus_seat.append(bus_line.pop(0))
print(bus_seat)
bus_seat.pop(0)
bus_seat.pop(0)
bus_seat.pop(0)
print(bus_seat)