from django import forms

class MixerForm(forms.Form):
    file = forms.FileField(
        label="Add file .txt",
        allow_empty_file=False
    )

    def clean_file(self):
        _file = self.cleaned_data.get('file')
        if _file:
            if not _file.name.endswith('.txt'):
                raise forms.ValidationError("Only .txt files are allowed")
        return _file
