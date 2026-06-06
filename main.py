@bot.message_handler(commands=['start'])
def start(message):

    markup = types.InlineKeyboardMarkup(row_width=1)

    markup.add(
        types.InlineKeyboardButton(
            "🎯 THAM GIA KÊNH NHẬN SỐ AI MIỄN PHÍ",
            url="https://t.me/XOSOAI88"
        )
    )

    markup.add(
        types.InlineKeyboardButton(
            "🎁 TẢI APP NHẬN +100K MIỄN PHÍ",
            url="http://ee88vn.pro/"
        )
    )

    markup.add(
        types.InlineKeyboardButton(
            "💬 CSKH HỖ TRỢ",
            url="https://t.me/CSKHEE8868"
        )
    )

    markup.add(
        types.InlineKeyboardButton(
            "👨‍💼 ADMIN",
            url="https://t.me/ANHSON8X"
        )
    )

    bot.send_message(
        message.chat.id,
        """
🎉 <b>CHÀO MỪNG BẠN ĐẾN VỚI AI DỰ ĐOÁN</b>

🤖 Nhận số AI miễn phí mỗi ngày

📢 Tham gia kênh Telegram để nhận số AI miễn phí.

🎁 Tải App nhận ngay <b>+100K MIỄN PHÍ</b>

💬 Cần hỗ trợ vui lòng liên hệ CSKH hoặc Admin.
        """,
        parse_mode="HTML",
        reply_markup=markup
    )
