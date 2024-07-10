
def flatten(all_target=[ 1,[2,[3]] ]):
    res = []
    def process(target):
        for item in target:
            if not isinstance(item, list):
                res.append(item)
            else:
                process(item)
    process(all_target)
    return res

print(flatten())