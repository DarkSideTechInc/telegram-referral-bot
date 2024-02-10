import random
import string
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Dictionary to store referral codes for each user
referral_codes = {}

# Function to handle /start command
def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    # Check if user is a member of the specified channel
    if is_member_of_channel(user_id):
        update.message.reply_text("Welcome to the Referral Bot! Use the buttons below to navigate.")
    else:
        update.message.reply_text("You must join our channel before using the bot.")
        update.message.reply_text("Join our channel: https://t.me/DarkSideTechInc")

# Function to check if user is a member of the specified channel
def is_member_of_channel(user_id):
    # Implement logic to check if user is a member of the specified channel
    # You can use the Telegram Bot API to check if the user is a member of the channel
    return True  # For testing purposes, always return True

# Function to handle Important message button
def important_message(update: Update, context: CallbackContext) -> None:
    reply_text = ("Please note don't try to use bots as we will be banning you from the bot!\n\n"
                  "All withdrawals can only be made at 100 Points each referral is 2 points!")
    update.message.reply_text(reply_text)

# Function to handle Refer button
def refer_user(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    # Check if user already has a referral code
    if user_id in referral_codes:
        referral_code = referral_codes[user_id]
    else:
        # Generate a unique referral code
        referral_code = generate_referral_code()
        # Save the referral code for the user
        referral_codes[user_id] = referral_code
    
    reply_text = f"Here is your referral code: {referral_code}\n\nRemember every referral is only 2 points and you need 100 Points."
    update.message.reply_text(reply_text)

# Function to handle Balance button
def balance(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    # Get user's current balance (implement this function)
    user_balance = get_user_balance(user_id)
    reply_text = f"Your current balance is: {user_balance} points."
    update.message.reply_text(reply_text)

# Function to handle Withdraw button
def withdraw(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Netflix Subscription 1 Month (150 Points)", callback_data='netflix')],
        [InlineKeyboardButton("Telegram Premium 3 Months (500 Points)", callback_data='telegram')],
        [InlineKeyboardButton("Amazon Prime Video Subscription 1 Month (100 Points)", callback_data='amazon')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("You have selected to withdraw your points. Choose one of the following services using the buttons below:", reply_markup=reply_markup)

# Function to handle button clicks for withdraw options
def handle_withdraw_options(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    service = query.data
    user_id = query.from_user.id
    user_balance = get_user_balance(user_id)
    if service == 'netflix':
        if user_balance >= 150:
            deduct_points(user_id, 150)
            query.message.reply_text("Well done! Your Netflix account will be sent to you via DM soon.")
            forward_withdrawal_message(update, user_id, "Netflix Subscription 1 Month")
        else:
            query.message.reply_text("Sorry, looks like you don't have sufficient points to make this withdrawal. Refer some more friends or try again later.")
    elif service == 'telegram':
        if user_balance >= 500:
            deduct_points(user_id, 500)
            query.message.reply_text("Well done! Your Telegram Premium account will be sent to you via DM soon.")
            forward_withdrawal_message(update, user_id, "Telegram Premium 3 Months")
        else:
            query.message.reply_text("Sorry, looks like you don't have sufficient points to make this withdrawal. Refer some more friends or try again later.")
    elif service == 'amazon':
        if user_balance >= 100:
            deduct_points(user_id, 100)
            query.message.reply_text("Well done! Your Amazon Prime Video account will be sent to you via DM soon.")
            forward_withdrawal_message(update, user_id, "Amazon Prime Video Subscription 1 Month")
        else:
            query.message.reply_text("Sorry, looks like you don't have sufficient points to make this withdrawal. Refer some more friends or try again later.")

# Function to generate custom referral code for the user
def generate_referral_code():
    # Generate a random string of alphanumeric characters
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return code

# Function to get user's current balance
def get_user_balance(user_id):
    # Implement logic to get user's current balance based on user ID
    return 50  # For testing purposes, replace with actual balance retrieval logic

# Function to deduct points from user's balance
def deduct_points(user_id, points):
    # Implement logic to deduct points from user's balance based on user ID
    pass  # Placeholder for actual deduction logic

# Function to forward withdrawal message
