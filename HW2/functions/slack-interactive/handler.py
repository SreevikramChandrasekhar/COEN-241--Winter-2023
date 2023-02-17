import json
import urllib

def handle(req):
    urlstring = urllib.unquote(req).decode('utf8').strip('payload=')
    response = json.loads(urlstring)
    data = {
            "attachments": [
                {
                    "replace_original": True,
                    "response_type": "Testing interactive",
                    "fallback": "Required interactive testing - summary of the atachment",
                    "color": "#36a64f",
                    "pretext": "Ahh yeah! Great choice, COEN 241 is absolutely amazing!",
                    "author_name": "Sreevikram Chandrasekhar",
                    "author_link": "https://github.com/SreevikramChandrasekhar/COEN-241--Winter-2023",
                    "author_icon": "https://avatars.githubusercontent.com/SreevikramChandrasekhar",
                    "title": "COEN 241",
                    "title_link": "https://www.scu.edu/engineering/academic-programs/department-of-computer-engineering/graduate/course-descriptions/",
                    "text": "Head over to COEN 241",
                    "image_url": "https://www.scu.edu/media/offices/umc/scu-brand-guidelines/visual-identity-amp-photography/visual-identity-toolkit/logos-ap-seals/Mission-Dont3.png",
                    "thumb_url": "https://www.scu.edu/engineering/academic-programs/department-of-computer-engineering/graduate/course-descriptions/",
                    "footer": "Slack Apps built on OpenFaas",
                    "footer_icon": "https://a.slack-edge.com/45901/marketing/img/_rebrand/meta/slack_hash_256.png",
                    "ts": 123456789
                    }
                ]
            }
    return json.dumps(data)
