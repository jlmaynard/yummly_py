import django_tables2 as tables
from django.utils.safestring import mark_safe
from django.utils.html import escape


#This is the class that will define what each row in the table will look like
class TableRow:
    id = ""
    name = ""
    image = []
    courses = ""
    cuisines = ""
    holidays = ""
    link = []
    rating = 0
    attributes = []
    prep_time = float(0)

    #Set the appropriate fields, this is the mapping from a yummly search result to our row
    def __init__(self, search_result):
        self.id = search_result['id']
        self.name = search_result['recipeName']
        self.link = ["http://www.yummly.com/recipe/" + self.id, self.name]
        self.rating = search_result['rating']
        self.attributes = search_result['attributes']

        self.prep_time = search_result['totalTimeInSeconds']

        if len(search_result['smallImageUrls']) > 0:
            self.image = ["http://www.yummly.com/recipe/" + self.id, search_result['smallImageUrls'][0]]

        if self.attributes.has_key("course"):
            self.courses = ', '.join(str(x) for x in self.attributes["course"])

        if self.attributes.has_key("cuisine"):
            self.cuisines = ', '.join(str(x) for x in self.attributes["cuisine"])

        if self.attributes.has_key("holiday"):
            self.holidays = ', '.join(str(x) for x in self.attributes["holiday"])


#Map the results into a list of table rows
def map_from_result_list(results):
    return_list = []
    [return_list.append(TableRow(result)) for result in results]
    return return_list


# noinspection PyMethodMayBeStatic
#This is the class for the actual table
class ResultTable(tables.Table):
    # Here is when you define the column types by the attributes
    image = tables.TemplateColumn('{{ record.image }}')
    link = tables.URLColumn()
    rating = tables.Column()
    prep_time = tables.Column()
    courses = tables.Column()
    cuisines = tables.Column()
    holidays = tables.Column()

    # Meta properties, or properties relating to the table itself not the data
    class Meta:
        attrs = {"class": "paleblue", 'min-width': '582px'}

    #I believe that this takes each method that is below and runs them to render the table correctly.
    #Don't touch what you don't understand!
    def __init__(self, *args, **kwargs):
        super(ResultTable, self).__init__(*args, **kwargs)

    #Rendering the image column
    def render_image(self, value):
        if len(value) > 0:
            return mark_safe(u'<a href="{0}"><img src="{1}"/></a>'.format(escape(value[0]), escape(value[1])))

    #Render the link, It's the recipes name with yummly's direct link as the href
    def render_link(self, value):
        link = u'<a href="{0}">{1}</a>'.format(escape(value[0]), escape(value[1]))

        x = link.encode("utf-8")
        return mark_safe(x)

    #Render Rating
    def render_rating(self, value):
        return value

    #Render Prep Time
    def render_prep_time(self, value):
        return "%.0f" % (value / 60)