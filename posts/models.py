from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название тега")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Категория"
    )
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Теги")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-pub_date']


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name="Пост"
    )
    author = models.CharField(max_length=100, verbose_name="Автор", default="Аноним")
    content = models.TextField(verbose_name="Комментарий")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    approved = models.BooleanField(default=False, verbose_name="Одобрен")

    def __str__(self):
        return f'Комментарий от {self.author} к посту "{self.post.title}"'

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['-created_date']

