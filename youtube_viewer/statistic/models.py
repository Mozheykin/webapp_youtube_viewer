from django.db import models

class Video(models.Model):
    video_id = models.AutoField(primary_key=True, verbose_name='id')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания задания')
    url = models.CharField(max_length=255, null=True, blank=True, verbose_name='Ссылка на видео')
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название видео')
    min_view = models.IntegerField(verbose_name='Время минимального просмотра в с.')
    max_view = models.IntegerField(verbose_name='Время максимального просмотра в с.')
    thread_view = models.IntegerField(verbose_name='Количество потоков для просмотра')
    count_view = models.IntegerField(verbose_name='Количество раз просмотрено')
    avalible = models.BooleanField(verbose_name='Просматривать')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Видео'
        verbose_name = 'Видео'
        # ordering = ['-created']