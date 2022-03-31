def test_home(api):
    resp = api.get('/')
    assert resp.status == '200 OK'
    assert b'Shortlify - Make a short URL!' in resp.data

def test_submit_link(api):
    form_data = {'url': 'http://example.com'}
    resp = api.post('/', data=form_data)
    assert resp.status == '200 OK'
    assert b'Shortlify - Your shortened URL' in resp.data

def test_submit_invalid_link(api):
    form_data = {'url': 'not_a_url'}
    resp = api.post('/', data=form_data)
    assert resp.status == '400 BAD REQUEST'
    assert b'Invalid URL.' in resp.data

def test_redirect(api):
    resp = api.get('/12345')
    assert resp.status == '302 FOUND'
    assert b'<a href="http://example.com">http://example.com</a>' in resp.data

def test_home_redirect(api):
    resp = api.get('54321')
    assert resp.status == '302 FOUND'
    assert b'<a href="/">/</a>' in resp.data
