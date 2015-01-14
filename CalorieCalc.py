class CalorieCalc:
    age = 0
    weight = 0
    height = 0
    gender = ""
    goal = ""
    activity_level = ""

    #Get user info from Yummly Driver
    def __init__(self, info):
        self.age = info.age
        self.weight = info.weight
        self.height = info.height
        self.gender = info.gender
        self.goal = info.goal
        self.activity_level = info.activity_level

    #Calculates user's BMI
    def get_bmi(self):
        bmi = ((self.weight * 703.0) / (self.height ** 2.0))
        bmi = round(bmi, 1)
        return bmi

    #Calculate user's BMR
    def get_bmr(self):
        if str(self.gender) == "Female":
            bmr = 655 + (4.35 * self.weight) + (4.7 * self.height) - (4.7 * self.age)
        elif str(self.gender) == "Male":
            bmr = 66 + (6.23 * self.weight) + (12.7 * self.height) - (6.8 * self.age)
        return bmr

    #Calculate user's caloric needs
    def get_calories(self):
        calories = 0
        bmr = self.get_bmr()
        #Use Harris-Benedict Equation to calculate daily energy expenditure
        if self.activity_level == "sedentary":
            calories = bmr * 1.2
        elif self.activity_level == "lightly active":
            calories = bmr * 1.375
        elif self.activity_level == "moderately active":
            calories = bmr * 1.55
        elif self.activity_level == "very active":
            calories = bmr * 1.725
        elif self.activity_level == "extra active":
            calories = bmr * 1.9

        #lose 2 pounds per week
        if self.goal == "Lose 2":
            calories -= 1000

        #lose 1 pound per week
        elif self.goal == "Lose 1":
            calories -= 500

        #lose 1/2 pound per week
        elif self.goal == "Lose 1/2":
            calories -= 250

        #gain 2 pounds per week
        elif self.goal == "Gain 2":
            calories += 1000

        #gain 1 pound per week
        elif self.goal == "Gain 1":
            calories += 500

        #gain 1/2 pound per week
        elif self.goal == "Gain 1/2":
            calories += 250

        #if BMI in normal range, maintain weight

        calories = int(calories)
        return calories

