#!/bin/python
# This is probably some of the ugliest shit.
# We run the given text through a series of tests;
#   If one test succeeds; get content.
# Else
#   If all tests fail
#       get direct content.


class Provider(object):
    def youtube_provide(self, url):
            provider_base = "plugin://plugin.video.youtube/play/?video_id="
            provider_match = "watch?v="
            pos = url.find(provider_match);
            if pos == -1:
                return ""
            else:
                return provider_base + url[pos + len(provider_match):]


    def provide(self, url):
        if "www.youtube.com" in url:
            return self.youtube_provide(url)
        else:
            return url

