from enum import Enum
from string import Template


class Messages(Enum):
    ApplicationComplete = 'Заявка оставлена успешно. ' \
                          'В ближайшее время мы свяжемся с ' \
                          'вами для подтверждения.'
    ApplicationError = 'Скорее всего вы ошиблись при вводе номера. ' \
                       'Обращаем ваше внимание, ' \
                       'что формат вводимого номера - 10 цифр, начиная с 9.'
    NewApplication = Template(
        'Поступила новая заявка от:\n '
        'Имя: $client_name\n '
        'Номер телефона: $client_phone'
    )
