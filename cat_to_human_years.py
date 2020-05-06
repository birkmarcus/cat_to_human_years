def human_years(cat_years):
    youth_multi = 8
    grown_multi = 4
    first_years = 4

    if cat_years >= first_years:
        youth = first_years * youth_multi
        grown = (cat_years - first_years) * grown_multi
        return youth + grown
    return youth * cat_years

rerun = True
while rerun == True:
    cat_years = int(input("Cat age: "))
    print(f"Your cat is {human_years(cat_years)} in human years")
    if input("Calculate new cat? (y/n)") == "n":
        rerun = False
    