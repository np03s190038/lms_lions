from django.contrib import admin
from .models import Books
from .models import Student
from .models import IssueBook
from .models import AddStudent


# Register your models here.


#class InventoryAdmin(admin.ModelAdmin):
 #   list_display = ["book_Name", "author_Name", "author_Image", "published_Date", "genre", "qunatity"]
  #  form = InventoryForm
   # list_filter = ['book_Name', 'author_Name']
    #search_fields = ['book_Name', 'author_Name']


admin.site.register(Books)
admin.site.register(Student)
admin.site.register(IssueBook)
admin.site.register(AddStudent)
