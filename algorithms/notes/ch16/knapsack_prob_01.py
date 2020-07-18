max_weight = 100
goods = [(10, 60), (20, 100), (25, 108), (30, 120), (40, 130), (50, 200), (60, 220)]

def dp_rec(goods_left, weight_avail):
    # recur problem
    if not goods_left:
        return 0
    good = goods_left[0]
    if good[0] <= weight_avail:
        v_with = good[1] + dp_rec(goods_left[1:], weight_avail - good[0])
        v_without = dp_rec(goods_left[1:], weight_avail)
        if v_with > v_without:
            value = v_with
            print("good: {} => left weigth {}, value with {}:  goods {}".format(good, weight_avail - good[0], value, goods_left[1:]))
        else:
            value = v_without
            print("good: {} => left weigth {}, value without {}:  goods {}".format(good, weight_avail, value, goods_left[1:]))
        return value
    else:
        return 0

best_value = dp_rec(goods, max_weight)
print(best_value)
