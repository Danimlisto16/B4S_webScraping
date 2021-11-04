import pdfkit

options = {
    'page-size':
    'A4',
    'margin-top':
    '0.75in',
    'margin-right':
    '0.75in',
    'margin-bottom':
    '0.75in',
    'margin-left':
    '0.75in',
    'encoding':
    "UTF-8",
    'custom-header': [('Denied-Encoding', 'gzip')],
    'cookie': [
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'no-outline':
    None
}

pdfkit.from_url(
    'https://samuel-vidovich.medium.com/3-cool-python-libraries-that-will-save-you-time-and-effort-27fcdc6762d5',
    './test.pdf',
    options=options)
