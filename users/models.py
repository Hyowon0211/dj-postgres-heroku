from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Job(models.Model):
    job_name = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return f'{self.pk} {self.job_name}'


class UserManager(BaseUserManager):
    def create_user(self, phone_nm, login_ID, login_PW, age, gender, password):
        if not phone_nm:
            raise ValueError('User must have a phone_nm')
        if not login_ID:
            raise ValueError('User must have an login_ID')
        if not login_PW:
            raise ValueError('User must have a login_PW')
        if not age:
            raise ValueError('User must have an age')
        if not password:
            raise ValueError('User must have a password')
        # phone_nm = self.phone_nm(phone_nm)
        user = self.model(phone_nm=phone_nm, login_ID=login_ID, login_PW=login_PW, age=age, gender=gender,
                          password=password)
        user.set_password(password)
        user.is_superuser = False
        user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_nm, login_ID, login_PW, age, gender, password):
        if not phone_nm:
            raise ValueError('User must have a phone_nm')
        if not login_ID:
            raise ValueError('User must have an login_ID')
        if not login_PW:
            raise ValueError('User must have a login_PW')
        if not age:
            raise ValueError('User must have an age')
        if not password:
            raise ValueError('User must have a password')
        user = self.create_user(phone_nm, login_ID, login_PW, age, gender, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, phone_nm):
        print(phone_nm)
        return self.get(phone_nm=phone_nm)


class User(AbstractBaseUser):
    GENDER_CHOICES = [
        (0, 'Female'),
        (1, 'Male'),
    ]
    phone_nm = models.CharField(max_length=11, unique=True)
    login_ID = models.CharField(max_length=15, unique=True)
    login_PW = models.CharField(max_length=20, blank=False)
    age = models.IntegerField(blank=False)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, blank=False)
    REQUIRED_FIELDS = ['login_ID', 'login_PW', 'age', 'gender']
    USERNAME_FIELD = 'phone_nm'

    objects = UserManager()

    def __str__(self):
        return f'{self.pk}-{self.phone_nm}'


class Profile(models.Model):
    related_user = models.OneToOneField(User, on_delete=models.CASCADE,
                                        related_name='related_user',
                                        primary_key=True)
    nickname = models.CharField(max_length=20, null=False)
    introduction = models.TextField(null=False, blank=True)
    jobs = models.ManyToManyField('Job', null=True, blank=True, default=None,
                                  related_name='jobs_set')  # profile_job ????????? ?????? ??????
    click_recomms = models.ManyToManyField('self', symmetrical=False,
                                           related_name='get_recomms', blank=True)

    # ??????(hyo)??? ????????? ?????????.  hyo.click_recomms.all()
    # ??????(song)??? ????????? ?????????. song.get_recomm.all()
    # hyo.click_recomms.add(gildong)   hyo??? gildong??? ??????
    # hyo.get_recomms.add(gildong)  gildong ??? hyo??? ??????(hyo??? ????????? ??????list??? gildong ??????)

    def recomms_cnt(self):
        return self.get_recomms.all().count()

    def already_clicked(self,
                        to_prof):  # self??? to_prof(id????)??? ?????? ?????? ????????? True . ???????????? False (view?????? pro.already_clicked == True??? raise????????????. False??? recomm?????????(add)
        if to_prof in self.click_recomms.all().values_list('pk', flat=True):
            return True
        else:
            return False

    # def increase_cnt(self):
    #     self.recomms_cnt = self.recomms_cnt + 1     # ???????????????,,,? ?????? ????????? ?????? add?????? ?????? ???????????? ?????? ???????????? ?????????????????????..

    def __str__(self):
        return f'{self.pk}-{self.nickname}'

    # -{self.user.phone_nm}  ????????? phone_nm??? ?????? ?????? .

    def get_jobs(self):
        return self.jobs.all().values('id', 'job_name')  # pk????????? return???????????????..
        # return Job.objects.get(id=self.jobs.all())
    # def _get_pk_val(self, meta=None):
    #     return self.jobs.all().values('pk')

    # User ?????? ?????? : login_ID, login_PW, age, gender, phone_nm,
    # Profile ?????? ?????? : nickname, introduction   , jobs, click_recomms
    # jobs??? click_recomms??? __init__?????? ??????????????????
    # def __init__(self):
    #     basic = Job.objects.get(pk=22)
    #     self.jobs.add(basic)
    #     #recomm_self = self
    #     self.click_recomms.add(self)
    #     super.__init__()
