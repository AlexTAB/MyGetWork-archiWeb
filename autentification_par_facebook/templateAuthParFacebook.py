{% if error %}
      {% if error == 'AUTH_FAILED' %}
          <p>Authentication failed</p>
      {% else %}{% if error == 'AUTH_DISABLED' %}
          <p>Your account is disabled</p>
      {% else %}{% if error == 'AUTH_DENIED' %}
          <p>You did not allow access</p>
       {% endif %}{% endif %}{% endif %}
  {% else %}
    <a href="https://graph.facebook.com/oauth/authorize?client_id={{ settings.FACEBOOK_APP_ID }}&redirect_uri={{ settings.FACEBOOK_REDIRECT_URI }}&scope=publish_stream,email&display=popup">
      <img src="http://developers.facebook.com/images/devsite/login-button.png"/>
    </a>
  {% endif %}

