from rest_framework import serializers
from organization.api.serializers import OrganizationSerializer
from faq.models import Faq



        
class FaqSerializer(serializers.ModelSerializer):
    
    organization = OrganizationSerializer
    class Meta:
        model = Faq
        fields = ['question','answer','organization']