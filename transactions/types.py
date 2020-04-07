from enum import Enum


class TransactionStatus(Enum):
    PROCESSING = 'processing'
    COMPLETED = 'completed'
    ERROR = 'error'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class TransactionLocation(Enum):
    ORIGINATION_BANK = 'origination_bank'
    ROUTABLE = 'routable'
    DESTINATION_BANK = 'destination_bank'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
