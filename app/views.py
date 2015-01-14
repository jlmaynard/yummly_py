#This is where all the views sit for pyum. If you're talking to the server, you talk here.
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from django_tables2 import RequestConfig
from django.contrib.auth.models import User

import app.tables
from app.forms import UserForm, UserFormWithoutLogin, AppUserForm, RecipeSearchForm
from app.models import AppUser
import YummlyDriver


#Register view
#This is the get and post for registering a user.
def register(request):
    registered = False

    if request.method == 'POST':
        #Get the relevant data from the post
        request.POST["username"] = request.POST["username"].lower()
        user_form = UserForm(data=request.POST)
        profile_form = AppUserForm(data=request.POST)

        #If the user is valid and they registered correctly, save
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        #Otherwise, throw back the errors
        else:
            print user_form.errors, profile_form.errors
    else:
        #Pull the forms for the get
        user_form = UserForm()
        profile_form = AppUserForm()

    #render the page with the forms
    return render(request, 'app/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


#User login view.
#If posting, check to make sure the can login
#If getting, return the login page
def user_login(request):
    #If posting, we're logging someone in
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        #Try to authenticate
        user = authenticate(username=username, password=password)

        #If he is a user
        if user is not None:
            #And they're active
            if user.is_active:
                #log em in and put em at the home page
                login(request, user)
                return render(request, 'app/home.html', {})
            #they aren't active
            else:
                return HttpResponse("Your Pyum account is disabled.")
        #they aren't a user
        else:
            print "Invalid login details: {0}".format(username)
            return HttpResponse("Invalid login details supplied.")
    #If getting, just show the page
    else:
        return render(request, 'app/login.html', {})


#This is when we are actually going to search for recipes through Yummly. We then store the results in session
def search_for_recipes(request):
    #Xreate Parameter Query for Yummly API
    parameters = YummlyDriver.django_query_to_parameter_object(request.POST, request.user.appuser)
    #Query for the matches
    results = YummlyDriver.search_recipes(parameters).matches
    #Store results in session
    request.session['results'] = results


#This is to take any recipe data found in the session and return the results in a bound table.
def bind_data_to_table(request):
    #Data from session
    result_data = list(request.session['results'])
    #Map to table data
    table_data = app.tables.map_from_result_list(result_data)
    #Bind to a new table
    table = app.tables.ResultTable(table_data)
    #Uh...not sure, I think this is for sorting specified in the query string
    RequestConfig(request).configure(table)
    #Return the table
    return table


#Search for recipe view
#If getting, return the page and table with any data stored in session
#If posting, take post data and turn it into a yummly query. get back the data, store it in session, and refresh the page.
def search_recipes(request):
    #If they're logged in
    if request.user.is_authenticated():
        #If they're posting
        if request.method == "POST":
            #Search for recipes
            search_for_recipes(request)

        #Putting any relevant values in the search_form inputs
        search_form = RecipeSearchForm(initial=request.GET)

        #Blank table
        table = []
        #If we don't have any results in session
        if not request.session.has_key('results'):
            #Bind a table with no results.
            table = app.tables.ResultTable([])
        #Otherwise, bind the results
        else:
            table = bind_data_to_table(request)

        #return the page with the relevant data populated
        return render(request, 'recipes.html', {'table': table, 'search_form': search_form})
    #They aren't logged in
    else:
        #Kick em to the login page.
        return render(request, 'app/login.html', {})


#Home View
def home(request):
    #If they're logged in
    if request.user.is_authenticated():
        #Send em the home page
        return render(request, 'app/home.html', {})
    #If they're not logged in
    else:
        #Kick em to the login page
        return render(request, 'app/login.html', {})


#User Logout View
#It does exactly what it says. Logs them out, then sends them to the login page
def user_logout(request):
    logout(request)
    return render(request, 'app/login.html', {})


#Here is where we are saving a user.
def save_user(request):
    #grab all that post data
    post_data = request.POST
    #So if the user didn't want to change their password, we're going to put it in the post data so it isn't changed
    #to blank
    if request.POST['password'] == "":
        post_data['password'] = request.user.password

    #Grab the data from the forms
    user_form = UserFormWithoutLogin(data=post_data, instance=User.objects.get(pk=request.user.id))
    profile_form = AppUserForm(data=post_data, instance=AppUser.objects.get(pk=request.user.appuser.id))

    #If everthing is valid, save all the data.
    if user_form.is_valid() and profile_form.is_valid():
        user = user_form.save()
        user.set_password(user.password)
        user.save()
        profile = profile_form.save()
        profile.save()
    #Return the forms
    return profile_form, user_form


#This is all the data that was filled out by the user when registering
def get_data_for_user(request):
    initial_user_data = {'email': request.user.email}
    initial_app_user_data = {
        'yummlydiet': request.user.appuser.yummlydiet,
        'allergies': request.user.appuser.allergies.all(),
        'age': request.user.appuser.age,
        'gender': request.user.appuser.gender,
        'height': request.user.appuser.height,
        'diabetic': request.user.appuser.diabetic,
        'activity_level': request.user.appuser.activity_level,
        'goal': request.user.appuser.goal}
    #Populate the forms with this data
    user_form = UserFormWithoutLogin(initial=initial_user_data)
    profile_form = AppUserForm(initial=initial_app_user_data)
    #return the filled out forms
    return profile_form, user_form


#This is the view for the profile page
#If Posting, we're updating the user.
#If Getting, we're pulling back the page with the user's data
def profile(request):
    #If they aren't logged in, kick them to the login page
    if not request.user.is_authenticated():
        return render(request, 'app/login.html', {})

    #initializing the forms
    user_form = UserFormWithoutLogin()
    profile_form = AppUserForm()

    #Posting, attempt to save the user
    if request.method == 'POST':
        profile_form, user_form = save_user(request)
    #Getting, load the user data
    else:
        profile_form, user_form = get_data_for_user(request)

    #Render the page
    return render(request, 'app/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


#About page View, just renders the page
def about(request):
    return render(request, 'app/about.html', {})