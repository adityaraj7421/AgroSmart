"""
Management command to populate initial data for the AgroSmart system.
This includes districts, crops, soils, and years.
"""
from django.core.management.base import BaseCommand
from app.models import District, Crop, Soil, Year


class Command(BaseCommand):
    help = 'Populates initial data (districts, crops, soils, years) for the AgroSmart system'

    def handle(self, *args, **options):
        # Populate Districts
        districts = [
            'Kathmandu', 'Lalitpur', 'Bhaktapur', 'Pokhara', 'Chitwan',
            'Biratnagar', 'Dharan', 'Butwal', 'Hetauda', 'Janakpur',
            'Bharatpur', 'Itahari', 'Nepalgunj', 'Dhading', 'Kavrepalanchok',
            'Nuwakot', 'Sindhupalchok', 'Makwanpur', 'Ramechhap', 'Dolakha'
        ]
        
        created_districts = 0
        for district_name in districts:
            district, created = District.objects.get_or_create(name=district_name)
            if created:
                created_districts += 1
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully populated {created_districts} new districts. '
                f'Total districts: {District.objects.count()}'
            )
        )
        
        # Populate Crops
        crops = [
            'Rice', 'Wheat', 'Maize', 'Potato', 'Tomato',
            'Onion', 'Garlic', 'Cabbage', 'Cauliflower', 'Carrot',
            'Radish', 'Cucumber', 'Pumpkin', 'Beans', 'Peas',
            'Lentil', 'Soybean', 'Mustard', 'Sunflower', 'Barley'
        ]
        
        created_crops = 0
        for crop_name in crops:
            crop, created = Crop.objects.get_or_create(name=crop_name)
            if created:
                created_crops += 1
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully populated {created_crops} new crops. '
                f'Total crops: {Crop.objects.count()}'
            )
        )
        
        # Populate Soils
        soils = [
            'Sandy Soil', 'Clay Soil', 'Loamy Soil', 'Silty Soil',
            'Peaty Soil', 'Chalky Soil', 'Red Soil', 'Black Soil'
        ]
        
        created_soils = 0
        for soil_name in soils:
            soil, created = Soil.objects.get_or_create(name=soil_name)
            if created:
                created_soils += 1
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully populated {created_soils} new soils. '
                f'Total soils: {Soil.objects.count()}'
            )
        )
        
        # Populate Years (for rainfall data)
        from datetime import datetime
        current_year = datetime.now().year
        years_list = list(range(current_year - 5, current_year + 1))
        
        created_years = 0
        for year_value in years_list:
            year, created = Year.objects.get_or_create(name=year_value)
            if created:
                created_years += 1
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully populated {created_years} new years. '
                f'Total years: {Year.objects.count()}'
            )
        )
        
        self.stdout.write(
            self.style.SUCCESS('\nInitial data population completed successfully!')
        )

