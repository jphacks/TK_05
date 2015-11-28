from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now_add=True, auto_now=True)

    class Meta:
        abstract = True


class Icon(BaseModel):
    file = models.ImageField("アイコン", upload_to='./icons', null=True, default=None, blank=True)

class User(AbstractUser, BaseModel):
    points = models.IntegerField("得点", default=0, blank=True)
    last_scored = models.DateTimeField("最終得点日時",  default=None, blank=True)
    screen_name = models.CharField("表示名", unique=True, max_length=30)
    icon = models.ForeignKey(Icon, verbose_name="アイコン")

class Service(BaseModel):
    name = models.CharField("サービス名", max_length=30)

class AuthToken(BaseModel):
    user = models.ForeignKey(User, verbose_name="ユーザ")
    service = models.ForeignKey(Service, verbose_name="サービス")
    token = models.CharField("トークン", max_length=128)

class Stage(BaseModel):
    name = models.CharField("ステージ名", max_length=255, unique=True)
    description = models.TextField("説明", blank=True)
    required_points = models.IntegerField("キーポイント")


class Category(BaseModel):
    name = models.CharField("カテゴリ名", max_length=255, unique=True)
    description = models.TextField("説明", blank=True)


class Question(BaseModel):
    number = models.IntegerField("問題番号", unique=True)
    title = models.CharField("問題名", max_length=255)
    body = models.TextField("問題文")
    stage = models.ForeignKey(Stage, verbose_name="ステージ", default=None, null=True)
    category = models.ForeignKey(Category, verbose_name="カテゴリ")
    is_public = models.BooleanField("公開するか", default=False, blank=True)
    is_delete = models.BooleanField("削除", default=False, blank=True)


class Answer(BaseModel):
    user = models.ForeignKey(User, verbose_name="ユーザ")
    question = models.ForeignKey(Question, verbose_name="問題")
    answer = models.TextField("解答")
    is_correct = models.BooleanField("正解か否か", default=False, blank=True)


class Flag(BaseModel):
    question = models.ForeignKey(Question, verbose_name="問題")
    flag = models.TextField("フラグ")
    point = models.IntegerField("点数")


class File(BaseModel):
    name = models.CharField("ファイル名", max_length=255)
    file = models.FileField(upload_to='files/', max_length=255, verbose_name="ファイル")
    question = models.ForeignKey(Question, verbose_name="問題")
    is_public = models.BooleanField("公開するか", default=False, blank=True)
    is_delete = models.BooleanField("削除", default=False, blank=True)

    @property
    def url(self):
        return reverse("download_file", args=(self.id, self.name))


class Importance(BaseModel):
    priority = models.IntegerField("重要度")
    name = models.CharField("名前", max_length=255)


class Notice(BaseModel):
    user = models.ForeignKey(User, verbose_name="ユーザ")
    question = models.ForeignKey(Question, verbose_name="問題", null=True, default=None)
    importance = models.ForeignKey(Importance, verbose_name="重要度")
    title = models.CharField("タイトル", max_length=255)
    body = models.TextField("本文")

class WriteUp(BaseModel):
    title = models.CharField("タイトル", max_length=128)
    body = models.TextField("本文")
    question = models.ForeignKey(Question, verbose_name="問題")
    user = models.ForeignKey(User, verbose_name="ユーザ")
    is_public = models.BooleanField("公開するか", blank=True, default=False)
    is_delete = models.BooleanField("削除", blank=True, default=False)

class Comment(BaseModel):
    body = models.CharField("本文", max_length=65535)
    user = models.ForeignKey(User, verbose_name="ユーザ")
    writeup= models.ForeignKey(WriteUp, verbose_name="WriteUp")
    is_public = models.BooleanField("公開するか", blank=True, default=False)
    is_delete = models.BooleanField("削除", blank=True, default=False)
