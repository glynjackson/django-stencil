from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from project_folder.apps.common.views.mixins import CrudMixin


class BaseListView(ListView):

    def get_context_data(self, **kwargs):
        context = super(BaseListView, self).get_context_data(**kwargs)
        context['action'] = 'list'
        context['model'] = self.model
        context['model_name'] = self.model._meta.verbose_name
        context['model_name_plural'] = self.model._meta.verbose_name_plural

        return context

    # TODO pagination


class BaseCreateView(CrudMixin, CreateView):
    action = CrudMixin.ACTION_ADD


class BaseUpdateView(CrudMixin, UpdateView):
    action = CrudMixin.ACTION_UPDATE


class BaseDeleteView(CrudMixin, DeleteView):
    action = CrudMixin.ACTION_DELETE
    bypass_related_objects = False

    def _get_related_objects(self):
        """
        Check if model has any related objects
        See http://stackoverflow.com/questions/2233883/get-all-related-django-model-objects
        """
        links = [rel.get_accessor_name() for rel in self.get_object()._meta.get_all_related_objects()]
        if links:
            related_objects = []
            for link in links:
                try:
                    objects = getattr(self.get_object(), link).all()
                    for object in objects:
                        related_objects.append(object)
                except ObjectDoesNotExist:
                    pass
            return related_objects
        return None


    def get_context_data(self, **kwargs):
        context = super(BaseDeleteView, self).get_context_data(**kwargs)

        # check if we have any related objects, unless explicitly indicated to bypass them
        if not self.bypass_related_objects:
            related_objects = self._get_related_objects()
            if related_objects:
                context['related_objects'] = related_objects
        context['action'] = self.action

        return context