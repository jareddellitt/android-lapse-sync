from dropbox import client, session
import config

ACCESS_TYPE = 'app_folder'

def create_new_session():
    sess = session.DropboxSession(config.get_key(), config.get_secret(), ACCESS_TYPE)
    request_token = sess.obtain_request_token()

    print((sess.build_authorize_url(request_token)))
    print("Visit this website and press the 'Allow' button, then hit 'Enter' here: ")

    raw_input()

    access_token = sess.obtain_access_token(request_token)
    config.save_access_token(access_token.key, access_token.secret)

    return sess

def get_previous_session():
    sess = None
    token_key, token_secret = config.get_access_token()

    if token_key and token_secret:
        sess = session.DropboxSession(config.get_key(), config.get_secret(), ACCESS_TYPE)
        sess.set_token(token_key, token_secret)

    return sess

def create_session():
    sess = get_previous_session()

    if not sess:
        sess = create_new_session()

    return sess

def get_client():
    return client.DropboxClient(create_session())