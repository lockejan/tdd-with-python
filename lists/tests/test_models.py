from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from lists.models import Item, List

User = get_user_model()


class ItemModelTest(TestCase):
    def test_default_text(self):
        item = Item()
        self.assertEqual(item.text, "")

    def test_item_is_related_to_list(self):
        new_list = List.objects.create()
        item = Item()
        item.list = new_list
        item.save()
        self.assertIn(item, new_list.item_set.all())

    def test_cannot_save_empty_list(self):
        new_list = List.objects.create()
        item = Item(list=new_list, text="")
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()


class ListModelTest(TestCase):
    def test_get_absolute_url(self):
        new_list = List.objects.create()
        self.assertEqual(new_list.get_absolute_url(), f"/lists/{new_list.id}/")

    def test_duplicate_items_are_invalid(self):
        new_list = List.objects.create()
        Item.objects.create(list=new_list, text="Coffee Beans")
        with self.assertRaises(ValidationError):
            item = Item(list=new_list, text="Coffee Beans")
            item.full_clean()
            # item.save()

    def test_CAN_save_same_item_to_different_lists(self):
        list_1 = List.objects.create()
        list_2 = List.objects.create()
        Item.objects.create(list=list_1, text="Coffee Beans")
        item = Item(list=list_2, text="Coffee Beans")
        item.full_clean()  # should not raise

    def test_list_ordering(self):
        list_1 = List.objects.create()
        item_1 = Item.objects.create(list=list_1, text="i1")
        item_2 = Item.objects.create(list=list_1, text="item 2")
        item_3 = Item.objects.create(list=list_1, text="item 3")
        self.assertEqual(list(Item.objects.all()), [item_1, item_2, item_3])

    def test_string_representation(self):
        item = Item(text="some text")
        self.assertEqual(str(item), "some text")

    def test_create_new_creates_list_and_first_item(self):
        List.create_new(first_item_text="new item text")
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, "new item text")
        new_list = List.objects.first()
        self.assertEqual(new_item.list, new_list)

    def test_create_new_optionally_saves_owner(self):
        user = User.objects.create()
        List.create_new(first_item_text="new item text", owner=user)
        new_list = List.objects.first()
        self.assertEqual(new_list.owner, user)

    def test_lists_can_have_owner(self):
        List(owner=User())  # should not raise

    def test_list_owner_is_optional(self):
        List().full_clean()  # should not raise

    def test_create_returns_new_list_object(self):
        returned = List.create_new(first_item_text="new item text")
        new_list = List.objects.first()
        self.assertEqual(returned, new_list)

    def test_list_name_is_first_item_text(self):
        new_list = List.objects.create()
        Item.objects.create(list=new_list, text="first item")
        Item.objects.create(list=new_list, text="second item")
        self.assertEqual(new_list.name, "first item")
