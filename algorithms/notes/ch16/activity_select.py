activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9),
              (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]

def dp_select(activities, i, j, s, f, track_m):
    if i > j:
        return 0
    best_arrange = 0
    for activity_id in range(i, j+1):
        arrange = 0
        print("checking: {} to {}".format(i, j))
        if activities[activity_id][0] >= s and activities[activity_id][1] <= f:
            print("k fit: {}".format(activity_id))
            arrange = dp_select(activities, i, activity_id-1, s, activities[activity_id][0], track_m) + \
                     1 + \
                     dp_select(activities, activity_id+1, j, activities[activity_id][1], f, track_m)
        if arrange > best_arrange:
            track_m[i][j] = activity_id
            best_arrange = arrange
    return best_arrange

track_m = [[None] * len(activities) for _ in range(len(activities))]
best_arrange = dp_select(activities, 0, len(activities) - 1, 0, 16, track_m)
print(best_arrange)
for row in track_m:
    print(row)

while n is not None:
    trace = track_m[0][10]
    print(trace)
