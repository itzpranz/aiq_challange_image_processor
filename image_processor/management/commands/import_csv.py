# In yourapp/management/commands/import_csv.py

import csv
from django.core.management.base import BaseCommand
from image_processor.models import ImageModel

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']
        
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row if present
            
            for row in reader:
                depth = float(row[0])  
                pixel_values = [int(value) for value in row[1:]]  

                try:
                    image = ImageModel.objects.get(depth=depth)
                except ImageModel.DoesNotExist:
                    image = ImageModel(depth=depth, pixel_values=pixel_values)
                else:
                    image.pixel_values = pixel_values
                
                image.save()
                
                if image.pk:
                    self.stdout.write(self.style.SUCCESS(f'Imported/Updated image with depth {depth}'))
                else:
                    self.stdout.write(self.style.ERROR(f'Failed to import/update image with depth {depth}'))
