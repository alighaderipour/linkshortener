from rest_framework import serializers
from .models import Link

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'

# کاربر فقط name و url رو می‌فرسته
# slug و clicks فقط برای نمایش استفاده می‌شن، کاربر حق تغییرشون رو نداره

class LinkSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'name', 'url', 'slug', 'clicks']
        read_only_fields = ['id', 'slug', 'clicks']