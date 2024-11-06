from day15Main import resources

whatDoYouWant = ""
whatDoYouWant = input("Ne içmek istersiniz ? (espresso , latte , cappucino)")
if whatDoYouWant == "resource":
    for resor in resources:
        print(f"{resor} : {resources[resor]}")