from django.shortcuts import render
import csv


def get_inflation_info():
    inflation_info = []
    title_info = []
    with open('inflation_russia.csv', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)
        for line in reader:
            for key, val in line.items():
                inflation = [elem if elem else "-" for elem in val.split(';')]
                inflation_info.append(inflation)
            for elem in line:
                title_info = [tit for tit in elem.split(";")]
                break
    return inflation_info, title_info


inflation_title = get_inflation_info()[1]
inflation_list = get_inflation_info()[0]


def inflation_view(request):
    template_name = 'inflation.html'
    title_info = inflation_title
    context = {
        'title_info': title_info,
        'inflation_list': inflation_list,
    }
    return render(request, template_name, context)
