from typing import Tuple, Any, Optional
from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from config import I18N_DOMAIN, LOCALES_DIR


async def get_lang(user_id):
    return None


class ACLMidlleware(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]) -> Optional[str]:
        user = types.User.get_current()
        return await get_lang(user.id) or user.locale


def setup_middleware(dp):
    i18n = ACLMidlleware(I18N_DOMAIN, LOCALES_DIR)
    dp.middleware.setup(i18n)
    return i18n
