from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_main = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            try:
                if form.cleaned_data['is_main']:
                    count_main += 1
            except Exception:
                raise ValidationError('Удалите пустые разделы')
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        if count_main > 1:
            raise ValidationError('Основным может быть только один раздел')
        elif count_main == 0:
            raise ValidationError('Выберите хотя бы один основной раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset




@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [RelationshipInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
