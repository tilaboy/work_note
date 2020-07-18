activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9),
              (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]

def dp_arr(activities, i, j, s, f, best_arr, track_m):
    if i > j:
        return 0
    best_arrange = 0
    if best_arr[s][f] is not None:
        return best_arr[s][f]
    for activity_id in range(i, j+1):
        arrange = 0
        #print("checking: {} to {}".format(i, j))
        if activities[activity_id][0] >= s and activities[activity_id][1] <= f:
            #print("k fit: {}".format(activity_id))
            arrange = dp_arr(activities, i, activity_id-1, s, activities[activity_id][0], best_arr, track_m) + \
                     1 + \
                     dp_arr(activities, activity_id+1, j, activities[activity_id][1], f, best_arr, track_m)
            if arrange > best_arrange:
                best_arrange = arrange
                best_arr[s][f] = best_arrange
                track_m[s][f] = activities[activity_id]
    #print("s: {}, f: {} => {}".format(s, f, track_m[s][f]))
    return best_arrange

def dp_select(activities):
    best_arr = [[None] * 17 for _ in range(16)]
    track_m = [[None] * 17 for _ in range(16)]
    best_arrange = dp_arr(activities, 0, len(activities) - 1, 0, 16, best_arr, track_m)
    print(best_arrange)
    for row in track_m:
        print(row)


def greedy_select(activities):
    sorted_activities = sorted(activities, key=lambda x: x[1])
    print(sorted_activities)
    current_act = sorted_activities[0]
    print("\tadd: {}".format(current_act))

    total_acts = 1
    for activity in sorted_activities[1:]:
        if activity[0] >= current_act[1]:
            print("\tadd: {}".format(activity))
            total_acts += 1
            current_act = activity
    print("total_acts: {}".format(total_acts))

def greedy_select_recur(activities):

    def recur_greedy(activities, i, start):
        while i < len(activities):
            if activities[i][0] >= start:
                print('add: {}, start: {}'.format(activities[i], start))
                return recur_greedy(activities, i + 1, activities[i][1]) + 1
            i += 1
        else:
            return 0

    sorted_activities = sorted(activities, key=lambda x: x[1])
    print(recur_greedy(sorted_activities, 0, 0))


def greedy_rev(activities):
    sorted_activities = sorted(activities, reverse=True, key=lambda x: x[0])
    print(sorted_activities)
    total_acts = 1
    cur_act = sorted_activities[0]
    print("\tadd: {}".format(cur_act))
    for act in sorted_activities[1:]:
        if act[1] < cur_act[0]:
            print("\tadd: {}".format(act))
            total_acts += 1
            cur_act = act
    print(total_acts)


greedy_rev(activities)
