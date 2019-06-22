from django.db import models
from django.utils.translation import ugettext as _
from furl import furl
from rest_framework.utils import json


class Message(models.Model):
    """
        A message with multiple recipients (or single recipient )
    """

    to = models.CharField(max_length=15, verbose_name=_("Recipient of the message"),
                                help_text=_("Recipient of the message"))
    message = models.CharField(max_length=500, verbose_name=_("Message Text"), help_text=_("Message Text"))

    block_code = models.IntegerField(blank=True, null=True, verbose_name=_("Block Code"), help_text=_("Block Code"))

    last_try = models.DateTimeField(blank=True, null=True)


class Operator(models.Model):
    """
        The Operator that messages are sent by
    """

    name = models.CharField(max_length=255, verbose_name=_("Operator Name"), help_text=_("A name for the operator"))

    username = models.CharField(max_length=255, verbose_name=_("Username"), help_text=_("User name given by operator"))
    password = models.CharField(max_length=255, verbose_name=_("Password"), help_text=_("Password given by operator"))

    sender = models.CharField(max_length=15, verbose_name=_("Sender Phone Number"),
                              help_text=_("The operator phone number"))

    retry_gap_time = models.IntegerField(verbose_name=_("Retry Gap Time"),
                                         help_text=_("Time in minutes before you can try to send a message again"))

    api_endpoint = models.CharField(max_length=500, verbose_name=_("API Endpoint"), help_text=_("API Endpoint"))

    def send_message(self, message):
        """
        Take a message and sends it
        :param message:
        :return:
        """

        api = furl(self.api_endpoint)

        api.args['uname'] = self.username
        api.args['pass'] = self.password
        api.args['from'] = self.sender
        api.args['msg'] = message.message






