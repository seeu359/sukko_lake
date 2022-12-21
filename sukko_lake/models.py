from django.db import models


class MainPicture(models.Model):
    name = models.CharField(
        max_length=50,
        help_text='Название фото.'
                  'Обязательное поле. '
                  'Будет выделено жирным шрифтом на фото в карусели.',
    )
    photo = models.URLField()
    description = models.CharField(
        max_length=300,
        help_text='Описание фото.'
                  'Обязательное поле.'
                  'Будет располагаться под названием в карусели')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Слайды из карусели'


class FakeUsers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = models.URLField(
        help_text='Фото, чтобы адекватно отображаться в отзыве,'
                  ' должно быть размером 250x250. '
                  'Сервис для изменения размеров фото: '
                  'https://www.iloveimg.com/ru или любой подобный сервис. '
                  'В идеале, чтобы начальный размер изображения был с '
                  'соотношением стороон 1 к 1, к примеру, с таким размером:'
                  ' 950x950. В таком случае, при уменьшении размеров фото '
                  'не нарушатся пропорции.',
    )
    description = models.CharField(
        max_length=200,
        blank=True,
        help_text='Необязательное поле. '
                  'Можешь делать себе какие-то пометки, '
                  'либо оставить пустым',
    )

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = 'Фейковые пользователи'


class FakeFeedback(models.Model):
    title = models.CharField(
        max_length=50,
        help_text='Заголовок - будет выделен жирным шрифтом в отзыве',
    )
    feedback_body = models.TextField(
        null=False,
        blank=False,
        help_text='Тело отзыва - основная часть отзыва',
    )
    user = models.ForeignKey(
        FakeUsers,
        on_delete=models.CASCADE
    )
    description = models.CharField(
        max_length=200,
        blank=True,
        help_text='Необязательное поле. '
                  'Можешь делать себе какие-то пометки, '
                  'либо оставить пустым',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Фейковые отзывы'


class Application(models.Model):
    WORK = 'W'
    WORK_OUT = 'WO'
    STATUS_CHOICES = [
        (WORK, 'В работе'),
        (WORK_OUT, 'Отработана'),
    ]
    client_name = models.CharField(
        max_length=50,
    )
    client_number = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=WORK,
    )

    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name_plural = 'Заявки от клиентов'
