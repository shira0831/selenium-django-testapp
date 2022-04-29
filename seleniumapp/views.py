from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .chrome_driver import *
from .models import *

# Create your views here.


class IndexViews(View):

    def get(self,request):
        print('get!!')
        params = {}
        params["data"] = Lancers.objects.all()
        print(params)
        return render(request,'base.html',params)

    def post(self,request):
        print('post!!')

        target = request.POST.getlist('btn')

        if str(target[0]) == 'delete':
            print('削除します')
            # DB全て削除
            Lancers.objects.all().delete()
            return redirect('index')

        else:
            print('スクレイピングボタンが押されました')
        
            chrome_driver = ChromeDriver()
            chrome_driver.open_url(
            "https://www.lancers.jp/work/search?open=1&ref=header_menu")

            data = []

            blocks = chrome_driver.get_blocks('.c-media__content')

            for block in blocks:

                details = {
                    'title': chrome_driver.get_text_from_block(block, '.c-media__title'),
                    'url': chrome_driver.get_url_from_block(block, '.c-media__title'),
                    'contributor': chrome_driver.get_text_from_block(block,'.c-avatar__note'),
                    'url2': chrome_driver.get_url_from_block(block, '.c-avatar__note > a')
                }
                print(details)
                data.append(details)
                
            
            for d in data:
                Lancers.objects.create(**d)
            print('DB登録!')

            chrome_driver.close_driver()
            return redirect('index')

