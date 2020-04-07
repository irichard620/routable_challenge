import uuid

from django.db import models

from transactions.types import TransactionStatus, TransactionLocation


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount_cents = models.IntegerField(default=0)

    @classmethod
    def create(cls, amount_cents):
        item = cls(amount_cents=amount_cents)
        return item


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    status = models.CharField(choices=TransactionStatus.choices(), max_length=16, default=TransactionStatus.PROCESSING)
    location = models.CharField(
        choices=TransactionLocation.choices(),
        max_length=24,
        default=TransactionLocation.ORIGINATION_BANK
    )
