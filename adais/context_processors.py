from .models import Restaurant

DAYS_OF_WEEK = (
    (7, 'All Week'),
    (0, 'Sunday'),
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
)

def getrest(self):

  p = Restaurant.objects.values_list('restaurantId', 'name').order_by('name')
  p = list(p)
  return { 'restList' : p, 'weekList' : DAYS_OF_WEEK }
