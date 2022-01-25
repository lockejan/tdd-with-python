from django.test import TestCase
from lists.forms import ItemForm, EMPTY_ITEM_ERROR
from lists.models import Item, List


class ItemFormTest(TestCase):
    def test_form_render_item_text_input(self):
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
