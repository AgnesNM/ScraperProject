from django_seed import Seed

seeder = Seed.seeder()

from ScraperApp.models import Scrapers
seeder.add_entity(Scrapers, 12)

inserted_pks = seeder.execute()