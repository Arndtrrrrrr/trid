from telethon import TelegramClient, events

# 1. إعداد API ID and HASH
api_id = 23144131
api_hash = '6e814f532ba378327170d1deca5a97ce'

# 2. إعداد القنوات
source_channel = '@JokerPocetbot' # اسم المستخدم أو ID لقناة المصدر
destination_channel = '@alhawtTradingbot1' # اسم المستخدم أو ID لقناتك

# 3. إنشاء العميل
client = TelegramClient('session_name', api_id, api_hash)

# 4. دالة لمعالجة الرسائل الجديدة
@client.on(events.NewMessage(chats=source_channel))
async def new_message_handler(event):
    # الحصول على نص الرسالة
    message_text = event.message.message
    
    # تعديل نص الرسالة
    modified_text = message_text.replace('🚧 Joker Trading 🚧', '👑✨ Alhawt Trading ✨👑')
    
    # إضافة إيموجيات قوية للتداول
    modified_text = f"📈💰🚀 {modified_text}"
    
    # إرسال الرسالة المعدلة إلى قناتك
    await client.send_message(destination_channel, modified_text)
    
# 5. تشغيل العميل
async def main():
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())