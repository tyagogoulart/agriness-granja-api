from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)

  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

def get_token_bearer(user):
    token = get_tokens_for_user(user)
    return 'Bearer {0}'.format(token['access'])