import datetime
import pytz
import logging
from Keyboardpad import Book_button

from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import CallbackQuery


tzInfo = pytz.timezone('Asia/Tashkent')
dt = datetime.datetime.now(tz=tzInfo)
API_TOKEN = '6091469143:AAGLoAoy1GbOX-UPvmksSBFTf51q1qqg-KA'
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
x = datetime.datetime.now()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    photo = "https://cdn.discordapp.com/attachments/997267800106205184/1073714083469209620/kingcs007_We_need_an_image_of_the_Telegram_bot_and_the_field_of_73d947ea-b2c8-448d-a477-9d0d2921e665.png"
    infos = f"""
😊Assalomu ALeykum<b> 🫂{message.from_user.full_name}</b>


🤖Bot Tibbiyot sohasi bo`yicha Kerakli qo`llanma va kitoblarni sizga izlashda yordam beradi
"""

    await bot.send_photo(message.from_user.id, photo, caption=infos)
    await message.answer("Button add",reply_markup=Book_button)
@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def send_welcome(message: types.Message):
    cls = f"🇺🇿Hurmatli: {message.from_user.full_name}\n\n🤖Bot: @maxsus_medbot"
    if message.text == "Infeksion nazorat":
        await message.answer_document("BQACAgIAAxkBAAM0Y-eoPAkXKCoHKyJRTSbZIju0ZNwAAiUmAAKz7RhLtuVoUck0kQ4uBA",caption=cls)
    elif message.text == "Farmakologiya(Azizova.S.S)":
        await message.answer_document("BQACAgIAAxkBAANGY-fJSqrjR6dT_MvqGGusxenXXqcAAm4mAAKz7RhLETWPZLxojG4uBA",caption=cls)
    elif message.text == "Umumiy gigiyena(Duschanova.B.A)2008y":
        await message.answer_document("BQACAgIAAxkBAANIY-fJhd_PuvocZfafa2c33vHDZyUAAmwmAAKz7RhLgxSXbruq5McuBA",caption=cls)
    elif message.text == "Xirurgik kasalliklarda hamshiralik ishi(Ziyayeva)":
        await message.answer_document("BQACAgIAAxkBAANKY-fJryszAZQvd9Vo2Qb1vnWABwsAAmsmAAKz7RhLLf-Clj1K6qguBA",caption=cls)
    elif message.text == "Pediatriyada hamshirlik ishi":
        await message.answer_document("BQACAgIAAxkBAANMY-fKmGX_fREq_GXJpFOFDXANTJIAAmomAAKz7RhL1H1PXnMNNX4uBA",caption=cls)
    elif message.text == "Akusherlik va Ginekologiya":
        await message.answer_document("BQACAgIAAxkBAANOY-fKszrCmX9u3YtAVF9lFtVISYQAAmgmAAKz7RhLW8rQNHxrzdcuBA",caption=cls)
    elif message.text == "Terapiya(M.Ziyayeva)":
        await message.answer_document("BQACAgIAAxkBAANQY-fK0HmdlsWCxaUq1JUn_uc73J4AAmUmAAKz7RhL74YBCiF6cywuBA",caption=cls)
    elif message.text == "Anatomiya Fiziologiya va Patalogiya":
        await message.answer_document("BQACAgIAAxkBAANSY-fK80HzUDqHEMcHqfq4NLHOdKwAAmImAAKz7RhLyfmUjiblODcuBA",caption=cls)
    elif message.text == "Hamshiralik ishi asoslari Zokirova.K.U":
        await message.answer_document("BQACAgIAAxkBAANUY-fLEysq7NJhwCAy6dQQM_IyUkMAAmEmAAKz7RhLJ0o4Fzz6NMkuBA",caption=cls)
    elif message.text == "Ichki kasalliklar Y.Arslonov T.Nazarov":
        await message.answer_document("BQACAgIAAxkBAANWY-fLNirgsmpcsaGg6oMk3ClzwNoAAl8mAAKz7RhL-O0PxUKhpTAuBA",caption=cls)
    elif message.text == "Tibbiy biologiya va Genetika K.Nishonboyev J.Hamidov":
        await message.answer_document("BQACAgIAAxkBAANYY-fLU3Bzk0KHuWxlUwc1qLF0WTIAAlsmAAKz7RhLlx3F4b8OJmwuBA",caption=cls)
    elif message.text == "Mikrobiol Immunol Virusol  Muhamedov.I 2006y":
        await message.answer_document("BQACAgIAAxkBAANaY-fLaTqr3z-dCoe3fC89jIj0JKkAAlYmAAKz7RhLnPOgmUY5fzMuBA",caption=cls)
    elif message.text == "Valeologiya":
        await message.answer_document("BQACAgIAAxkBAANcY-fLezN1euX7Hpvf7ESfy359vKoAAlUmAAKz7RhLk2VZ4bu-1q8uBA",caption=cls)
    elif message.text == "Yuqumli kasalliklarda hamshiralik ishi":
        await message.answer_document("BQACAgIAAxkBAANeY-fLkD1pR3Gd6MDtbnSUGmZl6_MAAlQmAAKz7RhLpD8ad52gNb0uBA",caption=cls)
    elif message.text == "Tibbiyot psixologiyasi Ibodullayev.Z 2012y":
        await message.answer_document("BQACAgIAAxkBAANgY-fLpeMtKfZ4BVb4zZdbFypLZzcAAlImAAKz7RhLPsWtKr-KjoEuBA",caption=cls)
    elif message.text == "Asab va Ruhiyat kitobi":
        await message.answer_document("BQACAgIAAxkBAANiY-fLvZocV9tCDCOJPDcOHjKAXYYAAkwmAAKz7RhLnL5TwqXIQDcuBA",caption=cls)
    elif message.text == "Jamoada hamshiralik ishi Shukurov":
        await message.answer_document("BQACAgIAAxkBAANkY-fL1DKTCYdfbJAtERVd3DYh1QADSiYAArPtGEv7TD-e9_QBuy4E",caption=cls)
    elif message.text == "Reabilitatsiya massaj va mehnat bilan davolash":
        await message.answer_document("BQACAgIAAxkBAANmY-fL9421N8MkWaCtFPin63FLZtsAAkgmAAKz7RhLXJgzp6ylzxouBA",caption=cls)
    elif message.text == "Biokimyo 1-qism Sobirova 2021y)":
        await message.answer_document("BQACAgIAAxkBAANoY-fMEUxc-ya9El4g9AJgb24xDmAAAkcmAAKz7RhL7VXssBKUzq4uBA",caption=cls)
    elif message.text == "Biokimyo 2-qism Sobirova 2021y":
        await message.answer_document("BQACAgIAAxkBAANqY-fMLjAokkiYaXPCcEHpViE40Z8AAkYmAAKz7RhL5Sydt6kzpzouBA",caption=cls)
    elif message.text == "Vrach faoliyatining huquqiy asoslari(G'iyosov.Z.A 2012y)":
        await message.answer_document("BQACAgIAAxkBAANsY-fMR12zLp75BB4sWrPgWz_PeiIAAkUmAAKz7RhLeAYAAVKBE-WnLgQ",caption=cls)
    elif message.text == "Gerontologiya va umumiy Geriatriya":
        await message.answer_document("BQACAgIAAxkBAANuY-fMYDAJiifON8bF1TiiM-GIu38AAkQmAAKz7RhLc89QTY0AAcEBLgQ",caption=cls)
    elif message.text == "Teri va Tanosil kasalliklari":
        await message.answer_document("BQACAgIAAxkBAANwY-fMc2ba3ZKvA1paUQT-8iM3CVYAAkEmAAKz7RhL8gmu_FlX2wouBA",caption=cls)
    elif message.text == "Oftalmologiya":
        await message.answer_document("BQACAgIAAxkBAANyY-fMiPykhAQ3ym6iT_i8AshDaAIAAkAmAAKz7RhLv0KCqCSFxPouBA",caption=cls)
    elif message.text == "Otarinolaringologiya A.Shamsiev N.Xushvaqova 2019y":
        await message.answer_document("BQACAgIAAxkBAAN0Y-fMm31qWitPUJ-yVWawAo7z9HcAAjgmAAKz7RhLhFzQ-2GHHc0uBA",caption=cls)
    elif message.text == "Ko'z kasalliklari 2016y":
        await message.answer_document("BQACAgIAAxkBAAN2Y-fMzPqNzFOLJ91_j3-7G0oaVVYAAv0jAAJP2RhIRd3cpr4Q9_ouBA",caption=cls)
    elif message.text == "Jarrohlik va reanimatsiya asoslarida hamshiralik ishi 2003y":
        await message.answer_document("BQACAgIAAxkBAAN4Y-fM3pBpHNX5hcjZqgaINGsAAfQ8AAJ8CQACPBcwSOi00lAv6oyiLgQ",caption=cls)
    elif message.text == "Bolalar kasalliklari(Daminov)":
        await message.answer_document("BQACAgIAAxkBAAN6Y-fM8_f-cVxFV38n27tRHV_qBB8AAosBAAKmxTBJWdnJTMpJjtUuBA",caption=cls)
    elif message.text == "Odam anatomiyasi Atlas 1-jild N.Ahmedov":
        await message.answer_document("BQACAgIAAxkBAAN8Y-fNDBunkdsZxI0qsCA7g8Pd_2MAAnsBAAI8NohJVpce_3LTpXAuBA",caption=cls)
    elif message.text == "Abu Ali Ibn Sino Tib qonunlari.2-jild":
        await message.answer_document("BQACAgIAAxkBAAOAY-fNSjI1Glz1ipC7hFPGbDZ9M6IAAnskAALZkAABSdGdOlhxghOwLgQ",caption=cls)
    elif message.text == "Tibbiyot kasbiga kirish":
        await message.answer_document("BQACAgIAAxkBAAOCY-fNY1LJrtay-RBzy1kpW_w_mMwAAngfAAKkDAlI2J9t9chvOyYuBA",caption=cls)
    elif message.text == "Ingliz tili 1-2-kurs":
        await message.answer_document("BQACAgIAAxkBAAOEY-fNjetmHHT8MqrHLZio6sIU3sEAAnImAAKz7RhL5PX886Agr2MuBA",caption=cls)
    elif message.text == "Rus tili gramatikasi":
        await message.answer_document("BQACAgIAAxkBAAOGY-fNpw6_mGw5MWg5BLNjAWu6jyUAAnAmAAKz7RhLHw5UqUsGA8guBA",caption=cls)
    elif message.text == "Lotin tili Xo'jayeva.L.U-2005y":
        await message.answer_document("BQACAgIAAxkBAAOIY-fNvrwxjxn08pvKEWfTytMWWbYAAmMmAAKz7RhLUVERaqnUMNIuBA",caption=cls)
    elif message.text == "O'zbekiston tarixi":
        await message.answer_document("BQACAgIAAxkBAAOKY-fN0yuRAdBePz7_Dqdu1RppnrUAAlcmAAKz7RhLiRvsgWprGzYuBA",caption=cls)
    elif message.text == "Informatika":
        await message.answer_document("BQACAgIAAxkBAAOMY-fN5U3xegpUMFRABv0sQZD2sNAAAl0mAAKz7RhLGyVvzBWWurYuBA",caption=cls)
    elif message.text == "Jamoat salomatligi va sog'liqni saqlash bosh.Mamatqulov":
        await message.answer_document("BQACAgIAAxkBAAOOY-fOBsIfYXTgCJiyULjrQuv4vTgAAicmAAKz7RhLPgEiI-1dMMUuBA",caption=cls)
    elif message.text == "Sport tibbiyoti va reabilitologiya.Darslik":
        await message.answer_document("BQACAgIAAxkBAAOQY-fOLeQJvexA8oLvAsKkg_6fN3kAAismAAKz7RhLOgtgKry3TzYuBA",caption=cls)
    elif message.text == "Kasb kasalliklari":
        await message.answer_document("BQACAgIAAxkBAAOSY-fOQb8H3-Ecm2W-yJMftHS1AWIAAjAmAAKz7RhL7mWjMvtR3pcuBA",caption=cls)
    elif message.text == "Abu Ali Ibn Sino.Tib qonunlari.1-jild":
        await message.answer_document("BQACAgIAAxkBAAN-Y-fNHjmC7JfDJXgdMH74nNIMYawAAmskAALZkAABSSe3mTV2_o-bLgQ",caption=cls)
    elif message.text == "Abu Ali Ibn Sino Tib qonunlari.1-jild":
        await message.answer_document("BQACAgIAAxkBAAIB32Pn2-fFQP9LvMQh7yQSf2g3HH9iAAJrJAAC2ZAAAUknt5k1dv6Pmy4E",caption=cls)
    elif message.text == "Fitoterapiya 213-y":
        await message.answer_document("BQACAgIAAxkBAAICEWPn5DN2sbsb5RnFIk_a8MXsxHPgAALVAwAC19IQSmT2JeEAAUi9cS4E",
                                      caption=cls)

    else:
        await message.answer_sticker(sticker='CAACAgIAAxkBAAEHsTdj594-6FVB-ZTndW4NHdoh6u31jgACJAIAAladvQp7NaMbcOWxxy4E')
        await message.answer("Bu mavzuga oid kitob topilmadi😢")

@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def file_viewer(message: types.Message):
    await message.answer(f"File Id->  <code>{message.document.file_id}</code>")
@dp.message_handler(commands=['virus'])
async def send_welcome2132(message: types.Message):
    API_TOKEN = "0"
   
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
