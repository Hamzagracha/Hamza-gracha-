import telebot
from telebot import types
from PIL import Image, ImageEnhance, ImageFilter
import io
import datetime

API_TOKEN = "8391245798:AAFePNKbTQ4tXdRoLGjGKPQPRthCbgd7ztU"
CHANNEL_LINK = "https://t.me/H4x_Droid"
INSTAGRAM_LINK = "https://www.instagram.com/nxv_6"

bot = telebot.TeleBot(API_TOKEN)

# تخزين الصورة الأصلية لكل مستخدم
user_original_images = {}

# قائمة 30 فلتر احترافي
FILTERS = [
    ("📱 iPhone 17 Pro", "iphone17"),
    ("📱 iPhone Natural", "iphone_nat"),
    ("📱 iPhone Portrait", "iphone_portrait"),
    ("🎥 Cinematic", "cinematic"),
    ("🎥 Teal & Orange", "teal_orange"),
    ("🎨 Vintage", "vintage"),
    ("🎨 Retro Film", "retro"),
    ("🎨 Fuji Film", "fuji"),
    ("📷 DSLR Sharp", "dslr"),
    ("📷 Canon", "canon"),
    ("📷 Sony HDR", "sony"),
    ("📷 Nikon", "nikon"),
    ("🌌 Neon Glow", "neon"),
    ("🌌 Cyberpunk", "cyberpunk"),
    ("🌈 HDR Boost", "hdr"),
    ("🌈 Vibrant Colors", "vibrant"),
    ("🕶️ Black & White", "bw"),
    ("🕶️ Matte B&W", "matte_bw"),
    ("✨ Pro Enhance", "pro_enhance"),
    ("✨ Beauty Glow", "beauty"),
    ("✨ Smooth Skin", "skin"),
    ("🌀 Portrait Blur", "blur_bg"),
    ("🌀 Soft Blur", "soft_blur"),
    ("🔥 Warm Tone", "warm"),
    ("❄️ Cool Tone", "cool"),
    ("🌅 Sunset", "sunset"),
    ("🌃 Night Mode", "night"),
    ("🖼️ Cartoon", "cartoon"),
    ("🎭 Dramatic", "dramatic"),
    ("🎭 Moody", "moody")
]

# ==============================
# التحقق من ساعات العمل
# ==============================

# دالة تضمن أن البوت نشط دائماً (24 ساعة)
def is_active_hours():
    return True

# مثال على استخدام الدالة في البوت
@bot.message_handler(commands=['start'])
def start_message(message):
    if is_active_hours():
        bot.send_message(message.chat.id, "مرحباً! البوت يعمل الآن ✅")
    else:
        bot.send_message(message.chat.id, "خارج ساعات العمل ⏰")

# ==============================
# دوال الفلاتر
# ==============================
def apply_filter(img, filter_name):
    img = img.convert("RGB")  # لضمان عمل كل الفلاتر
    if filter_name == "iphone17":
        img = ImageEnhance.Color(img).enhance(1.8)
        img = ImageEnhance.Sharpness(img).enhance(2.0)

    elif filter_name == "iphone_nat":
        img = ImageEnhance.Contrast(img).enhance(1.2)
        img = ImageEnhance.Color(img).enhance(1.2)

    elif filter_name == "iphone_portrait":
        img = img.filter(ImageFilter.GaussianBlur(3))
        img = ImageEnhance.Contrast(img).enhance(1.4)

    elif filter_name == "cinematic":
        img = ImageEnhance.Contrast(img).enhance(1.4)
        img = ImageEnhance.Color(img).enhance(1.3)

    elif filter_name == "teal_orange":
        img = ImageEnhance.Color(img).enhance(2.0)
        img = ImageEnhance.Brightness(img).enhance(1.1)

    elif filter_name == "vintage":
        img = ImageEnhance.Color(img).enhance(0.6)
        img = ImageEnhance.Brightness(img).enhance(1.1)

    elif filter_name == "retro":
        img = img.filter(ImageFilter.SMOOTH_MORE)
        img = ImageEnhance.Color(img).enhance(0.7)

    elif filter_name == "fuji":
        img = ImageEnhance.Color(img).enhance(1.5)
        img = ImageEnhance.Brightness(img).enhance(1.2)

    elif filter_name == "dslr":
        img = ImageEnhance.Sharpness(img).enhance(3.0)
        img = ImageEnhance.Contrast(img).enhance(1.7)

    elif filter_name == "canon":
        img = ImageEnhance.Color(img).enhance(1.4)
        img = ImageEnhance.Sharpness(img).enhance(2.0)

    elif filter_name == "sony":
        img = ImageEnhance.Contrast(img).enhance(1.8)
        img = ImageEnhance.Sharpness(img).enhance(2.5)

    elif filter_name == "nikon":
        img = ImageEnhance.Brightness(img).enhance(1.3)
        img = ImageEnhance.Color(img).enhance(1.2)

    elif filter_name == "neon":
        img = ImageEnhance.Color(img).enhance(2.0)
        img = ImageEnhance.Brightness(img).enhance(1.2)

    elif filter_name == "cyberpunk":
        img = ImageEnhance.Color(img).enhance(2.5)
        img = ImageEnhance.Contrast(img).enhance(1.5)

    elif filter_name == "hdr":
        img = ImageEnhance.Contrast(img).enhance(1.8)
        img = ImageEnhance.Sharpness(img).enhance(2.5)

    elif filter_name == "vibrant":
        img = ImageEnhance.Color(img).enhance(2.0)

    elif filter_name == "bw":
        img = img.convert("L")

    elif filter_name == "matte_bw":
        img = img.convert("L")
        img = ImageEnhance.Brightness(img).enhance(1.1)

    elif filter_name == "pro_enhance":
        img = ImageEnhance.Color(img).enhance(1.3)
        img = ImageEnhance.Contrast(img).enhance(1.5)
        img = ImageEnhance.Sharpness(img).enhance(2.2)

    elif filter_name == "beauty":
        img = img.filter(ImageFilter.SMOOTH_MORE)
        img = ImageEnhance.Brightness(img).enhance(1.2)

    elif filter_name == "skin":
        img = img.filter(ImageFilter.SMOOTH)

    elif filter_name == "blur_bg":
        img = img.filter(ImageFilter.GaussianBlur(8))

    elif filter_name == "soft_blur":
        img = img.filter(ImageFilter.BLUR)

    elif filter_name == "warm":
        img = ImageEnhance.Color(img).enhance(1.5)
        img = ImageEnhance.Brightness(img).enhance(1.2)

    elif filter_name == "cool":
        img = ImageEnhance.Color(img).enhance(0.8)
        img = ImageEnhance.Contrast(img).enhance(1.1)

    elif filter_name == "sunset":
        img = ImageEnhance.Color(img).enhance(1.7)
        img = ImageEnhance.Brightness(img).enhance(1.1)

    elif filter_name == "night":
        img = ImageEnhance.Brightness(img).enhance(0.6)
        img = ImageEnhance.Contrast(img).enhance(1.4)

    elif filter_name == "cartoon":
        img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

    elif filter_name == "dramatic":
        img = ImageEnhance.Contrast(img).enhance(2.0)
        img = ImageEnhance.Sharpness(img).enhance(2.0)

    elif filter_name == "moody":
        img = ImageEnhance.Color(img).enhance(0.6)
        img = ImageEnhance.Contrast(img).enhance(1.3)

    return img

# ==============================
# أوامر البوت
# ==============================
@bot.message_handler(commands=['start'])
def start_message(message):
    if not is_active_hours():
        bot.reply_to(message, "⏳ البوت يعمل فقط من 07:00 إلى 15:00")
        return

    if message.chat.id not in user_original_images:
        bot.send_message(
            message.chat.id,
            f"🚸| عذراً عزيزي .\n"
            f"🔰| عليك الاشتراك في قناة البوت لتتمكن من استخدامه\n\n"
            f"- {CHANNEL_LINK} \n\n"
            f"‼️| اشترك ثم ارسل /start"
        )
        user_original_images[message.chat.id] = {"stage": "channel"}
    else:
        stage = user_original_images[message.chat.id].get("stage")
        if stage == "channel":
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton("📷 تابعنا على إنستغرام", url=INSTAGRAM_LINK))
            bot.send_message(message.chat.id, "✅ الآن تابعنا على إنستغرام:", reply_markup=keyboard)
            user_original_images[message.chat.id]["stage"] = "instagram"
        elif stage == "instagram":
            bot.send_message(message.chat.id, "📸 أرسل صورة الآن لتجربة الفلاتر.")
            user_original_images[message.chat.id]["stage"] = "ready"

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    if not is_active_hours():
        bot.reply_to(message, "⏳ البوت يعمل فقط من 07:00 إلى 15:00")
        return

    file_info = bot.get_file(message.photo[-1].file_id)
    file = bot.download_file(file_info.file_path)

    user_original_images[message.chat.id]["original"] = file

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [types.InlineKeyboardButton(text, callback_data=data) for text, data in FILTERS]
    keyboard.add(*buttons)

    bot.reply_to(message, "✨ اختر فلتر من القائمة:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in [f[1] for f in FILTERS])
def callback_filter(call):
    if not is_active_hours():
        bot.answer_callback_query(call.id, "⏳ البوت يعمل فقط من 07:00 إلى 15:00")
        return

    if call.message.chat.id not in user_original_images or "original" not in user_original_images[call.message.chat.id]:
        bot.answer_callback_query(call.id, "⚠️ أرسل صورة أولاً")
        return

    img_bytes = io.BytesIO(user_original_images[call.message.chat.id]["original"])
    img = Image.open(img_bytes).convert("RGB")

    img = apply_filter(img, call.data)

    output = io.BytesIO()
    output.name = "filtered.jpg"
    img.save(output, format="JPEG")
    output.seek(0)

    bot.send_photo(call.message.chat.id, output, caption=f"✅ فلتر {call.data} مطبّق!")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if not is_active_hours():
        bot.reply_to(message, "⏳ البوت يعمل فقط من 07:00 إلى 15:00")
        return
    bot.reply_to(message, "🤖 أرسل صورة لتجربة الفلاتر.")

bot.polling()
