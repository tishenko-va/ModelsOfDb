from django.contrib import admin
from .models import Game, Buyer, News

# Фильтрацию по полям size и cost.
# Отображение полей title, cost и size при отображении всех полей списком.
# Поиск по полю title.
# Ограничение кол-ва записей до 20.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')
    list_filter = ('size', 'cost')
    search_fields = ('title',)
    list_per_page = 20

# Фильтрацию по полям balance и age.
# Отображение полей name, balance и age при отображении всех полей списком.
# Поиск по полю name.
# Ограничение кол-ва записей до 30.
# Доступным только для чтения поле balance.
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    list_filter = ('balance', 'age')
    search_fields = ('name',)
    list_per_page = 30
    readonly_fields = ('balance',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title', )
    list_per_page = 3
    readonly_fields = ('date',)






