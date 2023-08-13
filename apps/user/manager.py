# Django
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db.models.manager import BaseManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager, BaseManager):
    """
    This class helps to Developer and User model to creating User using methods.

    Note:
        You can read about the difference between "is_staff" and "is_superuser" by the link below.
        :link: https://stackoverflow.com/a/72054094/15219474
    """

    def __create_user(self, student_id, password, is_staff=False, is_superuser=False):
        """
        Creates and saves a User with the given student_id and password.
        :return: obj
        """
        user = self.model(student_id=student_id.replace(' ', ''), is_staff=is_staff, is_superuser=is_superuser)
        user.set_password(password.replace(' ', ''))
        user.save(using=self._db)
        return user

    def create_student(self, student_id, password):
        """
        Creates and saves a User with the given student_id and password.
        :return: obj
        """
        return self.__create_user(student_id, password)

    def create_admin(self, student_id, password):
        """
        Creates and saves an Admin with the given student_id and password.
        :return: obj
        """
        return self.__create_user(student_id, password, is_staff=True)

    def create_superuser(self, student_id, password):
        """
        Creates and saves a SuperUser with the given student_id and password.
        :return: obj
        """
        return self.__create_user(student_id, password, is_staff=True, is_superuser=True)
