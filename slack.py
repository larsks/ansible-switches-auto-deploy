from dataclasses import dataclass, asdict
import requests
import json

class SlackBase:
    def asjson(self, **kwargs):
        return json.dumps(asdict(self), **kwargs)

@dataclass
class SlackMarkdown(SlackBase):
    text: str
    type: str = 'mrkdwn'

@dataclass
class SlackBlock(SlackBase):
    type: str
    text: SlackMarkdown|None

@dataclass
class SlackAttachment(SlackBase):
    color: str
    blocks: list[SlackBlock]


@dataclass
class SlackMessage(SlackBase):
    attachments: list[SlackAttachment]


@dataclass
class SlackNotifier(SlackBase):
    notify_url: str
    username: str
    channel: str

    def notify(self, message: SlackMessage):
        pass


message = SlackMessage(attachments=[
        SlackBlock(type="text", text=SlackMarkdown(text="This is a test"))
    ])
