nr_bridges, nr_knites, team_memb = map(int, input().split(" "))

def hunt(nr_bridges, nr_knites, team_memb):
    teams = nr_knites // team_memb

    if teams < 1:
        return -1
    else:
        days = nr_bridges // teams
        left_bridges = nr_bridges % teams
        days += 1 if left_bridges > 1 else 0
        return days
