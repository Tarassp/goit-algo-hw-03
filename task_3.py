import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    phone_number = re.sub(r"[^\d+]", "", phone_number)
    if not phone_number.startswith("+"):
        phone_number = re.sub(r"^(38)?", "+38", phone_number)
    return phone_number

class PhoneNormalizer:
    def __call__(self, phones):
        return [self._normalize(phone) for phone in phones]

    def _normalize(self, phone):
        phone = re.sub(r"[^\d+]", "", phone)
        if not phone.startswith("+"):
            phone = re.sub(r"^(38)?", "+38", phone)
        return phone

normalizer = PhoneNormalizer()
print(normalizer(raw_numbers))