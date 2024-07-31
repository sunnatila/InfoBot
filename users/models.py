from django.db import models
from django.utils.translation import gettext_lazy as _


class TgUser(models.Model):
    language = models.CharField(max_length=3, verbose_name=_("Foydalanuvchining tili"))
    tg_id = models.IntegerField(verbose_name=_("Foydalanuvchining tg id"))

    objects = models.Manager()

    def __str__(self):
        return f'{str(self.id)} - foydalanuvchi'

    class Meta:
        verbose_name_plural = _("Telegram foydalanuvchilar")
        verbose_name = _("Telegram foydalanuvchi ")
        db_table = 'tg_users'

