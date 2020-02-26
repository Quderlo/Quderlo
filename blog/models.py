from django.conf import settings
from django.utils import timezone
from django.db import models
# TODO: удалить модели, которые не используеются, в том числе все из курсе django girl

class Table(models.Model):
    n = models.IntegerField()
    m = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)

    @property
    def n_as_array(self):
        return [x for x in range(self.n)]

    @property
    def m_as_array(self):
        return [x for x in range(self.m)]

    @property
    def fun_n_m(self):
        qs =  Table_cells.objects.filter(table = self)
        cells = {}
        for cell in qs:
            cell_n = cell.n
            cell_m = cell.m
            # print(cell_n, cell_m)
            # print(cell.cell)
            if cell_n not in cells:
                cells[cell_n] = {}
            if cell_m not in cells[cell_n]:
                cells[cell_n][cell_m] = cell
        d = []
        for i in range(self.n):
            for j in range(self.m):
                if i in cells and j in cells[i]:
                    dic = { 'n' : i, 'm': j, 'cell': cells[i][j].cell}
                else:
                    dic = {'n': i, 'm': j, 'cell': ''}
                d.append(dic)
        return d


class Table_cells(models.Model):
    cell = models.CharField(max_length=1)
    n = models.IntegerField()
    m = models.IntegerField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    @classmethod
    def create_cell(n, m, cell_changed, self):
        cell = self.create(n, m, cell = cell_changed)
        return cell


