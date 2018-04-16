from django.contrib import admin

# Register your models here.
from app01.models import Area,User

# class AreaInline(admin.StackedInline):
#     model = Area    # 关联子对象（多类对象）

class AreaInline(admin.TabularInline):
    model = Area    # 关联子对象（多类对象）
    # 预留空位
    extra = 2

class AreasAdmin(admin.ModelAdmin):
    list_display = ['id','title','parent_area']
    list_per_page = 10
    actions_on_top = False
    actions_on_bottom = True
    list_filter = ['title']
    search_fields = ['title']
    fields = ['parent','title']
    # 分组显示
    # fieldsets = (
    #     ('基本', {'fields': ('title',)}),
    #     ('高级', {'fields': ('parent',)}),
    # )
    inlines = [AreaInline]

admin.site.register(Area,AreasAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ['name','avent']

admin.site.register(User,UserAdmin)