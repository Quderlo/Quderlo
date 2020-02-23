from django.utils import timezone
from .models import Post
from .models import Table
from .models import Table_cells
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect


# TODO: удалить views, которые не используеются, в том числе все из курсе django girl

def submit(request):
    dic = request.POST
    print(dic['m'])
    print(dic['n'])
    if ('cell' in dic):
        print(dic['cell'])
        Table_cells.cell = dic['cell']
        Table_cells.n = dic['n']
        Table_cells.m = dic['m']
    return render(request, 'blog/sub_form.html', {'n': dic['n'], 'm': dic['m'], 'cell': dic['cell']})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def table_list(request):
    tables = Table.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'blog/table_list.html', {'tables': tables})


def table_list_n_m(request):
    tables = Table.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'blog/table_list_n_m.html', {'tables': tables})


def submit_n_m(request):
    if request.method == "GET":
        tables = Table.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
        return render(request, 'blog/table_list_n_m.html', {'tables': tables})

    if request.method == "POST":
        mem = request.POST

        # TODO: Заполнить эти переменные из запроса
        # n = None
        n = mem['n']
        # m = None
        m = mem['m']
        # text_from_cell = None
        cell_changed = mem['cell_changed']
        # table_id = None НЕ ЗНАЮ ПОКА
        table_id = mem.get("table_id")

        # TODO: Распечатать тут все, что пришло в POST
        print(mem)
        print('n = ', n, end= ' ')
        print('m = ', m, end=' ')
        print('cell_changed = ', cell_changed, end=' ')
        print("table_id={}".format(table_id))

        # TODO: проверить, есть ли уже в базе
        # Table_cells с такими же n,m и таблицей
        # заполнить переменную

        is_cell_exists = Table_cells.objects.filter(table__id=table_id, n=n, m=m).count()
        print(is_cell_exists)
        if is_cell_exists:
            # print("Существует")
            # TODO: перезаписать у текущей ячейки параметр .cell
            table = Table.objects.get(id=table_id)
            new_cell = Table_cells.objects.update(n=n, m=m, cell=cell_changed, table=table)
            # сохранить ее
        else:
            print("Не Существует")
            # создать новый объект Table_cells
            table = Table.objects.get(id=table_id)
            new_cell = Table_cells.objects.create(n=n, m=m, cell=cell_changed, table=table)
            new_cell.save()

        tables = Table.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
        return render(request, 'blog/table_list_n_m.html', {'tables': tables})
