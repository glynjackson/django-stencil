from django.contrib import messages
from django.views.generic.edit import ModelFormMixin


class CrudMixin(ModelFormMixin):
    """

    """
    ACTION_ADD = 'add'
    ACTION_UPDATE = 'update'
    ACTION_DELETE = 'delete'

    action = None
    #  Allow default success message to be overridden
    success_msg = None

    def get_success_url(self):
        """
        Before we return the success URL, we build the success Flash message to display after redirect. A custom
        message may have been set on the model. By default a message is built based on the model name and the action
        """
        if self.success_msg:
            msg = self.success_msg
        else:
            if self.action == CrudMixin.ACTION_ADD:
                activity = "added"
            elif self.action == CrudMixin.ACTION_UPDATE:
                activity = "updated"
            else:
                activity = "deleted"

            msg = '%s successfully %s' % (self.model._meta.verbose_name.title(), activity)

        messages.success(self.request, msg)

        # clear down referrer from session
        if 'referrer' in self.request.session:
            del self.request.session['referrer']

        return super(CrudMixin, self).get_success_url()

    def get_template_names(self):
        ''' We try to re-use templates, so if the action is add, update or delete, use a generic template,
            otherwise delegate to super method. The super method will use template_name if set
            '''
        if self.template_name:
            return self.template_name

        if self.action in (CrudMixin.ACTION_UPDATE, CrudMixin.ACTION_ADD):
            self.template_name = 'generic/create_update_form.html'
        elif self.action == CrudMixin.ACTION_DELETE:
            self.template_name = 'generic/confirm_delete.html'

        if self.template_name:
            templates = [self.template_name]
            return templates

        return super(CrudMixin, self).get_template_names()


    def get_context_data(self, **kwargs):
        context = super(CrudMixin, self).get_context_data(**kwargs)
        context['action'] = self.action
        context['model'] = self.model
        context['model_name'] = self.model._meta.verbose_name
        context['referrer'] = self.request.session['referrer'] if 'referrer' in self.request.session else None

        return context

    def get(self, request, *args, **kwargs):
        # referrer is used for cancel links. If the form does not validate, the standard HTTP_REFERER
        # will be incorrect/itself, so we store on GET request, and this gets cleared down on redirect-after-post
        if request.method == 'GET' and 'HTTP_REFERER' in request.META:
            referrer = request.META['HTTP_REFERER']
            request.session['referrer'] = referrer

        return super(CrudMixin, self).get(request, *args, **kwargs)

    def get_form_kwargs(self):
        """
        Pass cancel link to form as kwargs so that they can be applied to form cancel buttons
        """
        kwargs = super(CrudMixin, self).get_form_kwargs()
        referrer = self.request.session['referrer'] if 'referrer' in self.request.session else None
        kwargs.update({'referrer': referrer})

        return kwargs