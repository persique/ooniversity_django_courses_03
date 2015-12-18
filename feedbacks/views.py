from django.shortcuts import render
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.core.mail import mail_admins
from feedbacks.forms import FeedbackForm
from feedbacks.models import Feedback

class FeedbackView(CreateView):
    model = Feedback
    template_name = 'feedback.html'
    form_class = FeedbackForm
    context_object_name = 'form'
    success_url = reverse_lazy('feedback')
    #success_message = u"Thank you for your feedback! We will keep in touch with you very soon!"
    
    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context['title'] = "Feedback"
        return context 

    def form_valid(self, form):
        feedback = form.save()
        messages.success(self.request, u"Thank you for your feedback! We will keep in touch with you very soon!")
        mail_admins(feedback.subject, feedback.message)
        return super(FeedbackView, self).form_valid(form)

