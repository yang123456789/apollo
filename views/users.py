import tornado.web
from tornado.escape import json_decode
import logging
from views.base import *
from models import Users, session
import re
import tornado.locale


class Register(tornado.web.RequestHandler):
    def get_user_locale(self):
        # print(tornado.locale.Locale.get(120))
        # print(dir(tornado.locale.Locale))

        # if user_locale == 'en':
        #     return tornado.locale.get('en_US')
        tornado.locale.set_default_locale('zh_CN')
        user_locale = self.get_argument('lang', None)
        print(user_locale)
        print(tornado.locale.get('zh_CN'))
        return tornado.locale.get('zh_CN')

    def post(self):
        _ = self.locale.translate
        try:
            param = json_decode(self.request.body)
            logging.info(param)
            username = param.get('username')
            password = param.get('password')
            phone = param.get('phone')
            email = param.get('email')
            validate = self.validate(username, password, phone, email)
            if validate is True:
                self.save(username, password, phone, email)
                return self.write(render_200(_('register successfully')))
            return self.write(validate)
        except Exception as e:
            logging.error(e)
            return self.write(render_412(message=_('The param invalid')))

    def validate(self, username, password, phone, email):
        _ = self.locale.translate
        if not username or not re.match('^[a-zA-Z][a-zA-Z0-9]{3,19}$', username):
            return render_400(_('The username begins with the alphabet and contains alphanumeric 4 to 20 bits.'))
        elif Users.get_by_username(username):
            return render_400(_('The username had been registered'))
        elif not password:
            return render_400(_('The password does not None'))
        elif not phone or not re.match('^1(3|4|5|7|8)\d{9}$', phone):
            return render_400(_('The phone invalid'))
        elif Users.get_by_phone(phone):
            return render_400(_('The phone had been registered'))
        elif not email or re.match('^\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}$', email):
            return render_400(_('The email invalid'))
        elif Users.get_by_email(email):
            return render_409(_('The email had been registered'))
        return True

    def save(self, username, password, phone, email):
        pwd = encrypt(password)
        user = Users(username=username, password=pwd, phone=phone, email=email)
        session.add(user)
        session.commit()
        session.close()
        return True
