# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.deans.models import Dean


class DeanSerializer(serializers.ModelSerializer):
    """
    Serializer for the Deans of University.

    The DeanSerializer is responsible for converting instances of the Dean model
    to and from JSON format. It allows data to be serialized for responses and deserialized
    for request data, enabling easy integration with Django REST framework views.
    """

    class Meta:
        model = Dean
        fields = [
            'id',
            'full_name',
            'dob',
            'image',
        ]

    def create(self, validated_data):
        """
        Create a new Dean instance.

        This method is used to create a new Dean instance with the given validated data.

        Returns:
            Dean: The newly created instance of the Dean model.

        Raises:
            serializers.ValidationError: If a Dean with the same full name and date of birth
                                         already exists in the database.
        """
        full_name = validated_data.get('full_name')
        dob = validated_data.get('dob')
        image = validated_data.get('image', None)

        # Check if another Dean with the same full name and date of birth already exists
        if Dean.objects.filter(full_name=full_name, dob=dob).exists():
            raise serializers.ValidationError("Error. Dean with the same full name and date of birth already exists.")

        dean = Dean.objects.create(full_name=full_name, dob=dob, image=image)
        return self.to_representation(dean)

    def update(self, instance, validated_data):
        """
        Update an existing Dean instance.

        This method is used to update an existing Dean instance with the given validated data.

        Returns:
            Dean: The updated instance of the Dean model.

        Raises:
            serializers.ValidationError: If a Dean with the same full name and date of birth
                                         already exists in the database during update.
        """
        full_name = validated_data.get('full_name', instance.full_name)
        dob = validated_data.get('dob', instance.dob)
        image = validated_data.get('image', instance.image)

        # Check if another Dean with the same full name and date of birth already exists
        if Dean.objects.filter(full_name=full_name, dob=dob).exclude(id=instance.id).exists():
            raise serializers.ValidationError("Error. Dean with the same full name and date of birth already exists.")

        instance.full_name = full_name
        instance.dob = dob
        instance.image = image
        instance.save()

        return self.to_representation(instance)
