from django import forms
from django.forms import ModelForm, Textarea
from jhpl_ims.models import jhpl_ims_masterlist, incident
from tempus_dominus.widgets import DateTimePicker
from django.core.files.uploadedfile import InMemoryUploadedFile
from jhpl_ims.humanize import naturalsize


class CommentForm(forms.Form):
    comment = forms.CharField()


class MasterListForm(forms.ModelForm):
    class Meta:
        model = jhpl_ims_masterlist
        exclude = ["owner"]

        widgets = {
            'doc_num': forms.TextInput(attrs={'class': 'form-control'}),
            'doc_title': forms.TextInput(attrs={'class': 'form-control'}),
            'rev_num': forms.NumberInput(attrs={'class': 'form-control'}),
            'issue_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'reviewed_by': forms.Select(attrs={'class': 'form-control'}),
            'reviewed_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'approved_by': forms.Select(attrs={'class': 'form-control'}),
            'approved_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'control_copy_num': forms.NumberInput(attrs={'class': 'form-control'}),
        }



# Create the form class.
class CreateForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)

    # Call this 'picture' so it gets copied from the form to the in-memory model
    # It will not be the "bytes", it will be the "InMemoryUploadedFile"
    # because we need to pull out things like content_type
    picture = forms.FileField(required=False, label='File to Upload <= '+max_upload_limit_text)
    upload_field_name = 'picture'

    # Hint: this will need to be changed for use in the ads application :)
    class Meta:
        model = incident
        fields = ['incident_datetime','people_involved','incident_location','incident_description','incident_witness','picture']  # Picture is manual
        widgets = {
            'incident_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }
    # Validate the size of the picture
    def clean(self):
        cleaned_data = super().clean()
        pic = cleaned_data.get('picture')
        if pic is None:
            return
        if len(pic) > self.max_upload_limit:
            self.add_error('picture', "File must be < "+self.max_upload_limit_text+" bytes")

    # Convert uploaded File object to a picture
    def save(self, commit=True):
        instance = super(CreateForm, self).save(commit=False)

        # We only need to adjust picture if it is a freshly uploaded file
        f = instance.picture   # Make a copy
        if isinstance(f, InMemoryUploadedFile):  # Extract data from the form to the model
            bytearr = f.read()
            instance.content_type = f.content_type
            instance.picture = bytearr  # Overwrite with the actual image data

        if commit:
            instance.save()
       

        return instance