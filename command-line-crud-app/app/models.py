from django.db import models


class Item(models.Model):
    item_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    in_stock = models.BigIntegerField()

    def __str__(self):
        return f"{self.name} Item_ID:{self.item_id}"


def create_item(item_id, name, price, in_stock):
    return Item.objects.create(
        item_id=item_id, name=name, price=price, in_stock=in_stock
    )


def view_all_items():
    return Item.objects.all()


def search_item_by_name(name):
    return Item.objects.filter(name=name)


def get_item(item_id):
    return Item.objects.get(item_id=item_id)


def update_item(add, quantity, item_id):
    item = Item.objects.get(item_id=item_id)
    item.in_stock += quantity if add else -(quantity)
    item.save()


def delete_item(item_id):
    Item.objects.get(item_id=item_id).delete()
