from django.db import models


class Vacancy(models.Model):
    profession = models.CharField(max_length=100, verbose_name='Профессия')
    date = models.DateField(verbose_name='Дата')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.profession

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class Subscriber(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    content = models.TextField(verbose_name='Контент')
    date = models.DateField(verbose_name='Дата')
    photo = models.ImageField(upload_to='subscribers/', verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Для абонентов'
        verbose_name_plural = 'Для абонентов'


class Tender(models.Model):
    number = models.CharField(max_length=20, verbose_name='Номер')
    title = models.CharField(max_length=100, verbose_name='Название')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания')
    delivery_address = models.CharField(max_length=200, verbose_name='Адрес доставки')
    contest_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма конкурса')
    status = models.CharField(max_length=50, verbose_name='Статус')
    bid_results = models.TextField(verbose_name='Результаты вскрытия и оценки заявок')
    lots = models.TextField(verbose_name='Лоты')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тендер'
        verbose_name_plural = 'Тендеры'


class News(models.Model):
    description = models.TextField(verbose_name='Описание')
    video = models.URLField(verbose_name='Видео')
    date = models.DateField(verbose_name='Дата')
    content = models.TextField(verbose_name='Контент')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class User(models.Model):
    # Добавьте поля для пользователя в соответствии с вашими требованиями
    pass


class Lot(models.Model):
    number = models.CharField(max_length=20, verbose_name='Номер')
    title = models.CharField(max_length=100, verbose_name='Название')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    document = models.FileField(upload_to='lots/', verbose_name='Документ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Лот'
        verbose_name_plural = 'Лоты'


class Statistics(models.Model):
    calls_today = models.PositiveIntegerField(verbose_name='Звонки сегодня')
    calls_total = models.PositiveIntegerField(verbose_name='Звонки за все время')
    subscribers_count = models.PositiveIntegerField(verbose_name='Количество абонентов')
    water_pipe_kilometers = models.DecimalField(max_digits=10, decimal_places=2,
                                                verbose_name='Километры водопроводных сетей')
    sewer_pipe_kilometers = models.DecimalField(max_digits=10, decimal_places=2,
                                                verbose_name='Километры канализационных сетей')
    water_intakes = models.PositiveIntegerField(verbose_name='Водозаборные сооружения')

    def __str__(self):
        return f'Статистика #{self.id}'

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'


class Application(models.Model):
    # Добавьте поля для заявки в соответствии с вашими требованиями
    pass


class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    content = models.TextField(verbose_name='Контент')
    date = models.DateField(verbose_name='Дата')
    photo = models.ImageField(upload_to='services/', verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Contact(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Leader(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    position = models.CharField(max_length=100, verbose_name='Должность')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='leaders/', verbose_name='Фото')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Руководитель'
        verbose_name_plural = 'Руководители'
