import io
import csv
from datetime import datetime
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from io import BytesIO
from PIL import Image
import numpy as np
import os
import torch
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import asyncio
import time
from tensorflow import keras

TOKEN = "5804669631:AAGjdkONwz3AtlRsFf-hu-dzgDtVOig3EKo"

# Load the models
model1 = keras.models.load_model('/Users/andrew/Documents/NETOPT/best_model_GA_val_loss_0.0732_val_accuracy_0.9700.h5')
model2 = keras.models.load_model("/Users/andrew/Documents/NETOPT/best_model_GA_val.loss_0.0422_val.acc_0.9896.h5")
model2.load_weights('/Users/andrew/Documents/NETOPT/best_weights_GA_val.loss_0.0422_val.acc_0.9896.h5')

# Define the classes
classes1 = ['Металл', 'Пластик']
classes2 = ['Втулки', 'Леска', 'Ободки']

async def start(update, context):
    await update.message.reply_text('Отправь этому боту фотографию.')

async def process_image(update, context):
    user = update.message.from_user
    current_time = datetime.now().strftime('%H:%M')

    with open('/Users/andrew/Documents/NETOPT/netopt.csv', 'a', newline='') as file:  
        writer = csv.writer(file)
        writer.writerow([user.id, user.username, user.first_name, current_time])

    await update.message.reply_text('Мы получили от тебя фотографию. Идет распознавание...')

    file = await context.bot.get_file(update.message.photo[-1].file_id)
    img = Image.open(BytesIO(await file.download_as_bytearray()))

    # Delete the message containing the image
    await context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)

    # Resize image to target size
    img_resized = img.resize((600, 600))

    # Crop the image
    cropped_image1 = img_resized.crop((40, 160, 560, 410))

    # Resize image for prediction
    img_resized1 = cropped_image1.resize((120, 55))  # resize images if necessary
    img_resized2 = img_resized.resize((128, 182))
    img_np1 = np.array(img_resized1)
    img_np2 = np.array(img_resized2)
    img_np1 = img_np1[np.newaxis, ...]
    img_np2 = img_np2[np.newaxis, ...]  # Add an extra dimension for the batch size

    start_time = time.perf_counter()  # <--- Use time.perf_counter() here

    # Perform inference
    with torch.no_grad():
        prediction1 = model1.predict(img_np1)
        prediction2 = model2.predict(img_np2)

    # Measure how long the inference took
    duration = time.perf_counter() - start_time  # <--- Use time.perf_counter() here

    # Determine the predicted classes
    predicted_class1 = classes1[np.argmax(prediction1)]
    predicted_class2 = classes2[np.argmax(prediction2)]

    # Create a new image with the prediction result
    fig, ax = plt.subplots()
    ax.imshow(np.array(img))
    plt.title(f'Predicted classes: {predicted_class1}, {predicted_class2}')
    
    # Save the image to a BytesIO object
    buf = io.BytesIO()
    plt.savefig(buf, format='jpg', dpi=600)
    buf.seek(0)

    # Send photo
    await update.message.reply_photo(photo=buf)

    # Send processing time
    seconds, milliseconds = divmod(duration, 1)  # <--- Update this line to get seconds and milliseconds
    await update.message.reply_text(f"Время обработки {int(seconds):02} сек {int(milliseconds*1000):03} мс")  # <--- Update this line


def main():
    application = Application.builder().token(TOKEN).build()
    print('Бот запущен...')
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.PHOTO, process_image))
    application.run_polling()

if __name__ == "__main__":
    main()
