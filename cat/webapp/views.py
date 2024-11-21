import random
from django.shortcuts import render
from django.http import HttpResponseRedirect


class Cat:
    def __init__(self, name="Кот", age=1):
        self.name = name
        self.age = age
        self.hunger = 40
        self.happiness = 40
        self.is_sleeping = False

        self.avatar_normal = 'img/normal_cat.jpg'
        self.avatar_happy = 'img/funny_cat.jpg'
        self.avatar_sad = 'img/sad_cat.jpg'

    def feed(self):
        if self.is_sleeping:
            return False
        self.hunger += 15
        self.happiness += 5
        if self.hunger > 100:
            self.hunger = 100
            self.happiness -= 30
        if self.happiness > 100:
            self.happiness = 100
        return True

    def play(self):
        if self.is_sleeping:
            self.is_sleeping = False
            self.happiness -= 5
        else:
            self.happiness += 15
            self.hunger -= 10
            if random.randint(1, 3) == 1:
                self.happiness = 0
        if self.happiness > 100:
            self.happiness = 100
        if self.hunger < 0:
            self.hunger = 0
        return True

    def sleep(self):
        self.is_sleeping = True

    def get_avatar(self):
        if self.happiness >= 70:
            return self.avatar_happy
        elif self.happiness <= 30:
            return self.avatar_sad
        else:
            return self.avatar_normal

cat = Cat()

def index_view(request):
    if request.method == 'POST':
        cat.name = request.POST.get('name', cat.name)
        return HttpResponseRedirect('/cat_stats')
    return render(request, 'index.html')

def cat_stats_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'feed':
            cat.feed()
        elif action == 'play':
            cat.play()
        elif action == 'sleep':
            cat.sleep()
    return render(request, 'cat_stats.html', {'cat': cat})
