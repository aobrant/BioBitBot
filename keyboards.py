from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

inline_btn_01 = InlineKeyboardButton(text='Add BioBits 🫳🏻 ', callback_data='btn_add_bits')
inline_btn_02 = InlineKeyboardButton(text='View BioBits 👀', callback_data='btn_view_bits')
inline_btn_03 = InlineKeyboardButton(text='Analyze your BioBits 📊 (under construction)',
                                     callback_data='btn_analyze_bits')
inline_btn_04 = InlineKeyboardButton(text='Set reminders ⏰(under construction)', callback_data='btn_set_bits')

inline_btn_05 = InlineKeyboardButton(text='Sports ', callback_data='btn_sports')
inline_btn_06 = InlineKeyboardButton(text='Drinks ', callback_data='btn_drinks')
inline_btn_07 = InlineKeyboardButton(text='Sleep quality ', callback_data='btn_sleep')
inline_btn_08 = InlineKeyboardButton(text='1️⃣', callback_data='btn_s1')
inline_btn_09 = InlineKeyboardButton(text='2️⃣', callback_data='btn_s2')
inline_btn_10 = InlineKeyboardButton(text='3️⃣', callback_data='btn_s3')
inline_btn_11 = InlineKeyboardButton(text='4️⃣', callback_data='btn_s4')
inline_btn_12 = InlineKeyboardButton(text='5️⃣', callback_data='btn_s5')
inline_btn_13 = InlineKeyboardButton(text='Coffee (add 1 cup) ', callback_data='btn_coffee')
inline_btn_14 = InlineKeyboardButton(text='Daily water  (add 1 liter)', callback_data='btn_water')
inline_btn_15 = InlineKeyboardButton(text='Blood pressure (XX / YY mmHg)', callback_data='btn_pressure')
inline_btn_16 = InlineKeyboardButton(text='Weight (kg)', callback_data='btn_weight')

inline_btn_16 = InlineKeyboardButton(text='Walking (km)', callback_data='btn_walk')
inline_btn_17 = InlineKeyboardButton(text='Running (km)', callback_data='btn_run')
inline_btn_18 = InlineKeyboardButton(text='Cycling (km)', callback_data='btn_cycling')
inline_btn_19 = InlineKeyboardButton(text='Fitness / Gym workouts (hours)', callback_data='btn_gym')
inline_btn_20 = InlineKeyboardButton(text='Swimming (hours)', callback_data='btn_swim')
inline_btn_21 = InlineKeyboardButton(text='Trekking / Hiking (km)', callback_data='btn_hike')
inline_btn_22 = InlineKeyboardButton(text='Tennis (hours)', callback_data='btn_tennis')

inline_btn_23 = InlineKeyboardButton(text='Beer (1 cup)', callback_data='btn_beer')
inline_btn_24 = InlineKeyboardButton(text='Wine (1 glass)', callback_data='btn_wine')
inline_btn_25 = InlineKeyboardButton(text='Vodka (1 shot)', callback_data='btn_vodka')
inline_btn_26 = InlineKeyboardButton(text='Whiskey (1 shot)', callback_data='btn_whiskey')
inline_btn_27 = InlineKeyboardButton(text='Rum (1 shot)', callback_data='btn_rum')
inline_btn_28 = InlineKeyboardButton(text='Tequila( 1 shot)', callback_data='btn_tequila')
inline_btn_29 = InlineKeyboardButton(text='Gin (1 shot)', callback_data='btn_gin')

inline_btn_30 = InlineKeyboardButton(text='⬅️ Back', callback_data='back')
inline_btn_31 = InlineKeyboardButton(text='⛪ Home', callback_data='home')
inline_btn_32 = InlineKeyboardButton(text='Weight', callback_data='weight')


inline_kb_begin = InlineKeyboardBuilder()
inline_kb_begin.row(inline_btn_01, inline_btn_02)
inline_kb_begin.row(inline_btn_03)
inline_kb_begin.row(inline_btn_04)

inline_kb_beats = InlineKeyboardBuilder()
inline_kb_beats.row(inline_btn_32)
inline_kb_beats.row(inline_btn_05, inline_btn_06)
inline_kb_beats.row(inline_btn_07)
inline_kb_beats.row(inline_btn_08, inline_btn_09, inline_btn_10, inline_btn_11, inline_btn_12, width=5)
inline_kb_beats.row(inline_btn_13, inline_btn_14)
inline_kb_beats.row(inline_btn_15)
inline_kb_beats.row(inline_btn_31)

inline_kb_sports = InlineKeyboardBuilder()
inline_kb_sports.row(inline_btn_16, inline_btn_17, inline_btn_18, inline_btn_19,
                inline_btn_20, inline_btn_21, inline_btn_22, inline_btn_31, width=1)

inline_kb_drinks = InlineKeyboardBuilder()
inline_kb_drinks.row(inline_btn_23, inline_btn_24, inline_btn_25, inline_btn_26,
                inline_btn_27, inline_btn_28, inline_btn_29, inline_btn_31, width=3)


