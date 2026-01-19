from django import forms
from emoji_picker.widgets import EmojiPickerTextInput
from .models import Message

class MessageForm(forms.ModelForm):
    content = forms.CharField(
    label='',
    widget=EmojiPickerTextInput(attrs={'class': 'form-input', 'placeholder': 'Tapez votre message…'})
    )
    class Meta:
        model = Message
        fields = ['content']