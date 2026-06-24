class BootstrapFormMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        for campo in form.fields.values():
            campo.widget.attrs["class"] = "form-control"

        return form
