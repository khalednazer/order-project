from .models import profile
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import Customer

@receiver(post_save, sender = User)
def creaet(sender, instance, created, **kwargs ):
    if created:
        profile.objects.create(user = instance)
        print('user created')
        groupss =Group.objects.get(name='customer')
        instance.groups.add(groupss)
        Customer.objects.create(user = instance, name= instance.username)
        print('user created seccesfly')

# @receiver(post_save, sender = User)
# def update(sender, instance, created, **kwargs):
#     if  created == False :
#         print('profile updated')
#         instance.profile.save()
#         print('user updated form second def ')

# post_save.connect(update, sender=User)

