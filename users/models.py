from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Job(models.Model):
    job_name = models.CharField(max_length=30, blank=False)
    def __str__(self):
        return self.job_name


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
        user = self.model(phone_nm=phone_nm, login_ID=login_ID, login_PW=login_PW, age=age, gender=gender, password=password)
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


class User(AbstractUser):
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
    jobs = models.ManyToManyField('Job', null=True, blank=True, default=None)   # profile_job 테이블 자동 생성
    click_recomms = models.ManyToManyField('self', symmetrical=False, related_name='get_recomms', blank=True,null=True)
    # 본인(hyo)이 추천한 회원들.  hyo.click_recomms.all()
    # 회원(song)을 추천한 회원들. song.get_recomm.all()
    # hyo.click_recomms.add(gildong)   hyo가 gildong을 추천
    # hyo.get_recomms.add(gildong)  gildong 이 hyo를 추천(hyo를 추천한 회원list에 gildong 추가)

    # def save(self,  *args, **kwargs):
    #
    #     super(Profile, self).save(*args, **kwargs)  # Call teh 'real save() method
    def __str__(self):
        return f'{self.pk}-{self.nickname}'
    #-{self.user.phone_nm}  이렇게 phone_nm도 참조 가능 .

    def get_jobs(self):
        return self.jobs.values('id','job_name')  # pk값들만 return해야하는데..
        #return Job.objects.get(id=self.jobs.all())



