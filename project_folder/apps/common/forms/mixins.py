from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Div


class CrispyFormMixin(object):
    """
    Mixin that provides base layout for Bootstrap forms using crispy forms app.
    """
    submit_button_text = 'Save'
    cancel_link = ''

    def __init__(self, *args, **kwargs):
        # extract any kwarg passed in before calling super
        self.referrer = kwargs.pop('referrer', None)

        super(CrispyFormMixin, self).__init__(*args, **kwargs)

        if self.referrer:
            self.cancel_link = '<a href="%s" class="btn">Cancel</a>&nbsp;' % self.referrer

        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.form_action_layout = Layout(
            Div(
                Submit('submit', self.submit_button_text),
                HTML(self.cancel_link),
                css_class='form-group form-action'
            ),
        )