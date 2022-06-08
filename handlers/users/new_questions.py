from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.utils.callback_data import CallbackData
import random
from loader import dp, db


cb_get_answers = CallbackData("get_answers", "answer_id")


@dp.message_handler(Command('start_test'))
async def get_10_random_questions_litra(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    questions = await db.select_all_questions_litra()
    questions = [dict(q) for q in random.sample(questions, 10)]
    question = questions.pop(0)
    question_text = question.get("question")
    correct = question.get("correct")
    counter = 0
    print(correct)
    variables = [question.get("first"), question.get("second"), question.get("third"),
                 question.get("fourth"), question.get("fifth")]
    for index, variable in enumerate(variables, start=1):
        keyboard.add(types.InlineKeyboardButton(text=variable,
                                                callback_data=cb_get_answers.new(answer_id=index)))

    await message.answer(f"№{10 - len(questions)}\n {question_text}", reply_markup=keyboard)
    await state.update_data(variables=variables)
    await state.update_data(correct=correct)
    await state.update_data(questions=questions)
    await state.update_data(counter=counter)


@dp.callback_query_handler(cb_get_answers.filter())
async def get_answers_call(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    data = await state.get_data()
    questions = data.get('questions')
    answer_id = int(callback_data["answer_id"])
    counter = data.get('counter')
    correct = data.get('correct')
    if answer_id == correct:
        await call.message.answer("Правильна відповідь")
        counter += 1
        await state.update_data(counter=counter)
    else:
        await call.message.answer("Неправильна відповідь")
    print(answer_id, correct)
    if questions:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        question = questions.pop(0)
        question_text = question.get("question")
        correct = question.get("correct")
        print(correct)
        variables = [question.get("first"), question.get("second"), question.get("third"),
                     question.get("fourth"), question.get("fifth")]
        for index, variable in enumerate(variables, start=1):
            keyboard.add(types.InlineKeyboardButton(text=variable,
                                                    callback_data=cb_get_answers.new(answer_id=index)))

        await call.message.answer(f"№{10 - len(questions)} {question_text}", reply_markup=keyboard)
        await state.update_data(variables=variables)
        await state.update_data(correct=correct)
        await state.update_data(questions=questions)
    else:
        await call.message.answer(f"Вітаю! Ви набрали {counter} / 10")
    await call.answer(cache_time=60)
