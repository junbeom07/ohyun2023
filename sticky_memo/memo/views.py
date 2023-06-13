from django.shortcuts import render, HttpResponse
from memo.models import Memo

def get_all_memo(request):
    memo_list = Memo.objects.all()

    context = {"memos":memo_list}
    return render(request, "memo_list.html", context)