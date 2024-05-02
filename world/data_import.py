from world.models import Standing, Team, Player, Match, Statistic
import pandas as pd
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Import data from Excel file'

    def handle(self, *args, **kwargs):
        excel_path = '../数据话英超.xls'
        try:
            excel_data1 = pd.read_excel(excel_path)
            for index, row in excel_data1.iterrows():
                Standing.objects.create(
                    teamid=row['teamid'],
                    name=row['name'],
                    sum=row['sum'],
                    goals=row['goals'],
                    miss=row['miss'],
                    clear=row['clear'],
                    points=row['points']
                )
            self.stdout.write(self.style.SUCCESS('Data imported successfully'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Failed to import data: {e}'))
