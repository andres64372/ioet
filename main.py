def get_intervals(name_1, name_2):
    return {
        "1":{
            "start": int(name_1["start"].split(":")[0])*60 + int(name_1["start"].split(":")[1]),
            "end": int(name_1["end"].split(":")[0])*60 + int(name_1["start"].split(":")[1])
        },
        "2":{
            "start": int(name_2["start"].split(":")[0])*60 + int(name_2["start"].split(":")[1]),
            "end": int(name_2["end"].split(":")[0])*60 + int(name_2["start"].split(":")[1])
        }
    }

def combinate(data: list):
    return [
        [data[i],data[j]]
        for i in range(len(data))
        for j in range(i+1,len(data))
    ]

def decode(lines: str):
    data = {}
    for line in lines:
        name = line.split('=')[0]
        times = line.split('=')[1].replace('\n','').split(',')
        data[name] = []
        for time in times:
            day = time[0:2]
            start = time[2:].split('-')[0]
            end = time[2:].split('-')[1]
            data[name].append({"day": day, "start": start, "end": end})
    return data

def calculate(data: dict):
    output = []
    names = list(data.keys())
    pairs = combinate(names)
    for pair in pairs:
        matches = 0
        names_1 = data[pair[0]]
        names_2 = data[pair[1]]
        for name_1 in names_1:
            for name_2 in names_2:
                if name_1['day'] == name_2['day']:
                    intervals = get_intervals(name_1, name_2)
                    if intervals["1"]["end"] >= intervals["2"]["start"] and intervals["1"]["start"] <= intervals["2"]["end"]:
                        matches+=1
                    elif intervals["2"]["end"] >= intervals["1"]["start"] and intervals["2"]["start"] <= intervals["1"]["end"]:
                        matches+=1
        output.append(f"{pair[0]}-{pair[1]}: {matches}\n")
    return output

def main(lines: list):
    data = decode(lines)
    output = calculate(data)
    return output

if __name__ == '__main__':
    with open('inputs.txt','r') as f:
        lines = f.readlines()
    data = []
    for line in lines:
        if line.startswith('INPUT'):
            if data:
                output = main(data)
                print('INPUT')
                print(''.join(data))
                print('OUTPUT')
                print(''.join(output))
                print('\n-----------')
                data = []
        else:
            data.append(line)