from django.db import models
from django.db.models.signals import post_save 
from django.dispatch import receiver 


class Contact(models.Model):

    # Define the available option for the 'status' field. 
    # Each option is a tuple containing the database value and the human-readable label. 
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')
    resolution = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


@receiver(post_save, sender=Contact)
def contact_saved(sender, instance, created, **kwargs):
    """
    Handle the post-save signal emitted by the Contact model.

    This function is called when a Contact object is saved. It performs additional
    actions if the Contact object is newly created.

    The role of the signal ('post_save') is to notify any registered receivers that a model instance
    has been saved. It provides a way for different parts of the application to respond to the event
    of saving a model instance. 

    The role of the receiver function ('contact_saved') is to define the actions to be performed 
    when the signal is triggered. In this example, the receiver function checks if the 'Contact'
    instance was newly created('created' is 'True') and then performs additional actions
    (printing a message to the console). It's possible modify the receiver function to suit
    specific requirements, such as sending emails, updating related models, or performing any 
    other desired actions. 

    Args:
        sender (Type[Contact]): The sender of the signal, which is the Contact model.
        instance (Contact): The instance of the Contact model that was saved.
        created (bool): A boolean value indicating if the instance was newly created.
        **kwargs: Additional keyword arguments passed along with the signal.

    Returns:
        None

    Raises:
        None
    """
    if created: 
        # :TODO: perfom any additional actions here 
        print(f'A new contact has been saved: {instance.first_name} {instance.last_name}')