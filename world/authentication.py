from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.models import Q


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # 尝试通过邮箱地址查找用户
            user = UserModel.objects.get(Q(email__iexact=username) | Q(username__iexact=username))
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            # 用户不存在时返回None
            raise ValidationError("无效的登录凭证")
        return None

