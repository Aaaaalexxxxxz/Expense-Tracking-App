from .models import Record
from celery import shared_task
from datetime import datetime, timedelta

@shared_task
def process_recurring_records():
    today = date.today()
    recurring_record = Records.objects.filter(recurrance =['Weekly', 'Biweekly', 'Monthly'] )

    for record in recurring_record:
        new_record = Record.objects.create(
            userid=record.userid,
            created_at=record.next_occurance,
            catagory=record.catagory,
            recurrance=record.recurrance,
            description=record.description,
            income=record.income,
            amount=record.amount,
            next_occurance=record.calculate_next_occurance()
        )

        #update original record with next occurance
        record.next_occurance = record.calculate_next_occurance()
        record.save()