# Python
import datetime

# Django
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

# Project
from apps.main.univer_groups.models import UniverGroup
from apps.user.manager import UserManager


def upload_avatar_to(instance, filename):
    """
    file will be uploaded to MEDIA_ROOT/user_images/student_id/<filename>
    """
    return 'files/user_images/{0}/{1}'.format(instance.student_id, filename)


def upload_background_to(instance, filename):
    """
    file will be uploaded to MEDIA_ROOT/user_images/student_id/<filename>
    """
    return 'files/user_images/{0}/background___{1}'.format(instance.student_id, filename)


class User(AbstractBaseUser, PermissionsMixin):
    """
        This model represents user accounts within your application. It builds upon Django's
        built-in AbstractUser class, providing a foundation for authentication, permissions,
        and user-related functionality. You can extend this model to include custom fields
        and methods specific to your application's requirements.

        Attributes:
            id (int): Unique identifier for the user.
            student_id (int): Unique identifier for the student.
            full_name (str): Full name of the user (uppercase).
            phone_number (int): Phone number associated with the user.
            passport_number (int): Passport number.
            passport_issue_date (datetime): Date when the passport was issued.
            dob (datetime, optional): Birth date of the user (nullable).
            gender (str): Gender of the user (enum).
            nation (str, optional): Nationality of the user (nullable).
            profile_image (str): URL of the user's profile image.
            about_me (str, optional): Brief user description (nullable).
            fails (int): Number of fails (calculated from Fails table).
            univer_group (int): ID of the group the user belongs to.
            email_address (email): Email address associated with the user.

        Note:
            It's important to tailor the fields and methods of this model to match your
            application's needs while adhering to security best practices.
    """
    class GenderTypes(models.TextChoices):
        MALE = "MALE", _("MALE")
        FEMALE = "FEMALE", _("FEMALE")

    student_id = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128)
    full_name = models.CharField(max_length=255)
    phone_number = models.IntegerField(blank=True, null=True)
    passport_number = models.CharField(max_length=9, unique=True, null=True)
    passport_issue_date = models.DateField(null=True)
    passport_expiry_date = models.DateField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GenderTypes.choices, default=GenderTypes.MALE)
    nation = models.CharField(max_length=100, blank=True, default='UZBEK')
    profile_image = models.ImageField(upload_to=upload_avatar_to, blank=True, null=True)
    background_image = models.ImageField(upload_to=upload_background_to, blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    fails = models.IntegerField(blank=True, null=True)
    univer_group = models.ForeignKey(UniverGroup, on_delete=models.SET_NULL, null=True)
    email_address = models.EmailField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_dean = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    last_login = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'student_id'

    @property
    def calculate_passport_expiry_date(self):
        """
        This method used to figure out passport_expiry_date using the formula "passport_issue_date + (365 * 10)"
        :return: datetime
        """
        issue_date = self.passport_issue_date
        current_date = issue_date + datetime.timedelta(days=365 * 10)
        self.passport_expiry_date = current_date.strftime('%Y-%m-%d')
        return self.passport_expiry_date

    @property
    def upper_case_full_name(self):
        """
        This is used to generate all letters of the student's full_name in uppercase
        :return: str
        """
        return self.full_name.upper()

    # @property
    # def calculate_fails_of_student(self):
    #     from apps.main.fails.models import Fail
    #     fails = self.fails

    def is_member(self, *groups):
        """
        This method used to check a group of users.
        If a result is True, then User member of this group is otherwise not member
        :return: boolean
        """
        return self.groups.filter(student_id__in=groups).exists()

    def is_in_multiple_groups(self, *groups):
        """
        This method used to check a group of users.
        If a result is True, then User member of this group is otherwise not member
        :return: boolean
        """
        return self.groups.filter(student_id__in=[*groups]).exists()

    def __str__(self):
        return self.student_id

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id', ]
