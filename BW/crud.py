import BW.models as models
from BW.models import Reviews, Orders
import datetime

#                                             
def add_review(author, review_description, date):
    new_review = models.Reviews(
        author = author,
        review_description = review_description,
        date=datetime.datetime.now()

    )
    new_review.save()

    return new_review

def get_all_reviews_from_current_bike(bike):
    return models.Reviews.objects.filter(product_review=bike)




def create_Order(User, date):
    new_order = models.Orders(
        User=User,
        date=datetime.datetime.now()
    )

    new_order.save()

    return new_order

def add_item_to_order(order, product, count):
    order_item = models.Orders(
        product=product,
        order=order,
        count=count

    )
    
    order_item.save()
    return order_item













# def get_review():
#     return models.Reviews.objects.get(id=Reviews.id)




# import BW.models as models

# def something(based_off_of_lines_in_model):
#     new_something = models.Something(
#         based=based
#         off=off
#         lines=lines
#     )
#     new_something.save()

#     return new_something

# def get_all_smth():
#     return models.Somethinf.objects.all()

# def get_smth():
#     return models.Somethinf.objects.get(id=based) # get - получить запись

# def get_smth_filter():
#     return models.Somethinf.objects.filter(based=based) # filter - получить несколько записей по определенному филттру все

# def update_smth(id, update_data):
#     update_data=get_all_smth

#     update_data.save()
#     return update_data

# def delete():
#     smth.delete()