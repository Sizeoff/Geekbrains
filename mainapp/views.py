from django.shortcuts import render
from django.template import  Template, Context
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string

def index(request):
#    template = Template(
#        'Hello{{ name }}'
#    )
#    context = Context(
#       {'name': 'Anton'}
#    )
    template = get_template('main/index.html')
    context = {'name': 'ANTON'}
    return HttpResponse(template.render(context))

def main(request):
    return render(request, 'mainapp/index.html')

def katalog(request):
    return render(
        request,
        'mainapp/katalog.html',
        {'katalog_text': 'Здесь вы можете выбрать все, что придется вам по душе',
         'katalog_time': 'Сегодня: '}

    )

def contacts(request):
    rendered_page = render_to_string(
            'mainapp/contacts.html',
        {
            'contacts': ['контакт 1: ',
                         'контакт 2: ',
                         'контакт 3: +79992295565']
        }
    )
    return HttpResponse(rendered_page)

#    return render(request, 'mainapp/contacts.html')