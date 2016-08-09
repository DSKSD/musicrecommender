# coding: utf-8
from django.core.management.base import BaseCommand, CommandError
from main.models import Post, Vote
from django.db.models import Avg

def round_of_rating(number):
    """Round a number to the closest half integer.
    >>> round_of_rating(1.3)
    1.5
    >>> round_of_rating(2.6)
    2.5
    >>> round_of_rating(3.0)
    3.0
    >>> round_of_rating(4.1)
    4.0"""

    return round(number * 2) / 2

# 각 포스팅의 평균 Rating을 계산하는 commands
class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        stars = Vote.objects.values('post').annotate(meanstar=Avg('score'))
        
        print 'Computing mean of stars!!'
        
        for star in stars:
            post_id = star['post']
            meanstar = star['meanstar']
            post = Post.objects.get(pk=post_id)
            post.meanstar = round(meanstar, 2)
            post.save()
        
        print 'Done!'    
