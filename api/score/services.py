

def calculate_score(rolls: str):

    scores = [0 for i in range(10)]
    current_frame = 0
    first_attempt = True
    end_frame = False
    current_score = 0

    for index, roll in enumerate(rolls):
        pins = 0
        if first_attempt and roll == 'X':
            current_score = 10
            pins = 10
            end_frame = True

        if not first_attempt and roll == '/':
            pins = 10 - current_score
            current_score = 10
            end_frame = True

        if roll in '-123456789':
            pins = 0 if roll == '-' else int(roll)
            if first_attempt:
                current_score = pins
                first_attempt = False
            else:
                current_score += pins
                end_frame = True

        if index-2 >= 0 and rolls[index-2] == 'X' and current_frame-2 < 10:
            if first_attempt:
                scores[current_frame-2] += pins
            else:
                scores[current_frame-1] += pins

        if index-1 >= 0 and rolls[index-1] in 'X/' and current_frame-1 < 10:
            scores[current_frame-1] += pins

        if end_frame:

            if current_frame < 10:
                scores[current_frame] = current_score

            current_frame += 1
            end_frame = False
            first_attempt = True
            current_score = 0

    return sum(scores)