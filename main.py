#TEMPLATES  feb 20 2017,Mon 6:56pm PRESIDENT'S DAY 4430GSWAY Matt6:1verse
import os
import webapp2#rgb(0,234,200) also use rgb(0,234,222,
import jinja2
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))
hidden_html = """
<input type ="hidden" name="food" value="%s"
"""
item_html = "<li>%s</li>"#this will be a list item, that goes inside the shopping_list_html
shopping_list_html = """
<br> <br>
<h2 style='color:white;background-color:rgb(234,13,156)'>Shopping List</h2>
<ul>
%s
</ul>
"""
class Handler (webapp2.RequestHandler):
    def write(self,*a,**kw):
        self.response.out.write(*a,**kw)

    def render_str(self,template,**params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render (self,template,**kw):
        self.write(self.render_str(template,**kw))

class MainPage(Handler):
    def get(self):
        n = self.request.get("n")
        if n:
            n = int(n)
        self.render("shopping_list.html", n=n)

        ##Using function named render instead of the code below
        # a="<h4 style='color:white;background-color:rgb(234,13,156);text-align:center''>Hello, Udacity !!!!<h4>"
        # self.write(a)
        # output = form_html
        # output_hidden =""#output_html will hold the content that is going # to be stuffed into %sFOR NOW ,it is an empty string ""
        # items = self.request.get_all("food")#gets all GET parameters and  #POST parameters of the same name "food"in the URL
        # if items:
        #     output_items = ""
        #     for item in items :
        #         output_hidden+= hidden_html % item#hidden_html refers to the HTML string %s that is going to  hold the hiden value.For every item in items, add to the string #output_hidden, the value os hidden_html, substituting the food name in item
        #         output_items+= item_html % item
        #     output_shopping = shopping_list_html % output_items
        #     output += output_shopping
        # output = output % output_hidden
        # self.write(output)
app = webapp2.WSGIApplication([('/',MainPage),
                                ],
                                debug=True)
