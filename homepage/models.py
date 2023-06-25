from django.db import models

class ProfileManager(models.Manager):
    """Custom manager for the Profile model.

    This manager provides methods for retrieving and managing the profile object.

    Attributes:
        None

    Methods:
        get_profile(): Retrieve the profile object.
    """
    def get_profile(self):
        """Retrieve the profile object.

        This method retrieves the profile object. If it exists, the existing profile
        object is returned. If it doesn't exist, a new profile object is created.

        Args:
            None

        Returns:
            Profile: The profile object.

        Raises:
            None
        """
        profile, created = self.get_or_create(pk=1)
        return profile 
    
    def create(self, **kwargs):
        """Prevent creation of additional objects.

        This method is overridden to prevent the creation of additional objects.
        Any attempts to create a new profile object will be blocked.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            None

        Raises:
            None
        """ 
        pass

    def get_or_create(self, **kwargs):
        """Ensure only one object is returned.

        This method is overridden to ensure that only one profile object is returned,
        regardless of any other arguments provided. It sets the primary key (pk)
        argument to 1 to fetch the specific profile object.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            Tuple[Profile, bool]: A tuple containing the profile object and a boolean
            indicating whether it was created.

        Raises:
            None
        """
        kwargs['pk'] = 1
        return super().get_or_create(**kwargs)
        
class Profile(models.Model):
    image = models.ImageField(upload_to='images/profile')
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)

    objects = ProfileManager()

class URLs(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    image = models.ImageField(upload_to='icons')

    
    
    def __str__(self):
        return self.name
