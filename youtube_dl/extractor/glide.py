# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class GlideIE(InfoExtractor):
    IE_DESC = 'Glide mobile video messages (glide.me)'
    _VALID_URL = r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    _TEST = {
        'url': 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==',
        'md5': '4466372687352851af2d131cfaa8a4c7',
        'info_dict': {
            'id': 'UZF8zlmuQbe4mr+7dCiQ0w==',
            'ext': 'mp4',
            'title': 'Damon Timm\'s Glide message',
            'thumbnail' : 'http://dk608k4lm7m9j.cloudfront.net/3ee7da5af87065a1eeb8c6c9a864ba5b_2.jpg'
        }
    }

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)
        title = self._html_search_regex(r'<title>(.*?)</title>', webpage, 'title')
        video_url = self._search_regex(r'<source src="(.*?)" type="video/mp4">', webpage, 'video_url')
        thumbnail_url = self._search_regex(r'<img id="video-thumbnail" src="(.*?)" alt="Video thumbnail">', webpage, 'thumbnail_url')

        return {
            'id': video_id,
            'title': title,
            'url' : 'http:' + video_url,
            'thumbnail' : 'http:' + thumbnail_url
        }
