data = sorted(open("input.txt").read().split("\n"))
outputs = {}
bots = {}

def get_bot(id):
    if id not in bots:
        bots[id] = {"value": None}
    return bots[id]

def get_output(id):
    if id not in outputs:
        outputs[id] = []
    return outputs[id]

def add_bot(id, low_type, low_id, high_type, high_id):
    bot = get_bot(id)
    bot["low"] = get_bot(low_id) if low_type == "bot" else get_output(low_id)
    bot["high"] = get_bot(high_id) if high_type == "bot" else get_output(high_id)

def insert_into_target(target, value):
    if "value" in target:
        insert_into_bot(target, value)
    else:
        target.append(value)

def insert_into_bot(bot, value):
    hand_value = bot["value"]
    if hand_value is not None:
        lower_value = min(hand_value, value)
        upper_value = max(hand_value, value)
        bot["value"] = None

        insert_into_target(bot["low"], lower_value)
        insert_into_target(bot["high"], upper_value)
    else:
        bot["value"] = value

for line in data:
    split = line.split()
    if split[0] == "bot":
        add_bot(int(split[1]), split[5], int(split[6]), split[10], int(split[11]))
    elif split[0] == "value":
        bot_id = int(split[-1])
        bot = get_bot(bot_id)
        value = int(split[1])
        insert_into_bot(bot, value)

print(outputs[0][0] * outputs[1][0] * outputs[2][0])
