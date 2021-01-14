def solution(skill, skill_trees):
    answer = len(skill_trees)
    for i in skill_trees:
        l = 0
        for j in range(len(i)):
            if i[j] not in skill :
                print(i)
                continue;
            else:
                if len(skill) > l:
                    if i[j] == skill[l]:
                        print(i[j])
                        l+=1
                    else:
                        answer-=1
                        break;
    return answer
