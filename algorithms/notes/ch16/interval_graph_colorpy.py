activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9),
              (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]

def assign_rooms(activities):
    rooms = [[(1, 4)]]
    for act in activities[1:]:
        for room in rooms:
            if act[0] >= room[-1][1]:
                room.append(act)
                break
        else:
            rooms.append([act])
    return rooms


rooms = assign_rooms(activities)
print(rooms)
