BASE_URL = 'http://result.rgpv.ac.in/result/'

RESULT_SUFFIX = 'BErslt.aspx'

HEADERS_GET = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 \
    Firefox/66.0',

    'Accept': 'text/html,application/xhtml+xml,application/\
    xml;q=0.9,*/*;q=0.8',

    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'http://result.rgpv.ac.in/result/ProgramSelect.aspx',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

HEADERS_POST = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 \
    Firefox/66.0',

    'Accept': 'text/html,application/xhtml+xml,application/\
    xml;q=0.9,*/*;q=0.8',

    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'http://result.rgpv.ac.in/result/BErslt.aspx',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

COOKIES = {
    '_ga': 'GA1.3.1812489123.1656755485',
    'ASP.NET_SessionId': 'kyuhqc55rhinol550ybgdbej',
}

TIMEOUT = 5
