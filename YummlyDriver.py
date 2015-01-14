from yummly import Client

from CalorieCalc import CalorieCalc


class YummlyApiInfo:
    def __init__(self):
        pass

    #Vi's Key
    Id = '17f360b5'
    Key = '214819cbde16a118c615fc0061e6dc8b'

    # Erik's Key
    #Id = '1db8b5cc'
    #Key = 'd470fadf2ef7bdcaec50be759255006a'

    #Mark's Key
    #Id= '694cee2e'
    #Key = '392df3bc63518ea410eef68eb6da066e'

    #Greg's Key
    #Id = 'c406a4d1'
    #Key = '654c0671661c94a799e761615c36cdd5'


#Object that contains all user information
#As well as any search options
class RecipeQueryParameters:
    def __init__(self):
        pass

    # include measurements & user info
    ignore_user_preferences = False
    age = 0
    height = 0
    weight = 0
    gender = ""
    goal = ""
    activity_level = ""
    meals_left = 3
    diabetic = False
    calories_consumed = 0

    q = ""
    start = 0
    maxResult = 25
    requirePictures = False
    allowed_ingredients = []
    excluded_ingredients = []
    facet_field = []
    allowed_diet = []
    allergies = []
    max_total_time_in_seconds = 0

    # Flavor stuff
    sweet_min_flavor = 0.0
    sweet_max_flavor = 0.0
    meaty_min_flavor = 0.0
    meaty_max_flavor = 0.0
    sour_min_flavor = 0.0
    sour_max_flavor = 0.0
    bitter_min_flavor = 0.0
    bitter_max_flavor = 0.0
    piquant_min_flavor = 0.0
    piquant_max_flavor = 0.0

    # Nutrition stuff
    min_fat = 0
    max_fat = 0
    min_sodium = 0
    max_sodium = 0
    min_cholesterol = 0
    max_cholesterol = 0
    min_fat_sat = 0
    max_fat_sat = 0
    min_carbs = 0
    max_carbs = 0
    min_fiber = 0
    max_fiber = 0
    min_protein = 0
    max_protein = 0
    min_vitamin_c = 0
    max_vitamin_c = 0
    min_calcium = 0
    max_calcium = 0
    min_iron = 0
    max_iron = 0
    min_sugar = 0
    max_sugar = 0
    min_calories = 0
    max_calories = 0
    min_vitamin_a = 0
    max_vitamin_a = 0
    min_trans_fat = 0
    max_trans_fat = 0

    #Creates a dictionary of all search options, so they can be passed to Yummly API
    def to_dictionary(self):
        return_dictionary = {}
        if self.q != "":
            return_dictionary["q"] = self.q
        if self.start > 0:
            return_dictionary['start'] = self.start
        if self.maxResult != 40:
            return_dictionary['maxResult'] = self.maxResult
        if self.requirePictures:
            return_dictionary['requirePictures'] = True
        if len(self.allowed_ingredients) > 0:
            return_dictionary['allowedIngredient[]'] = self.allowed_ingredients
        if len(self.excluded_ingredients) > 0:
            return_dictionary['excludedIngredient[]'] = self.excluded_ingredients
        if len(self.facet_field) > 0:
            return_dictionary['facetField[]'] = self.facet_field
        if len(self.allowed_diet) > 0:
            return_dictionary['allowedDiet[]'] = self.allowed_diet
        if len(self.allergies) > 0:
            return_dictionary['allowedAlergy[]'] = self.allergies,
        if self.max_total_time_in_seconds > 0:
            return_dictionary['maxTotalTimeInSeconds'] = self.max_total_time_in_seconds
        if self.sweet_min_flavor > 0.0:
            return_dictionary['flavor.sweet.min'] = self.sweet_min_flavor
        if self.sweet_max_flavor > 0.0:
            return_dictionary['flavor.sweet.max'] = self.sweet_max_flavor
        if self.meaty_min_flavor > 0.0:
            return_dictionary['flavor.meaty.min'] = self.meaty_min_flavor
        if self.meaty_max_flavor > 0.0:
            return_dictionary['flavor.meaty.max'] = self.meaty_max_flavor
        if self.sour_min_flavor > 0.0:
            return_dictionary['flavor.sour.min'] = self.sour_min_flavor
        if self.sour_max_flavor > 0.0:
            return_dictionary['flavor.sour.max'] = self.sour_max_flavor
        if self.bitter_min_flavor > 0.0:
            return_dictionary['flavor.bitter.min'] = self.bitter_min_flavor
        if self.bitter_max_flavor > 0.0:
            return_dictionary['flavor.bitter.max'] = self.bitter_max_flavor
        if self.piquant_min_flavor > 0.0:
            return_dictionary['flavor.piquant.min'] = self.piquant_min_flavor
        if self.piquant_max_flavor > 0.0:
            return_dictionary['flavor.piquant.max'] = self.piquant_max_flavor
        if self.min_fat > 0.0:
            return_dictionary['nutrition.FAT.min'] = self.min_fat
        if self.max_fat > 0.0:
            return_dictionary['nutrition.FAT.max'] = self.max_fat
        if self.min_sodium > 0.0:
            return_dictionary['nutrition.NA.min'] = self.min_sodium
        if self.max_sodium > 0.0:
            return_dictionary['nutrition.NA.max'] = self.max_sodium
        if self.min_cholesterol > 0.0:
            return_dictionary['nutrition.CHOLE.min'] = self.min_cholesterol
        if self.max_cholesterol > 0.0:
            return_dictionary['nutrition.CHOLE.max'] = self.max_cholesterol
        if self.min_fat_sat > 0.0:
            return_dictionary['nutrition.FATSAT.min'] = self.min_fat_sat
        if self.max_fat_sat > 0.0:
            return_dictionary['nutrition.FATSAT.max'] = self.max_fat_sat
        if self.min_carbs > 0.0:
            return_dictionary['nutrition.CHOCDF.min'] = self.min_carbs
        if self.min_carbs > 0.0:
            return_dictionary['nutrition.CHOCDF.max'] = self.max_carbs
        if self.min_fiber > 0.0:
            return_dictionary['nutrition.FIBTG.min'] = self.min_fiber
        if self.max_fiber > 0.0:
            return_dictionary['nutrition.FIBTG.max'] = self.max_fiber
        if self.min_protein > 0.0:
            return_dictionary['nutrition.PROCNT.min'] = self.min_protein
        if self.max_protein > 0.0:
            return_dictionary['nutrition.PROCNT.max'] = self.max_protein
        if self.min_vitamin_c > 0.0:
            return_dictionary['nutrition.VITC.min'] = self.min_vitamin_c
        if self.max_vitamin_c > 0.0:
            return_dictionary['nutrition.VITC.max'] = self.max_vitamin_c
        if self.min_calcium > 0.0:
            return_dictionary['nutrition.CA.min'] = self.min_calcium
        if self.max_calcium > 0.0:
            return_dictionary['nutrition.CA.max'] = self.max_calcium
        if self.min_iron > 0.0:
            return_dictionary['nutrition.FE.min'] = self.min_iron
        if self.max_iron > 0.0:
            return_dictionary['nutrition.FE.max'] = self.max_iron
        if self.min_sugar > 0.0:
            return_dictionary['nutrition.SUGAR.min'] = self.min_sugar
        if self.max_sugar > 0.0:
            return_dictionary['nutrition.SUGAR.max'] = self.max_sugar
        if self.min_calories > 0.0:
            return_dictionary['nutrition.ENERC_KCAL.min'] = self.min_calories
        if self.max_calories > 0.0:
            return_dictionary['nutrition.ENERC_KCAL.max'] = self.max_calories
        if self.min_vitamin_a > 0.0:
            return_dictionary['nutrition.VITA_IU.min'] = self.min_vitamin_a
        if self.max_vitamin_a > 0.0:
            return_dictionary['nutrition.VITA_IU.max'] = self.max_vitamin_a
        if self.min_trans_fat > 0.0:
            return_dictionary['nutrition.FATRN.min'] = self.min_trans_fat
        if self.max_trans_fat > 0.0:
            return_dictionary['nutrition.FATRN.max'] = self.max_trans_fat

        return return_dictionary


#Uses Yummly API to search for recipes
def search_recipes(recipe_query_parameters):
    # passed in partial recipe parameters object

    #if "ignore user preferences" option  is not selected, calculate nutritional requirements
    if not recipe_query_parameters.ignore_user_preferences:
        # call calculator to figure out desired meals
        calc = CalorieCalc(recipe_query_parameters)

        # calculate max calories for meal
        recipe_query_parameters.max_calories = calc.get_calories() - recipe_query_parameters.calories_consumed

        if recipe_query_parameters.meals_left > 0:
            recipe_query_parameters.max_calories /= recipe_query_parameters.meals_left

        #diabetic info
        if recipe_query_parameters.diabetic:
            recipe_query_parameters.max_carbs = 65
            recipe_query_parameters.min_carbs = 45
            recipe_query_parameters.max_sodium = 0.4

    # have yummly driver query data
    client = Client(api_id=YummlyApiInfo.Id, api_key=YummlyApiInfo.Key)
    recipe_query_parameters.q = recipe_query_parameters.allowed_ingredients[0]
    return_dictionary = recipe_query_parameters.to_dictionary()
    return client.search(**return_dictionary)


#Get's search parameters from Django
def django_query_to_parameter_object(post_data_dictionary, user):
    parameter_object = RecipeQueryParameters()
    #putting included ingredients into a list
    if len(post_data_dictionary['in_ingredients']):
        parameter_object.allowed_ingredients = [x.strip() for x in post_data_dictionary['in_ingredients'].split(',')]
    #putting excluded ingredients into a list
    if len(post_data_dictionary['ex_ingredients']):
        parameter_object.excluded_ingredients = [x.strip() for x in post_data_dictionary['ex_ingredients'].split(',')]
    #converting the prep-time from a string into an integer
    if len(post_data_dictionary['prep_time']):
        parameter_object.max_total_time_in_seconds = int(post_data_dictionary['prep_time'])
    #saving mix and max sweetness, shifting decimal point for conversion purposes
    if len(post_data_dictionary['amount-sweetness']):
        sweetness = post_data_dictionary['amount-sweetness'].split('-')
        parameter_object.sweet_min_flavor = float(sweetness[0]) / 10.00
        parameter_object.sweet_max_flavor = float(sweetness[1]) / 10.00
    #saving min and max meatiness, shifting the decimal point for conversion purposes
    if len(post_data_dictionary['amount-meatiness']):
        meatiness = post_data_dictionary['amount-meatiness'].split('-')
        parameter_object.meaty_min_flavor = float(meatiness[0]) / 10.00
        parameter_object.meaty_max_flavor = float(meatiness[1]) / 10.00
    #saving min and max sourness, shifting the decimal point for conversion purposes
    if len(post_data_dictionary['amount-sourness']):
        sourness = post_data_dictionary['amount-sourness'].split('-')
        parameter_object.sour_min_flavor = float(sourness[0]) / 10.00
        parameter_object.sour_max_flavor = float(sourness[1]) / 10.00
    #saving min and max bitterness, shifting the decimal point for conversion purposes
    if len(post_data_dictionary['amount-bitterness']):
        bitterness = post_data_dictionary['amount-bitterness'].split('-')
        parameter_object.bitter_min_flavor = float(bitterness[0]) / 10.00
        parameter_object.bitter_max_flavor = float(bitterness[1]) / 10.00
    #saving min and max spicyness, shifting the decimal point for conversion purposes
    if len(post_data_dictionary['amount-spicyness']):
        spicyness = post_data_dictionary['amount-spicyness'].split('-')
        parameter_object.piquant_min_flavor = float(spicyness[0]) / 10.00
        parameter_object.piquant_max_flavor = float(spicyness[1]) / 10.00

    #checks to see if we are ignoring user preferences, if so skip to the return
    #else assign additional information from user preferences
    if post_data_dictionary.has_key('ignore_user_preferences'):
        parameter_object.ignore_user_preferences = True
    else:
        if len(post_data_dictionary['current_weight']):
            parameter_object.weight = int(post_data_dictionary['current_weight'])

        if len(post_data_dictionary['calories_consumed']):
            parameter_object.calories_consumed = int(post_data_dictionary['calories_consumed'])

        parameter_object.meals_left = int(post_data_dictionary['num_meals'])

        parameter_object.age = user.age
        parameter_object.gender = user.gender
        parameter_object.activity_level = user.activity_level.level
        parameter_object.allowed_diet = user.yummlydiet.searchValue
        parameter_object.allergies = user.allergies.all()
        parameter_object.diabetic = user.diabetic
        parameter_object.goal = user.goal.goal
        parameter_object.height = user.height

    return parameter_object
