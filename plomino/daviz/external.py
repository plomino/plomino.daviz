""" Utilities to get data from External URL
"""
from zope.interface import implements
from zope.globalrequest import getRequest

from eea.app.visualization.data.external import ExternalData
from eea.app.visualization.data.interfaces import IExternalData

class DynamicExternalData(ExternalData):
    """ Overrives eea.app.visualization ExternalData utility to re-inject
    current querystring parameters in the external url. 
    """
    implements(IExternalData)

    def _inject_querystring(self, url):
        request = getRequest()
        querystring = request["QUERY_STRING"]
        if '?' in url:
            url += "&" + querystring
        else:
            url += "?" + querystring
        return url

    def test(self, url, timeout=15):
        """ Test to see if provided URL is a valid URL
        """
        return ExternalData.test(self, self._inject_querystring(url), timeout)

    def __call__(self, url, timeout=15):
        """ Get data and convert it to TSV if possible
        """
        return ExternalData.__call__(
            self,
            self._inject_querystring(url),
            timeout
        )
