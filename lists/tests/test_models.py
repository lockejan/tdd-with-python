from django.test import TestCase
from django.core.exceptions import ValidationError
from lists.models import Item, List
from django.contrib.auth import get_user_model

User = get_user_model()


class ItemModelTest(TestCase):
    def test_default_text(self):
        item = Item()
        self.assertEqual(item.text, '')

    def test_item_is_related_to_list(self):
        new_list = List.objects.create()
        item = Item()
        item.list = new_list
        item.save()
        self.assertIn(item, new_list.item_set.all())

    def test_cannot_save_empty_list(self):
        new_list = List.objects.create()
        item = Item(list=new_list, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()


class ListModelTest(TestCase):
    def test_get_absolute_url(self):
        new_list = List.objects.create()
        self.assertEqual(new_list.get_absolute_url(), f'/lists/{new_list.id}/')

    def test_duplicate_items_are_invalid(self):
        new_list = List.objects.create()
        Item.objects.create(list=new_list, text='Coffee Beans')
        with self.assertRaises(ValidationError):
            item = Item(list=new_list, text='Coffee Beans')
            item.full_clean()
            # item.save()

    def test_CAN_save_same_item_to_different_lists(self):
        list_1 = List.objects.create()
        list_2 = List.objects.create()
        Item.objects.create(list=list_1, text='Coffee Beans')
        item = Item(list=list_2, text='Coffee Beans')
        item.full_clean()  #should not raise

    def test_list_ordering(self):
        list_1 = List.objects.create()
        item_1 = Item.objects.create(list=list_1, text='i1')
        item_2 = Item.objects.create(list=list_1, text='item 2')
        item_3 = Item.objects.create(list=list_1, text='item 3')
        self.assertEqual(list(Item.objects.all()), [item_1, item_2, item_3])

    def test_string_representation(self):
        item = Item(text='some text')
        self.assertEqual(str(item), 'some text')

    def test_lists_can_have_owners(self):
        user = User.objects.create(email='a@b.com')
        new_list = List.objects.create(owner=user)
        self.assertIn(new_list, user.list_set.all())

    def test_list_owner_is_optional(self):
        List.objects.create()  # should not raise
        self.assertEqual(len(List.objects.all()), 1)

    def test_list_name_is_first_item_text(self):
        new_list = List.objects.create()
        Item.objects.create(list=new_list, text='first item')
        Item.objects.create(list=new_list, text='second item')
        self.assertEqual(new_list.name, 'first item')
