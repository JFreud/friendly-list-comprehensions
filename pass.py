def pass_check(password):
    caps = [True for x in password if x.isupper()]
    naps = [True for x in password if x.islower()]
    nums = [True for x in password if x.isdigit()]
    return True in caps and True in naps and True in nums

def pass_quality(password):
    pass_points = 0
    punc = ".?!&#,;:-_*"
    pass_points += 1 if True in [True for x in password if x.isupper()] else 0
    pass_points += 1 if True in [True for x in password if x.islower()] else 0
    pass_points += 1 if True in [True for x in password if x.isdigit()] else 0
    pass_points += len([x for x in password if x in punc])
    pass_points += len(password) / 4
    return 10 if pass_points > 10 else pass_points

if __name__ == "__main__":
    print str(pass_check("Gh2")) + " should be True"
    print str(pass_check("gh2")) + " should be False"
    print str(pass_check("GH2")) + " should be False"
    print str(pass_check("GHt")) + " should be False"
    print pass_quality("diannao")
    print pass_quality("Diannao")
    print pass_quality("DianNao")
    print pass_quality("D1ANNao")
    print pass_quality("D!anNa0")
    print pass_quality("D!anNa0D!anNa0")
    print pass_quality("D!anNa0D!anNa0D!anNa0D!anNa0")
