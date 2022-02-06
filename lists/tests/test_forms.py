from django.test import TestCase
from lists.forms import (ItemForm, EMPTY_ITEM_ERROR, DUPLICATE_ITEM_ERROR,
                         ExistingListItemForm)
from lists.models import Item, List


class ItemFormTest(TestCase):
    def test_form_renders_item_text_input(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_ITEM_ERROR])

    def test_form_save_handles_saving_to_a_list(self):
        form = ItemForm(data={'text': 'to do'})
        new_list = List.objects.create()
        new_item = form.save(for_list=new_list)
        self.assertEqual(new_item, Item.objects.first())
        self.assertEqual(new_item.text, 'to do')
        self.assertEqual(new_item.list, new_list)


class ExistingListItemFormTest(TestCase):
    def test_form_renders_item_text_input(self):
        new_list = List.objects.create()
        form = ExistingListItemForm(for_list=new_list)
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())

    def test_form_validation_for_blank_items(self):
        new_list = List.objects.create()
        form = ExistingListItemForm(for_list=new_list, data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_ITEM_ERROR])

    def test_form_validation_for_duplicate_items(self):
        new_list = List.objects.create()
        Item.objects.create(list=new_list, text='no twins!')
        form = ExistingListItemForm(for_list=new_list,
                                    data={'text': 'no twins!'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [DUPLICATE_ITEM_ERROR])
