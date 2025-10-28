from django import forms

class MixerForm(forms.Form):
    file = forms.FileField(
        label="Add file",
        allow_empty_file=False,
        widget = forms.FileInput(attrs={
            'placeholder': 'Add file',
            'title': 'Only .txt files are allowed',
            'class': 'form-control'
        })
    )

    def clean_file(self):
        _file = self.cleaned_data.get('file')
        if _file:
            if not _file.name.endswith('.txt'):
                raise forms.ValidationError("Only .txt files are allowed")
        return _file
