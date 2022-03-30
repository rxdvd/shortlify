def test_home(api):
    resp = api.get('/')
    assert resp.status == '200 OK'
    assert b'Shortlify - Make a short URL!' in resp.data

def test_submit_link(api):
    form_data = {'url': 'http://example.com'}
    resp = api.post('/', data=form_data)
    assert resp.status == '201 CREATED'
    assert b'Shortlify - Your shortened URL' in resp.data
