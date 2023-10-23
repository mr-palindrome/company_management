import uuid
from django.core.management.base import BaseCommand
from management.models import Company


class Command(BaseCommand):
    help = 'Add dummy companies to the database'

    def handle(self, *args, **options):
        dummy_data = [
            {
                'company_name': 'Company 1',
                'company_ceo': 'CEO 1',
                'company_address': 'Address 1',
                'inception_Date': '2023-01-01',
            },
            {
                'company_name': 'Company 2',
                'company_ceo': 'CEO 2',
                'company_address': 'Address 2',
                'inception_Date': '2023-02-15',
            },
        ]

        for data in dummy_data:
            company = Company(
                id=uuid.uuid4(),
                company_name=data['company_name'],
                company_ceo=data['company_ceo'],
                company_address=data['company_address'],
                inception_Date=data['inception_Date'],
            )
            company.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully added company: {company.company_name}'))
