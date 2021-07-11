class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        def split_time(input_time):
            hour, minute = input_time.split(":")
            return int(hour), int(minute)

        def norm_start_time(input_hour, input_min):
            i_block = input_min // 15
            min_left = input_min % 15
            if min_left > 0:
                i_block += 1
            return input_hour * 4 + i_block

        def norm_end_time(input_hour, input_min):
            i_block = input_min // 15
            return input_hour * 4 + i_block

        start_hour, start_min = split_time(startTime)
        end_hour, end_min = split_time(finishTime)
        nr_gone_games = norm_start_time(start_hour, start_min)
        nr_all_games = norm_end_time(end_hour, end_min)

        if start_hour > end_hour or ( start_hour == end_hour and start_min > end_min ):
            return 96 - nr_gone_games + nr_all_games
        else:
            return nr_all_games - nr_gone_games


sol = Solution()
cases = [
    {
        "start": "12:01",
        "end": "12:44",
        "expect": 1
    },
    {
        "start": "12:01",
        "end": "14:44",
        "expect": 9
    },
    {
        "start": "0:0",
        "end": "23:44",
        "expect": 92
    },
    {
        "start": "0:10",
        "end": "23:44",
        "expect": 91
    },
    {
        "start": "23:00",
        "end": "0:0",
        "expect": 4
    },
    {
        "start": "23:06",
        "end": "0:11",
        "expect": 3
    },
    {
        "start": "20:00",
        "end": "6:0",
        "expect": 40
    }

]
for case in cases:
    print(case["start"], case["end"], sol.numberOfRounds(case["start"], case["end"]))
