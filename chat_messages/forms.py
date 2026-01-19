from django import forms
from emoji_picker.widgets import EmojiPickerTextInput
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {'content': EmojiPickerTextInput()}
