from slackclient import SlackClient
import os
slack_token = "xoxp-292441824967-291380213314-385123399780-ede8482aba5a12a03ff3345d9068d91d"
sc = SlackClient(slack_token)

class slackclient():
  def __init__(self, message, channel):
    self.message = message
    sc.api_call(
      "chat.postMessage",
      channel=channel,
      text= message
    )